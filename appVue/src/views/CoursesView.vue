<script setup>
import { ref, onMounted, computed } from 'vue'
import { supabase } from '../lib/supabaseClient.js'

const allCourses = ref([])
const isLoading = ref(true)
const activeCategory = ref('Semua Kursus')

const categories = [
  { name: 'Semua Kursus', icon: 'grid_view' },
  { name: 'Design', icon: 'palette' },
  { name: 'Development', icon: 'code' },
  { name: 'Marketing', icon: 'campaign' },
  { name: 'Self-Growth', icon: 'psychology' }
]

const filteredCourses = computed(() => {
  if (activeCategory.value === 'Semua Kursus') {
    return allCourses.value
  }
  return allCourses.value.filter(c => c.category.toLowerCase() === activeCategory.value.toLowerCase())
})

const fetchCourses = async () => {
  isLoading.value = true
  try {
    const { data, error } = await supabase
      .from('courses')
      .select('*, profiles(full_name, avatar_url)')
      .order('created_at', { ascending: false })
    
    if (!error && data) {
      allCourses.value = data
    }
  } catch (err) {
    console.error('Error fetching courses:', err)
  } finally {
    isLoading.value = false
  }
}

const formatPrice = (price) => {
  return price > 0 ? `Rp ${parseInt(price).toLocaleString('id-ID')}` : 'Gratis'
}

onMounted(() => {
  fetchCourses()
})
</script>

