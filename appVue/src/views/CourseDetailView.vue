<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { supabase } from '../js/supabase.js'

const route = useRoute()
const router = useRouter()
const courseId = computed(() => route.query.id)

const course = ref(null)
const lessons = ref([])
const isLoading = ref(true)

const formatPrice = (price) => {
  return price > 0 ? `Rp ${parseInt(price).toLocaleString('id-ID')}` : 'Gratis'
}

const getBenefits = () => {
  if (!course.value?.benefits) return []
  return course.value.benefits.split(';').map(b => b.trim()).filter(b => b)
}

const getFeatures = () => {
  if (!course.value?.features) return []
  return course.value.features.split(';').map(b => b.trim()).filter(b => b)
}

const fetchCourseData = async () => {
  if (!courseId.value) {
    isLoading.value = false
    return
  }

  try {
    const { data: courseData, error } = await supabase
      .from('courses')
      .select('*, profiles(full_name, avatar_url, bio)')
      .eq('id', courseId.value)
      .single()

    if (!error && courseData) {
      course.value = courseData
    }

    const { data: lessonsData } = await supabase
      .from('lessons')
      .select('*')
      .eq('course_id', courseId.value)
      .order('order_index', { ascending: true })

    if (lessonsData) {
      lessons.value = lessonsData
    }
  } catch (err) {
    console.error('Error fetching course:', err)
  } finally {
    isLoading.value = false
  }
}

const startLearning = () => {
  if (lessons.value.length > 0) {
    router.push({ path: '/lesson', query: { course: courseId.value, lesson: lessons.value[0].id } })
  } else {
    router.push({ path: '/lesson', query: { course: courseId.value } })
  }
}

const goToLesson = (lessonId) => {
  router.push({ path: '/lesson', query: { course: courseId.value, lesson: lessonId } })
}

onMounted(() => {
  fetchCourseData()
})
</script>

