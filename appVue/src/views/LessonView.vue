<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { supabase } from '../js/supabase.js'

const route = useRoute()
const router = useRouter()

const course = ref(null)
const lessons = ref([])
const currentLesson = ref(null)
const isLoading = ref(true)

const courseId = computed(() => route.query.course)
const lessonId = computed(() => route.query.lesson)

const getYouTubeEmbed = (url) => {
  if (!url) return ''
  let videoId = ''
  const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([^&?]+)/)
  if (match && match[1]) {
    videoId = match[1]
  }
  return videoId ? `https://www.youtube.com/embed/${videoId}?rel=0` : url
}

const fetchLessonData = async () => {
  if (!courseId.value) {
    isLoading.value = false
    return
  }

  isLoading.value = true
  try {
    const { data: courseData } = await supabase.from('courses').select('*').eq('id', courseId.value).single()
    course.value = courseData

    const { data: lessonsData } = await supabase
      .from('lessons')
      .select('*')
      .eq('course_id', courseId.value)
      .order('order_index', { ascending: true })

    if (lessonsData && lessonsData.length > 0) {
      lessons.value = lessonsData
      
      if (lessonId.value) {
        currentLesson.value = lessonsData.find(l => l.id == lessonId.value) || lessonsData[0]
      } else {
        currentLesson.value = lessonsData[0]
      }
    } else {
      lessons.value = []
      currentLesson.value = null
    }
  } catch (err) {
    console.error('Error fetching lesson:', err)
  } finally {
    isLoading.value = false
  }
}

const goToLesson = (id) => {
  router.push({ path: '/lesson', query: { course: courseId.value, lesson: id } })
}

watch(() => route.query, () => {
  fetchLessonData()
})

onMounted(() => {
  fetchLessonData()
})
</script>

