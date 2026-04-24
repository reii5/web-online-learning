<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../js/supabase.js'

const router = useRouter()
const isAccessDenied = ref(false)
const userProfile = ref(null)
const courses = ref([])
const newCourse = ref({
  title: '',
  category: 'Design',
  level: 'Beginner',
  description: '',
  benefits: '',
  features: '',
  price: 0,
  thumbnail_url: ''
})
const newLesson = ref({
  course_id: '',
  title: '',
  order_index: 1,
  video_url: '',
  duration_minutes: 10
})

const checkAuth = async () => {
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) {
    router.push('/login')
    return
  }

  const { data: profile } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', user.id)
    .single()

  if (!profile || (profile.role !== 'instructor' && profile.role !== 'admin')) {
    isAccessDenied.value = true
    return
  }

  userProfile.value = profile
  loadCourses()
}

const loadCourses = async () => {
  if (!userProfile.value) return
  const { data } = await supabase
    .from('courses')
    .select('*')
    .eq('instructor_id', userProfile.value.id)
    .order('created_at', { ascending: false })
  
  if (data) courses.value = data
}

const deleteCourse = async (courseId) => {
  if (!confirm('Apakah Anda yakin ingin menghapus kelas ini?')) return
  const { error } = await supabase.from('courses').delete().eq('id', courseId)
  if (error) {
    alert('Gagal menghapus kelas: ' + error.message)
  } else {
    loadCourses()
  }
}

const addCourse = async () => {
  if (!userProfile.value) return
  const courseData = {
    ...newCourse.value,
    instructor_id: userProfile.value.id
  }
  const { error } = await supabase.from('courses').insert([courseData])
  if (error) {
    alert('Gagal menambah kelas: ' + error.message)
  } else {
    newCourse.value = { title: '', category: 'Design', level: 'Beginner', description: '', benefits: '', features: '', price: 0, thumbnail_url: '' }
    loadCourses()
  }
}

const addLesson = async () => {
  if (!newLesson.value.course_id) {
    alert('Pilih kelas terlebih dahulu!')
    return
  }
  const lessonData = {
    ...newLesson.value,
    is_locked: false
  }
  const { error } = await supabase.from('lessons').insert([lessonData])
  if (error) {
    alert('Gagal menambah materi: ' + error.message)
  } else {
    newLesson.value.title = ''
    newLesson.value.video_url = ''
    newLesson.value.order_index++
  }
}

const handleLogout = async () => {
  await supabase.auth.signOut()
  router.push('/')
}

onMounted(() => {
  checkAuth()
})
</script>