<template>
  <div class="bg-background text-on-surface min-h-screen flex flex-col font-['Plus_Jakarta_Sans']">
    <!-- TopNavBar -->
    <nav class="bg-[#fbf9f1]/80 dark:bg-stone-950/80 backdrop-blur-xl docked full-width top-0 z-50 shadow-[0_20px_50px_rgba(27,28,23,0.05)]">
      <div class="flex justify-between items-center px-8 h-20 w-full max-w-screen-2xl mx-auto">
        <div class="flex items-center gap-8">
          <router-link to="/" class="text-xl font-extrabold text-stone-900 dark:text-stone-50 hover:text-primary transition-colors cursor-pointer">Sunbeam Learning</router-link>
          <div class="hidden md:flex gap-6">
            <router-link to="/" class="text-stone-600 dark:text-stone-400 font-medium font-semibold hover:text-[#745b00] transition-colors">Beranda</router-link>
            <router-link to="/courses" class="text-[#745b00] dark:text-[#f2c94c] font-bold border-b-2 border-[#f2c94c] font-semibold tracking-tight">Kelas</router-link>
            <a class="text-stone-600 dark:text-stone-400 font-medium font-semibold hover:text-[#745b00] transition-colors" href="#">Instruktur</a>
            <a class="text-stone-600 dark:text-stone-400 font-medium font-semibold hover:text-[#745b00] transition-colors" href="#">Mentor Chat</a>
          </div>
        </div>
        <div class="flex items-center gap-4">
          <div class="hidden md:block relative">
            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline">search</span>
            <input class="pl-10 pr-4 py-2 bg-surface-container-highest rounded-full border-none focus:outline-none text-sm w-64" placeholder="Search courses..." type="text" />
          </div>
          <button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors">notifications</button>
          <button class="bg-primary text-on-primary px-6 py-2 rounded-full font-bold text-sm hover:scale-105 duration-200 ease-out cursor-pointer">Masuk</button>
        </div>
      </div>
    </nav>

    <main class="max-w-screen-2xl mx-auto px-4 md:px-8 pt-8 pb-24 flex-1 w-full">
      <div v-if="isLoading" class="flex justify-center py-20">
        <span class="material-symbols-outlined text-4xl animate-spin text-primary">sync</span>
      </div>
      <div v-else-if="!course" class="text-center py-20">
        <p class="text-error text-xl">Kursus tidak ditemukan.</p>
        <router-link to="/courses" class="text-primary mt-4 inline-block font-bold">Kembali ke daftar kelas</router-link>
      </div>
      <div v-else>
        <!-- Hero Section -->
        <section class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16 items-center">
          <div class="lg:col-span-7 space-y-6">
            <div class="inline-flex items-center gap-2 bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full text-xs font-bold tracking-widest uppercase">
              <span class="material-symbols-outlined text-sm">category</span>
              {{ course.category }}
            </div>
            <h1 class="text-5xl md:text-6xl font-extrabold tracking-tight text-on-surface leading-[1.1]">{{ course.title }}</h1>
            <p class="text-lg text-on-surface-variant max-w-2xl leading-relaxed">
              {{ course.description }}
            </p>
            <div class="flex flex-wrap items-center gap-6 pt-4">
              <div class="flex items-center gap-3">
                <img class="w-12 h-12 rounded-full object-cover border-2 border-primary-container" :src="course.profiles?.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" />
                <div>
                  <p class="text-sm font-bold">{{ course.profiles?.full_name || 'Instruktur' }}</p>
                  <p class="text-xs text-on-surface-variant">Mentor Sunbeam</p>
                </div>
              </div>
              <div class="h-10 w-px bg-outline-variant opacity-30 hidden sm:block"></div>
              <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-primary-container" style="font-variation-settings: 'FILL' 1;">star</span>
                <span class="font-bold">4.9</span>
                <span class="text-sm text-on-surface-variant">(2.4k students)</span>
              </div>
            </div>
            <div class="flex items-center gap-4 pt-6">
              <button @click="startLearning" class="bg-primary text-on-primary px-8 py-4 rounded-full font-bold text-lg shadow-xl shadow-primary/20 transition-all hover:scale-105 active:scale-95">
                Enroll Now
              </button>
              <button class="flex items-center gap-2 font-bold text-primary hover:text-on-primary-fixed-variant transition-colors px-6 py-4">
                <span class="material-symbols-outlined">play_circle</span>
                Watch Trailer
              </button>
            </div>
          </div>
          <div class="lg:col-span-5 relative">
            <div class="aspect-square rounded-xl overflow-hidden shadow-2xl rotate-2 hover:rotate-0 transition-transform duration-500 bg-surface-container-high relative group">
              <img class="w-full h-full object-cover" :src="course.thumbnail_url || 'https://via.placeholder.com/600'" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </div>
            <!-- Decorative Elements -->
            <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-lg shadow-xl max-w-[200px] -rotate-3">
              <p class="text-xs font-bold text-primary mb-1 uppercase tracking-wider">Next Session</p>
              <p class="text-sm font-bold">Live Q&amp;A on Friday</p>
              <p class="text-xs text-on-surface-variant">with {{ course.profiles?.full_name || 'Instruktur' }}</p>
            </div>
            <div class="absolute -top-6 -right-6 w-24 h-24 bg-primary-container rounded-full blur-3xl opacity-30"></div>
          </div>
        </section>

        <!-- Bento Layout Content -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- Left Side: Main Content -->
          <div class="lg:col-span-2 space-y-12">
            <!-- Tentang Kursus -->
            <section id="about">
              <h2 class="text-3xl font-bold mb-6 flex items-center gap-3">
                <span class="w-10 h-1px bg-primary-container border-b-2"></span>
                Tentang Kursus
              </h2>
              <div class="bg-surface-container-low p-8 rounded-lg space-y-4">
                <p class="text-on-surface-variant leading-relaxed text-lg whitespace-pre-wrap">{{ course.description }}</p>
              </div>
            </section>
            
            <!-- Apa yang akan dipelajari -->
            <section id="outcomes">
              <h2 class="text-3xl font-bold mb-6 flex items-center gap-3">
                <span class="w-10 h-1px bg-primary-container border-b-2"></span>
                Apa yang akan dipelajari
              </h2>
              <div class="grid md:grid-cols-2 gap-4">
                <div v-if="getBenefits().length === 0" class="col-span-full text-stone-400 text-sm italic">Belum ada detail manfaat.</div>
                <div v-else v-for="item in getBenefits()" :key="item" class="flex items-start gap-3 p-4 bg-white rounded-lg shadow-sm">
                  <span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                  <span class="font-medium text-on-surface-variant">{{ item }}</span>
                </div>
              </div>
            </section>

            <!-- Kurikulum -->
            <section id="curriculum">
              <div class="flex justify-between items-end mb-8">
                <h2 class="text-3xl font-bold flex items-center gap-3">
                  <span class="w-10 h-1px bg-primary-container border-b-2"></span>
                  Kurikulum
                </h2>
                <p class="text-sm font-bold text-on-surface-variant">DAFTAR MATERI</p>
              </div>
              <div class="space-y-4">
                <p v-if="lessons.length === 0" class="p-6 text-center text-stone-500">Belum ada materi untuk kelas ini.</p>
                <div v-else v-for="(l, i) in lessons" :key="l.id" @click="goToLesson(l.id)" class="bg-surface-container-low p-6 rounded-2xl flex items-center gap-4 hover:shadow-lg transition-shadow cursor-pointer">
                  <div class="w-12 h-12 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center font-bold">
                    {{ i + 1 }}
                  </div>
                  <div class="flex-1">
                    <h4 class="font-bold text-lg mb-1">{{ l.title }}</h4>
                    <p class="text-sm text-on-surface-variant">{{ l.duration_minutes || 0 }} menit • Video</p>
                  </div>
                  <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-sm">
                    <span class="material-symbols-outlined text-primary">{{ l.is_locked ? 'lock' : 'play_arrow' }}</span>
                  </div>
                </div>
              </div>
            </section>
          </div>

          <!-- Right Side: Sticky Sidebar / Call to Action -->
          <div class="lg:col-span-1">
            <div class="sticky top-24 space-y-6">
              <div class="bg-surface-container p-8 rounded-lg shadow-sm">
                <div class="mb-6">
                  <div class="flex items-baseline gap-2 mb-1">
                    <span class="text-4xl font-black">{{ formatPrice(course.price) }}</span>
                  </div>
                </div>
                <ul class="space-y-4 mb-8">
                  <li v-if="getFeatures().length === 0" class="text-sm text-stone-400 italic">Belum ada fitur ekstra.</li>
                  <li v-else v-for="item in getFeatures()" :key="item" class="flex items-center gap-3 text-sm">
                    <span class="material-symbols-outlined text-primary text-lg">star</span>
                    {{ item }}
                  </li>
                </ul>
                <button @click="startLearning" class="w-full bg-primary text-on-primary py-4 rounded-full font-bold text-lg shadow-lg hover:bg-on-primary-fixed-variant transition-colors mb-4">
                  Mulai Belajar Sekarang
                </button>
                <p class="text-center text-xs text-on-surface-variant">Garansi 30 hari uang kembali</p>
              </div>

              <!-- Instructor Mini Card -->
              <div class="bg-white p-6 rounded-lg border border-outline-variant/10">
                <h5 class="font-bold mb-4 uppercase text-xs tracking-widest text-outline">Mentor Kamu</h5>
                <div class="flex items-start gap-4">
                  <img class="w-16 h-16 rounded-full object-cover" :src="course.profiles?.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" />
                  <div>
                    <h6 class="font-bold">{{ course.profiles?.full_name || 'Instruktur' }}</h6>
                    <p class="text-xs text-on-surface-variant leading-relaxed mb-3">
                      Telah mengajar secara global dengan fokus pada bidangnya.
                    </p>
                    <button class="text-xs font-bold text-primary flex items-center gap-1 hover:underline">
                      Lihat Profil <span class="material-symbols-outlined text-[14px]">arrow_forward</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <div class="bg-[#f5f4ec] dark:bg-stone-900 w-full rounded-t-[3rem] mt-20">
      <footer class="flex flex-col md:flex-row justify-between items-center px-12 py-16 gap-8 max-w-screen-2xl mx-auto">
        <div class="space-y-4 text-center md:text-left">
          <span class="text-xl font-bold text-stone-900 dark:text-stone-50">Sunbeam Learning</span>
          <p class="text-stone-500 dark:text-stone-400 text-sm leading-relaxed max-w-xs">© 2024 Sunbeam Learning. Learning made tactile.</p>
        </div>
        <div class="flex gap-8">
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">About Us</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Terms of Service</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Privacy Policy</a>
          <a class="text-stone-500 hover:text-stone-900 transition-colors text-sm" href="#">Help Center</a>
        </div>
      </footer>
    </div>
  </div>
</template>