<template>
  <div class="text-on-surface selection:bg-primary-container selection:text-on-primary-container bg-[#fbf9f1] min-h-screen font-body flex flex-col">
    <!-- TopNavBar -->
    <header class="bg-[#fbf9f1]/80 dark:bg-stone-950/80 backdrop-blur-xl docked full-width top-0 z-50 shadow-[0_20px_50px_rgba(27,28,23,0.05)] sticky">
      <div class="flex justify-between items-center px-8 h-20 w-full max-w-screen-2xl mx-auto">
        <router-link to="/" class="text-xl font-extrabold text-stone-900 dark:text-stone-50 tracking-tighter hover:text-primary transition-colors cursor-pointer">Sunbeam Learning</router-link>

        <nav class="hidden md:flex items-center gap-8">
          <router-link to="/" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Beranda</router-link>
          <router-link to="/courses" class="text-[#745b00] font-bold border-b-2 border-[#f2c94c] transition-colors">Kelas</router-link>
          <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Instruktur</a>
          <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Mentor Chat</a>
        </nav>

        <div class="flex items-center gap-6">
          <div class="hidden lg:flex items-center bg-surface-container-highest px-4 py-2 rounded-full">
            <span class="material-symbols-outlined text-on-surface-variant text-xl">search</span>
            <input class="bg-transparent border-none focus:outline-none text-sm font-medium ml-2 w-48" placeholder="Cari materi..." type="text" />
          </div>
          <button class="text-stone-600"><span class="material-symbols-outlined">notifications</span></button>
          <button class="bg-primary-container text-on-primary-container px-6 py-2.5 rounded-full font-bold text-sm hover:scale-95 duration-200 transition-all shadow-lg shadow-primary/10 cursor-pointer">Masuk</button>
        </div>
      </div>
    </header>

    <main class="max-w-screen-2xl mx-auto flex flex-1 w-full">
      <!-- SideNavBar / Category Filter -->
      <aside class="hidden md:flex flex-col gap-2 py-8 bg-[#f5f4ec] dark:bg-stone-900 h-screen w-72 rounded-r-[3rem] sticky top-20 shadow-xl shadow-stone-900/5 z-40">
        <div class="px-8 mb-8">
          <div class="flex items-center gap-3 mb-2">
            <img alt="Profile" class="w-10 h-10 rounded-full border-2 border-white shadow-sm" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAIzPner4oaRhIEC_9AG2WvUyguA1xPGZ6G7oXTJXTjG2sdaMIVYtE27xyhSEh300ZhxXHMl2Fsyb0m5urBM9vHqbk4soEOA92_g8gCgKHyn3yZU78a3Atqbt-ZDpwnsgxcrULziZIeNRtyFjtzd40jdcmVzzUhAx1MQI2lVZt9R4G4eWJDAEzhvIgQR7CPVjorLmYgIraatnWD6VcqR2O8KkVAQLiibnCDngtc6-skevX1LWwqaubkKKtyyOCZLmWTr8QqAhDW1G0" />
            <div>
              <p class="text-xs text-on-surface-variant font-medium">Welcome back</p>
              <p class="text-sm font-bold text-stone-900">Budi Santoso</p>
            </div>
          </div>
        </div>
        <nav class="flex flex-col gap-1">
          <div class="px-8 mb-2">
            <h3 class="text-[10px] uppercase tracking-[0.2em] font-extrabold text-outline mb-4">Categories</h3>
          </div>
          <button 
            v-for="cat in categories" :key="cat.name"
            @click="activeCategory = cat.name"
            :class="[
              'mx-4 px-6 py-3 flex items-center gap-3 rounded-full transition-all text-left',
              activeCategory === cat.name 
                ? 'bg-[#ffffff] dark:bg-stone-800 text-[#745b00] dark:text-[#f2c94c] font-bold translate-x-1' 
                : 'text-stone-500 dark:text-stone-400 hover:bg-white/50'
            ]">
            <span class="material-symbols-outlined">{{ cat.icon }}</span>
            <span class="text-sm">{{ cat.name }}</span>
          </button>
        </nav>
        <div class="mt-auto px-6 pb-24">
          <div class="bg-secondary-container p-6 rounded-xl relative overflow-hidden group">
            <div class="relative z-10">
              <p class="text-on-secondary-container font-bold text-sm mb-1">Upgrade Pro</p>
              <p class="text-on-secondary-container/70 text-xs mb-4">Dapatkan akses ke semua mentor premium.</p>
              <button class="bg-secondary text-on-secondary text-[10px] uppercase font-bold tracking-widest px-4 py-2 rounded-full hover:scale-105 transition-transform">Learn More</button>
            </div>
            <span class="material-symbols-outlined absolute -right-4 -bottom-4 text-7xl opacity-10 group-hover:rotate-12 transition-transform">auto_awesome</span>
          </div>
        </div>
      </aside>

      <!-- Main Content Area -->
      <section class="flex-1 px-6 md:px-12 py-10">
        <!-- Header Section -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
          <div>
            <span class="text-primary font-bold text-sm tracking-widest uppercase mb-2 block">Catalog</span>
            <h1 class="text-4xl md:text-5xl font-extrabold text-on-surface tracking-tight">Jelajahi Skill Baru</h1>
            <p class="text-on-surface-variant mt-4 text-lg max-w-xl leading-relaxed">Pilih kurikulum yang dirancang oleh ahli industri untuk mengakselerasi karir masa depanmu.</p>
          </div>
          <div class="flex gap-2">
            <button class="bg-surface-container-high px-5 py-2.5 rounded-full text-sm font-semibold flex items-center gap-2">
              <span class="material-symbols-outlined text-lg">filter_list</span> Filter
            </button>
            <button class="bg-surface-container-high px-5 py-2.5 rounded-full text-sm font-semibold flex items-center gap-2">
              Terbaru <span class="material-symbols-outlined text-lg">expand_more</span>
            </button>
          </div>
        </div>

        <!-- Chips Mobile Scroll -->
        <div class="flex md:hidden gap-3 overflow-x-auto pb-6 hide-scrollbar">
          <button 
            v-for="cat in categories" :key="cat.name + '-mob'"
            @click="activeCategory = cat.name"
            :class="[
              'px-6 py-2 rounded-full text-sm whitespace-nowrap',
              activeCategory === cat.name 
                ? 'bg-primary-container text-on-primary-container font-bold'
                : 'bg-surface-container-high text-on-surface-variant font-medium'
            ]">
            {{ cat.name }}
          </button>
        </div>

        <!-- Grid Content -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Loading State -->
          <div v-if="isLoading" class="col-span-full text-center py-20 text-stone-500 flex flex-col items-center">
              <span class="material-symbols-outlined text-4xl mb-4 animate-spin text-primary">sync</span>
              <p class="font-medium">Memuat data dari database...</p>
          </div>

          <!-- Empty State -->
          <div v-else-if="filteredCourses.length === 0" class="col-span-full text-center py-20 text-stone-500">
              <p class="font-medium">Belum ada kelas di kategori ini.</p>
          </div>

          <!-- Courses -->
          <router-link 
            v-else
            v-for="c in filteredCourses" :key="c.id"
            :to="'/lesson?id=' + c.id"
            class="bg-surface-container-lowest rounded-xl overflow-hidden hover:shadow-xl transition-all group flex flex-col cursor-pointer border border-stone-100">
              <div class="relative overflow-hidden h-56">
                  <img :src="c.thumbnail_url || 'https://via.placeholder.com/600'" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                  <div class="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-on-surface shadow-sm">
                      {{ c.level }}
                  </div>
              </div>
              <div class="p-6 flex flex-col flex-1">
                  <span class="text-[10px] uppercase tracking-widest font-extrabold text-primary mb-2">{{ c.category }}</span>
                  <h3 class="text-xl font-bold text-on-surface leading-tight mb-3 group-hover:text-primary transition-colors">{{ c.title }}</h3>
                  <p class="text-on-surface-variant text-sm line-clamp-2 mb-6">{{ c.description || '' }}</p>
                  <div class="mt-auto flex items-center justify-between border-t border-stone-100 pt-4">
                      <div class="flex items-center gap-3">
                          <img :src="c.profiles?.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" class="w-8 h-8 rounded-full object-cover">
                          <span class="text-xs font-bold text-on-surface-variant">{{ c.profiles?.full_name || 'Instruktur' }}</span>
                      </div>
                      <span class="text-sm font-extrabold text-primary">{{ formatPrice(c.price) }}</span>
                  </div>
              </div>
          </router-link>
        </div>

        <!-- Pagination or Load More -->
        <div class="mt-20 flex justify-center">
          <button class="bg-surface-container text-primary font-bold px-10 py-4 rounded-full hover:bg-primary-container hover:text-on-primary-container transition-all shadow-lg shadow-black/5">Muat Lebih Banyak</button>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="bg-[#f5f4ec] dark:bg-stone-900 w-full rounded-t-[3rem] mt-20 tonal-shift-bg">
      <div class="flex flex-col md:flex-row justify-between items-center px-12 py-16 gap-8 max-w-screen-2xl mx-auto">
        <div class="flex flex-col gap-4">
          <div class="text-xl font-bold text-stone-900 dark:text-stone-50">Sunbeam Learning</div>
          <p class="text-stone-500 dark:text-stone-400 font-['Plus_Jakarta_Sans'] text-sm leading-relaxed max-w-xs">© 2024 Sunbeam Learning. Learning made tactile. Designed for the curious minds of tomorrow.</p>
        </div>
        <div class="flex flex-wrap justify-center gap-8 md:gap-12">
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">About Us</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Terms of Service</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Privacy Policy</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Help Center</a>
        </div>
      </div>
    </footer>

    <!-- BottomNavBar (Mobile Only) -->
    <div class="md:hidden fixed bottom-0 left-0 w-full rounded-t-xl z-50 bg-[#fbf9f1]/90 backdrop-blur-lg shadow-[0_-10px_40px_rgba(0,0,0,0.05)]">
      <div class="flex justify-around items-center h-20 px-6 pb-2">
        <router-link to="/" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00]">
          <span class="material-symbols-outlined">home</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Beranda</span>
        </router-link>
        <router-link to="/courses" class="flex flex-col items-center justify-center text-[#745b00]">
          <span class="material-symbols-outlined">local_library</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Kelas</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style>
/* Scoped css not needed because we use tailwind */
</style>
