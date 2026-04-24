<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../js/supabase.js'

const router = useRouter()
const courses = ref([])
const isLoading = ref(true)

const fetchCourses = async () => {
  try {
    const { data, error } = await supabase
      .from('courses')
      .select('*, profiles(full_name)')
      .order('created_at', { ascending: false })
      .limit(4)

    if (!error && data) {
      courses.value = data
    }
  } catch (err) {
    console.error(err)
  } finally {
    isLoading.value = false
  }
}

const formatPrice = (price) => {
  return price > 0 ? `Rp ${parseInt(price).toLocaleString('id-ID')}` : 'Gratis'
}

const getGridClass = (index) => {
  if (index === 0) return 'md:col-span-2 md:row-span-2'
  if (index === 1) return 'md:col-span-2'
  return 'md:col-span-1'
}

onMounted(() => {
  fetchCourses()
})
</script>

<template>
  <div class="text-on-surface selection:bg-primary-container selection:text-on-primary-container min-h-screen bg-[#fbf9f1] flex flex-col font-['Plus_Jakarta_Sans']">
    <!-- TopNavBar -->
    <nav class="bg-[#fbf9f1]/80 backdrop-blur-xl fixed top-0 z-50 w-full shadow-[0_20px_50px_rgba(27,28,23,0.05)]">
      <div class="flex justify-between items-center px-8 h-20 w-full max-w-screen-2xl mx-auto">
        <router-link to="/" class="text-xl font-extrabold text-stone-900 hover:text-primary transition-colors cursor-pointer">Sunbeam Learning</router-link>

        <div class="hidden md:flex items-center gap-8">
          <router-link to="/" class="text-[#745b00] font-bold border-b-2 border-[#f2c94c] transition-colors">Beranda</router-link>
          <router-link to="/courses" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Kelas</router-link>
          <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Instruktur</a>
          <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Mentor Chat</a>
        </div>

        <div class="flex items-center gap-6">
          <span class="material-symbols-outlined text-stone-600 cursor-pointer hover:text-primary transition-all">notifications</span>
          <button class="bg-primary-container text-on-primary-container px-6 py-2.5 rounded-full font-bold hover:scale-95 duration-200 ease-out transition-transform cursor-pointer">
            Masuk
          </button>
        </div>
      </div>
    </nav>

    <main class="pt-20 flex-1">
      <!-- Hero Section -->
      <section class="relative px-8 pt-16 pb-24 overflow-hidden">
        <div class="max-w-screen-2xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
          <div class="z-10 text-center lg:text-left">
            <span class="inline-block bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full text-xs font-bold tracking-widest uppercase mb-6">Edu-Playground</span>
            <h1 class="text-5xl md:text-7xl font-extrabold text-on-surface tracking-tight leading-[1.1] mb-8">
              Belajar Santai, <span class="text-primary italic">Skill Bertambah!</span>
            </h1>
            <p class="text-lg md:text-xl text-on-surface-variant max-w-xl mb-10 leading-relaxed font-medium">
              Platform belajar online paling kasual buat kamu yang mau berkembang tanpa tekanan. Fokus ke hasil, bukan sekadar teori membosankan.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <router-link to="/courses" class="bg-primary-container text-on-primary-container px-10 py-5 rounded-full text-lg font-bold shadow-lg hover:shadow-xl transition-all hover:-translate-y-1 text-center">
                Mulai Sekarang
              </router-link>
              <button class="bg-white/50 backdrop-blur-sm text-stone-700 px-10 py-5 rounded-full text-lg font-bold hover:bg-white transition-all">
                Lihat Silabus
              </button>
            </div>
          </div>
          <div class="relative flex justify-center items-center">
            <div class="absolute w-[120%] h-[120%] bg-radial-gradient from-primary-container/20 to-transparent rounded-full blur-3xl -z-10"></div>
            <img alt="Casual student illustration" class="w-full max-w-lg drop-shadow-2xl" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBqdVmUo-phB6Ao_g8iMOWqGkRJ18U3IFOvX0fw6fEl1lD0T7gLwwSGrasuErttHLldUFRnNeLLsjhEYuPA-NQ6OXv4CtnAFwor6Ott8IjDJ4XH-gHjgYIePFEcT_5DEzlc7MF7cEQNFfXCMhuc2PFNZaTbSaifHSbtxtw4E-ugV8Uh15ajU5w6LziWyKh3zWLcDMKBc5is1J6UZaDl86wy_Z_lpRyaOIcKl8YoZ_98WQI5t2qxrMoxd-mi3JLxgEAYv2b7WcJuAxU"/>
          </div>
        </div>
      </section>

      <!-- Features -->
      <section class="px-8 py-20 bg-surface-container-low rounded-t-xl">
        <div class="max-w-screen-2xl mx-auto">
          <div class="flex flex-col md:flex-row gap-8">
            <div class="flex-1 bg-surface-container-lowest p-10 rounded-lg shadow-sm group hover:shadow-md transition-all">
              <div class="w-16 h-16 bg-primary-container/30 flex items-center justify-center rounded-2xl mb-8 group-hover:scale-110 transition-transform">
                <span class="material-symbols-outlined text-primary text-3xl">book</span>
              </div>
              <h3 class="text-2xl font-bold mb-4">Materi To-the-point</h3>
              <p class="text-on-surface-variant text-lg leading-relaxed">Nggak ada basa-basi, langsung ke intinya. Kami kurasi materi paling penting biar kamu cepet bisa praktek langsung.</p>
            </div>
            <div class="flex-1 bg-surface-container-lowest p-10 rounded-lg shadow-sm group hover:shadow-md transition-all">
              <div class="w-16 h-16 bg-secondary-container/30 flex items-center justify-center rounded-2xl mb-8 group-hover:scale-110 transition-transform">
                <span class="material-symbols-outlined text-secondary text-3xl">chat</span>
              </div>
              <h3 class="text-2xl font-bold mb-4">Mentor Friendly</h3>
              <p class="text-on-surface-variant text-lg leading-relaxed">Tanya apa aja kayak ke temen sendiri. Mentor kami asik dan siap bantu kendala kamu lewat chat personal yang santai.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Bento Course Grid -->
      <section class="px-8 py-24">
        <div class="max-w-screen-2xl mx-auto">
          <div class="flex justify-between items-end mb-12">
            <div>
              <h2 class="text-4xl font-bold tracking-tight mb-2">Featured Courses</h2>
              <p class="text-on-surface-variant font-medium">Pilih petualangan belajarmu hari ini.</p>
            </div>
            <router-link to="/courses" class="text-primary font-bold hover:underline hidden md:block">Lihat Semua Kelas</router-link>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 lg:grid-rows-[250px_250px]">
            <div v-if="isLoading" class="col-span-full text-center py-20 text-stone-500 flex flex-col items-center justify-center min-h-[300px]">
              <span class="material-symbols-outlined text-4xl mb-4 animate-spin text-primary">sync</span>
              <p class="font-medium">Memuat kelas unggulan...</p>
            </div>
            <router-link v-else v-for="(c, i) in courses" :key="c.id" :to="'/course-detail?id=' + c.id" :class="[getGridClass(i), 'bg-surface-container-lowest rounded-lg overflow-hidden group shadow-[0_10px_30px_rgba(0,0,0,0.03)] hover:shadow-xl transition-all relative cursor-pointer flex flex-col']">
              <img :src="c.thumbnail_url || 'https://via.placeholder.com/600'" :class="['w-full object-cover group-hover:scale-105 transition-transform duration-500', i === 0 ? 'h-2/3' : 'h-48']">
              <div class="p-6 md:p-8 flex-1 flex flex-col">
                <span class="text-[10px] uppercase tracking-widest font-bold text-primary mb-2 block">{{ c.category }}</span>
                <h3 :class="[i === 0 ? 'text-3xl' : 'text-xl', 'font-bold mb-4']">{{ c.title }}</h3>
                <div class="mt-auto flex justify-between items-center text-sm">
                  <span class="font-medium text-on-surface-variant">{{ c.profiles?.full_name || 'Instruktur' }}</span>
                  <span class="bg-primary-container text-on-primary-container px-3 py-1 rounded-full font-bold">{{ formatPrice(c.price) }}</span>
                </div>
              </div>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Final CTA -->
      <section class="px-8 py-16">
        <div class="max-w-screen-xl mx-auto bg-primary rounded-xl p-12 md:p-20 text-center relative overflow-hidden">
          <div class="absolute top-0 right-0 w-64 h-64 bg-primary-container rounded-full blur-[120px] -translate-y-1/2 translate-x-1/2"></div>
          <div class="relative z-10">
            <h2 class="text-4xl md:text-5xl font-extrabold text-white mb-6">Siap Belajar Tanpa Beban?</h2>
            <p class="text-primary-container text-lg md:text-xl font-medium mb-10 opacity-90 max-w-2xl mx-auto">Gabung dengan 10.000+ pelajar lainnya yang sudah mulai bertumbuh dengan cara paling asik.</p>
            <button class="bg-white text-primary px-12 py-5 rounded-full text-xl font-bold hover:scale-105 transition-transform">Daftar Sekarang Juga</button>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="bg-surface-container rounded-t-xl mt-20">
      <div class="flex flex-col md:flex-row justify-between items-center px-12 py-16 gap-8 max-w-screen-2xl mx-auto">
        <div class="flex flex-col gap-4 text-center md:text-left">
          <div class="text-xl font-bold text-stone-900">Sunbeam Learning</div>
          <p class="text-stone-500 max-w-xs text-sm leading-relaxed">© 2024 Sunbeam Learning. Learning made tactile.</p>
        </div>
        <div class="flex gap-8">
          <a class="text-stone-500 font-medium hover:text-stone-900 transition-colors" href="#">About Us</a>
          <a class="text-stone-500 font-medium hover:text-stone-900 transition-colors" href="#">Terms of Service</a>
          <a class="text-stone-500 font-medium hover:text-stone-900 transition-colors" href="#">Privacy Policy</a>
          <a class="text-stone-500 font-medium hover:text-stone-900 transition-colors" href="#">Help Center</a>
        </div>
      </div>
    </footer>

    <!-- BottomNavBar (Mobile Only) -->
    <div class="md:hidden fixed bottom-0 left-0 w-full rounded-t-xl z-50 bg-[#fbf9f1]/90 backdrop-blur-lg shadow-[0_-10px_40px_rgba(0,0,0,0.05)]">
      <div class="flex justify-around items-center h-20 px-6 pb-2">
        <router-link to="/" class="flex flex-col items-center justify-center text-[#745b00]">
          <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">home</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Beranda</span>
        </router-link>
        <router-link to="/courses" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00]">
          <span class="material-symbols-outlined">local_library</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Kelas</span>
        </router-link>
      </div>
    </div>
  </div>
</template>