<template>
  <div class="bg-surface text-on-surface selection:bg-primary-container selection:text-on-primary-container min-h-screen font-body flex flex-col">
    <!-- TopNavBar -->
    <header class="bg-[#fbf9f1]/80 dark:bg-stone-950/80 backdrop-blur-xl docked full-width top-0 z-50 shadow-[0_20px_50px_rgba(27,28,23,0.05)]">
      <div class="flex justify-between items-center px-8 h-20 w-full max-w-screen-2xl mx-auto">
        <div class="flex items-center gap-8">
          <router-link to="/" class="text-xl font-extrabold text-stone-900 dark:text-stone-50 tracking-tighter hover:text-primary transition-colors cursor-pointer">Sunbeam Learning</router-link>
          <nav class="hidden md:flex gap-6">
            <router-link to="/" class="text-stone-600 dark:text-stone-400 font-semibold tracking-tight hover:text-[#745b00] dark:hover:text-[#f2c94c] transition-colors">Beranda</router-link>
            <router-link to="/courses" class="text-[#745b00] dark:text-[#f2c94c] font-bold border-b-2 border-[#f2c94c] font-semibold tracking-tight">Kelas</router-link>
            <a class="text-stone-600 dark:text-stone-400 font-semibold tracking-tight hover:text-[#745b00] dark:hover:text-[#f2c94c] transition-colors" href="#">Instruktur</a>
            <a class="text-stone-600 dark:text-stone-400 font-semibold tracking-tight hover:text-[#745b00] dark:hover:text-[#f2c94c] transition-colors" href="#">Mentor Chat</a>
          </nav>
        </div>
        <div class="flex items-center gap-6">
          <div class="hidden lg:flex items-center bg-surface-container-highest px-4 py-2 rounded-full gap-2">
            <span class="material-symbols-outlined text-outline">search</span>
            <input class="bg-transparent border-none focus:outline-none text-sm w-48 font-medium" placeholder="Search lessons..." type="text"/>
          </div>
          <button class="text-on-surface-variant hover:text-primary transition-colors"><span class="material-symbols-outlined">notifications</span></button>
          <div class="h-10 w-10 rounded-full overflow-hidden border-2 border-primary-container">
            <img alt="User avatar" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDKdyyV7dj7XfR4eCgkiD8ETAffA_PuL42rAT6J1OLIH4qah0WXLyM0i3wEbEYU-kCskOav2DHRu5ttHIM1lnmjDh8rRFUT7hCWHFLD_mLhEAJb-1alUFC3e2WWEIzf081UWdAjwPSpygbGGyuwNkgA6RZPt2i_iKv7t2IxzSFy8CCk3uH_EXuUDquHIrFZN3L1CoA5qvG4oGRVKZM1gGVQ9lTsALtLtZ1dU21HTg61nzo2G_YSr7qHz8PTZrAZvt3AV6owbyvsMZg"/>
          </div>
        </div>
      </div>
    </header>

    <main class="max-w-screen-2xl mx-auto px-8 pt-10 pb-12 w-full flex-1">
      <div v-if="isLoading" class="flex justify-center items-center h-64">
        <span class="material-symbols-outlined text-white animate-spin text-5xl">sync</span>
      </div>
      <div v-else-if="!courseId" class="text-center py-20 text-error">
        Akses tidak valid. Parameter kursus tidak ditemukan.
      </div>
      <div v-else>
        <!-- Breadcrumb Header -->
        <nav class="flex items-center gap-2 mb-8 text-sm font-medium">
          <router-link to="/courses" class="text-on-surface-variant hover:text-primary transition-colors">{{ course?.title || 'Kelas' }}</router-link>
          <span class="material-symbols-outlined text-outline-variant text-xs">chevron_right</span>
          <span class="text-primary font-bold">{{ currentLesson?.title || 'Materi' }}</span>
        </nav>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <!-- Video Player Column -->
          <section class="lg:col-span-8 flex flex-col gap-8">
            <!-- Large Video Player with Tactile Design -->
            <div class="relative aspect-video bg-black rounded-xl overflow-hidden shadow-2xl group border-8 border-surface-container flex items-center justify-center">
                <iframe v-if="currentLesson?.video_url" class="w-full h-full" :src="getYouTubeEmbed(currentLesson.video_url)" :title="currentLesson.title" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                <div v-else class="text-white text-center">Video tidak tersedia.</div>
            </div>
            
            <!-- Lesson Info Content -->
            <div class="bg-surface-container-lowest p-10 rounded-xl">
              <h1 class="text-4xl font-extrabold text-on-surface tracking-tight mb-4">{{ currentLesson?.title || course?.title || 'Tanpa Judul' }}</h1>
              <p class="text-lg text-on-surface-variant leading-relaxed mb-8">
                  {{ currentLesson?.description || course?.description || 'Instruktur belum mengunggah materi apapun.' }}
              </p>
              <div class="flex flex-wrap gap-4">
                <div class="flex items-center gap-2 bg-secondary-container/50 px-4 py-2 rounded-full text-on-secondary-container font-semibold text-sm">
                  <span class="material-symbols-outlined text-lg">download</span>
                  Resource Pack (PDF)
                </div>
                <div class="flex items-center gap-2 bg-tertiary-container/30 px-4 py-2 rounded-full text-on-tertiary-container font-semibold text-sm">
                  <span class="material-symbols-outlined text-lg">description</span>
                  Color Study Workbook
                </div>
              </div>
            </div>
          </section>

          <!-- Lesson Sidebar Column -->
          <aside class="lg:col-span-4 sticky top-28 bg-surface-container-low rounded-xl flex flex-col h-[calc(100vh-10rem)] overflow-hidden shadow-xl shadow-stone-900/5">
            <div class="p-8 border-b border-outline-variant/10">
              <h2 class="text-xl font-extrabold text-on-surface mb-2">Course Progress</h2>
              <div class="flex items-center gap-3">
                <div class="flex-1 h-3 bg-surface-container-highest rounded-full overflow-hidden">
                  <div class="h-full w-[65%] bg-primary shadow-[0_0_8px_rgba(116,91,0,0.2)] rounded-full"></div>
                </div>
                <span class="text-sm font-bold text-primary">65%</span>
              </div>
            </div>
            
            <div class="flex-1 overflow-y-auto p-4 space-y-2">
              <div v-if="lessons.length === 0" class="p-4 text-center text-sm text-stone-500">Belum ada materi.</div>
              <div v-else v-for="(l, i) in lessons" :key="l.id" class="space-y-2">
                  <div class="flex items-center gap-3 px-4 py-2">
                      <span class="text-[10px] font-black uppercase tracking-widest text-outline">Bagian {{ i + 1 }}</span>
                      <div class="h-px flex-1 bg-outline-variant/20"></div>
                  </div>
                  <div @click="goToLesson(l.id)" 
                      :class="[
                        'flex items-center gap-4 px-4 py-4 rounded-lg cursor-pointer transition-all',
                        currentLesson?.id === l.id ? 'bg-surface-container-lowest shadow-sm border border-primary/10' : 'hover:bg-surface-container-highest/40'
                      ]">
                      <div :class="[
                        'flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center',
                        currentLesson?.id === l.id ? 'bg-primary-container text-on-primary-container' : 'bg-surface-container-highest text-outline'
                      ]">
                          <span class="material-symbols-outlined text-sm" :style="currentLesson?.id === l.id ? 'font-variation-settings: \'FILL\' 1;' : ''">{{ currentLesson?.id === l.id ? 'play_circle' : 'play_arrow' }}</span>
                      </div>
                      <div class="flex-1">
                          <p :class="['text-sm font-bold', currentLesson?.id === l.id ? 'text-primary' : 'text-on-surface-variant']">{{ l.title }}</p>
                          <p :class="['text-[10px] font-medium', currentLesson?.id === l.id ? 'text-primary/70' : 'text-outline']">
                              {{ l.duration_minutes || '0' }} menit <span v-if="currentLesson?.id === l.id">• SEDANG DITONTON</span>
                          </p>
                      </div>
                  </div>
              </div>
            </div>
            
            <div class="p-6 bg-surface-container-highest/30">
              <button class="w-full py-4 bg-on-surface text-surface rounded-xl font-bold tracking-tight hover:scale-[1.02] transition-transform active:scale-95 shadow-lg">
                  Discussion Forum (12)
              </button>
            </div>
          </aside>
        </div>
      </div>
    </main>

    <!-- Global Footer (Shared Component) -->
    <div class="w-full bg-[#f5f4ec] dark:bg-stone-900 mt-24">
      <footer class="flex flex-col md:flex-row justify-between items-center px-12 py-16 gap-8 max-w-screen-2xl mx-auto">
        <div class="flex flex-col gap-4 text-center md:text-left">
          <span class="text-xl font-bold text-stone-900 dark:text-stone-50">Sunbeam Learning</span>
          <p class="text-sm leading-relaxed text-stone-500 dark:text-stone-400 max-w-xs">© 2024 Sunbeam Learning. Learning made tactile.</p>
        </div>
        <div class="flex gap-8">
          <a class="text-stone-500 dark:text-stone-400 font-medium hover:text-stone-900 transition-colors" href="#">About Us</a>
          <a class="text-stone-500 dark:text-stone-400 font-medium hover:text-stone-900 transition-colors" href="#">Terms of Service</a>
          <a class="text-stone-500 dark:text-stone-400 font-medium hover:text-stone-900 transition-colors" href="#">Privacy Policy</a>
          <a class="text-stone-500 dark:text-stone-400 font-medium hover:text-stone-900 transition-colors" href="#">Help Center</a>
        </div>
      </footer>
    </div>
  </div>
</template>