<template>
  <div class="text-on-surface min-h-screen relative overflow-hidden flex font-['Plus_Jakarta_Sans'] bg-surface">
    <!-- Restrict Access Overlay -->
    <div v-if="isAccessDenied" class="fixed inset-0 z-[100] bg-surface flex flex-col items-center justify-center backdrop-blur-md">
      <div class="bg-white p-10 rounded-3xl shadow-2xl border border-stone-100 text-center max-w-md mx-4">
        <div class="w-20 h-20 bg-red-100 text-red-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <span class="material-symbols-outlined text-4xl">lock</span>
        </div>
        <h1 class="text-2xl font-bold mb-3">Akses Ditolak</h1>
        <p class="text-on-surface-variant mb-8 text-sm leading-relaxed">Workspace ini eksklusif untuk Instruktur dan Administrator.</p>
        <router-link to="/" class="bg-stone-900 text-white w-full block py-3 rounded-xl font-bold hover:bg-stone-800">Kembali ke Beranda</router-link>
      </div>
    </div>

    <!-- Sidebar -->
    <aside class="w-72 bg-white border-r border-stone-100 flex flex-col h-screen z-20 shrink-0 hidden md:flex">
      <div class="h-20 px-8 flex items-center border-b border-stone-100 shrink-0">
        <router-link to="/" class="text-xl font-extrabold text-stone-900 flex items-center gap-2">
          <div class="w-8 h-8 bg-primary-container rounded-lg flex items-center justify-center">
            <span class="material-symbols-outlined text-on-primary-container text-lg">school</span>
          </div>
          Sunbeam<span class="text-stone-400 font-normal">Workspace</span>
        </router-link>
      </div>
      <div class="mt-auto p-6 border-t border-stone-100">
        <button @click="handleLogout" class="w-full flex items-center justify-center gap-2 text-stone-500 hover:text-red-600 hover:bg-red-50 px-4 py-3 rounded-xl font-bold border border-stone-200">
          <span class="material-symbols-outlined text-xl">logout</span> Keluar
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 h-screen overflow-y-auto flex flex-col">
      <header class="h-20 px-6 md:px-10 flex items-center justify-between sticky top-0 z-10 shrink-0 bg-[#fbf9f1]/80 backdrop-blur-xl border-b border-stone-100">
        <div>
          <h2 class="text-[10px] md:text-sm font-bold text-stone-500 uppercase tracking-widest">Overview</h2>
          <h1 class="text-lg md:text-xl font-bold text-stone-900">Selamat datang kembali!</h1>
        </div>
        <div class="flex items-center gap-3">
          <div class="text-right hidden md:block">
            <p class="font-bold text-sm text-stone-900">{{ userProfile?.full_name || 'Loading...' }}</p>
            <p class="text-xs text-stone-500 font-medium">Instruktur</p>
          </div>
          <div class="w-11 h-11 rounded-full overflow-hidden border-2 border-transparent">
            <img :src="userProfile?.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" class="w-full h-full object-cover">
          </div>
        </div>
      </header>

      <div class="p-6 md:p-10 max-w-7xl mx-auto w-full flex-1 space-y-10">
        <!-- Forms Section Layout -->
        <div class="grid grid-cols-1 xl:grid-cols-2 gap-10">
          <!-- KIRI: Add Course -->
          <div class="bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.03)] border border-stone-100 p-6 md:p-8 flex flex-col">
            <h3 class="text-2xl font-bold text-stone-900 mb-6">Buat Kelas Baru</h3>
            <form @submit.prevent="addCourse" class="space-y-6 flex-1 flex flex-col">
              <div class="space-y-4 flex-1">
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">Judul Kelas</label>
                  <input v-model="newCourse.title" required class="w-full bg-white border border-stone-200 rounded-xl px-4 py-3" placeholder="Misal: UI/UX Design Masterclass">
                </div>
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">Deskripsi</label>
                  <textarea v-model="newCourse.description" required rows="2" class="w-full border border-stone-200 rounded-xl px-4 py-3"></textarea>
                </div>
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">URL Cover</label>
                  <input v-model="newCourse.thumbnail_url" required class="w-full border border-stone-200 rounded-xl px-4 py-3" placeholder="https://...">
                </div>
              </div>
              <div class="pt-6 mt-auto">
                <button type="submit" class="w-full bg-stone-900 text-white font-bold px-8 py-4 rounded-xl hover:bg-stone-800">
                  Terbitkan Kelas
                </button>
              </div>
            </form>
          </div>

          <!-- KANAN: Add Lesson & List -->
          <div class="space-y-10 flex flex-col h-full">
            <!-- Add Lesson -->
            <div class="bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.03)] border border-stone-100 p-6 md:p-8">
              <h3 class="text-xl font-bold text-stone-900 mb-6">Tambah Materi Video</h3>
              <form @submit.prevent="addLesson" class="space-y-4">
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">Pilih Kelas</label>
                  <select v-model="newLesson.course_id" required class="w-full border border-stone-200 rounded-xl px-4 py-3">
                    <option disabled value="">Memuat kelas...</option>
                    <option v-for="c in courses" :key="c.id" :value="c.id">{{ c.title }}</option>
                  </select>
                </div>
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">Judul Materi</label>
                  <input v-model="newLesson.title" required class="w-full border border-stone-200 rounded-xl px-4 py-3" placeholder="Bab 1...">
                </div>
                <div>
                  <label class="block text-[10px] uppercase font-bold text-stone-500 mb-1">URL Video</label>
                  <input v-model="newLesson.video_url" required class="w-full border border-stone-200 rounded-xl px-4 py-3" placeholder="https://...">
                </div>
                <div class="pt-2">
                  <button type="submit" class="w-full bg-secondary text-white font-bold px-8 py-3 rounded-xl hover:bg-[#2a5153]">
                    Unggah Materi
                  </button>
                </div>
              </form>
            </div>

            <!-- Manage Courses List -->
            <div class="bg-white rounded-[2rem] shadow-[0_10px_40px_rgba(0,0,0,0.03)] border border-stone-100 p-6 md:p-8 flex-1 flex flex-col min-h-[300px]">
              <h3 class="text-xl font-bold text-stone-900 mb-6">Arsip Kelas</h3>
              <div class="flex-1 overflow-y-auto space-y-3">
                <div v-if="courses.length === 0" class="text-center p-6 border-2 border-dashed border-stone-200 rounded-2xl">
                  <p class="text-stone-500 font-medium text-sm">Belum ada kelas.</p>
                </div>
                <div v-else v-for="c in courses" :key="c.id" class="flex items-center gap-4 p-3 border border-stone-100 rounded-2xl group">
                  <div class="flex-1 min-w-0 cursor-pointer" @click="router.push('/course-detail?id='+c.id)">
                    <h4 class="font-bold text-stone-900 truncate group-hover:text-primary transition-colors">{{ c.title }}</h4>
                    <span class="text-[10px] font-bold uppercase tracking-widest text-primary bg-primary-container/20 px-2 rounded-md">{{ c.category }}</span>
                  </div>
                  <button @click="deleteCourse(c.id)" class="w-8 h-8 rounded-full bg-red-50 text-red-500 flex items-center justify-center hover:bg-red-500 hover:text-white">
                    <span class="material-symbols-outlined text-[16px]">delete</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>
