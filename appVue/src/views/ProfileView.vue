<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../lib/supabaseClient.js'

const router = useRouter()
const user = ref(null)
const profile = ref({
  full_name: '',
  avatar_url: '',
  role: ''
})
const isLoading = ref(true)
const isSaving = ref(false)

const checkAuth = async () => {
  const { data: { user: currentUser } } = await supabase.auth.getUser()
  if (!currentUser) {
    router.push('/login')
    return
  }
  user.value = currentUser

  const { data: profileData } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', currentUser.id)
    .single()

  if (profileData) {
    profile.value = profileData
  }
  isLoading.value = false
}

const handleLogout = async () => {
  await supabase.auth.signOut()
  router.push('/')
}

const saveChanges = async () => {
  isSaving.value = true
  const { error } = await supabase
    .from('profiles')
    .update({ full_name: profile.value.full_name })
    .eq('id', user.value.id)

  if (!error) {
    alert('Profil berhasil diperbarui!')
  } else {
    alert('Gagal menyimpan profil: ' + error.message)
  }
  isSaving.value = false
}

onMounted(() => {
  checkAuth()
})
</script>

<template>
  <div class="bg-background text-on-surface min-h-screen font-['Plus_Jakarta_Sans']">
    <!-- TopAppBar -->
    <header class="fixed top-0 w-full z-50 flex justify-between items-center px-6 py-4 max-w-7xl mx-auto bg-stone-50/80 dark:bg-stone-900/80 backdrop-blur-xl transition-all">
      <router-link to="/" class="text-2xl font-bold text-yellow-800 dark:text-yellow-400 tracking-tight hover:text-primary transition-colors cursor-pointer">Sunbeam</router-link>

      <nav class="hidden md:flex items-center gap-8">
        <router-link to="/" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Beranda</router-link>
        <router-link to="/courses" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Kelas</router-link>
        <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Instruktur</a>
        <a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="#">Mentor Chat</a>
      </nav>

      <div class="flex items-center gap-4">
        <button class="p-2 rounded-full hover:bg-stone-200/50 transition-all active:scale-95">
          <span class="material-symbols-outlined text-stone-500">help</span>
        </button>
        <button @click="handleLogout" class="p-2 rounded-full hover:bg-stone-200/50 transition-all active:scale-95 cursor-pointer">
          <span class="material-symbols-outlined text-stone-500">logout</span>
        </button>
        <div class="w-10 h-10 rounded-full overflow-hidden bg-surface-container-high border-2 border-primary-container">
          <img :src="profile.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" class="w-full h-full object-cover">
        </div>
      </div>
    </header>

    <main v-if="!isLoading" class="max-w-4xl mx-auto px-6 pt-32 pb-40">
      <!-- Profile Hero Section -->
      <section class="mb-12 flex flex-col md:flex-row items-center md:items-end gap-8 bg-surface-container-low p-10 rounded-xl relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-primary-container/20 rounded-full -mr-20 -mt-20 blur-3xl"></div>
        <div class="relative z-10 w-32 h-32 md:w-40 md:h-40 rounded-full border-4 border-surface-container-lowest shadow-xl overflow-hidden">
          <img :src="profile.avatar_url || 'https://cdn-icons-png.flaticon.com/512/149/149071.png'" class="w-full h-full object-cover">
        </div>
        <div class="relative z-10 text-center md:text-left">
          <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-on-surface mb-2">{{ profile.full_name || 'Student' }}</h1>
          <p class="text-on-surface-variant font-medium opacity-80">Premium Learner • Member since 2023</p>
          <div class="mt-4 flex gap-3 justify-center md:justify-start">
            <span class="bg-primary-container/30 text-on-primary-container px-4 py-1.5 rounded-full text-sm font-bold tracking-wide">64% COURSE PROGRESS</span>
          </div>
          <div v-if="profile.role === 'instructor' || profile.role === 'admin'" class="mt-6">
            <router-link to="/admin" class="bg-stone-900 text-white px-6 py-2.5 rounded-full font-bold text-sm hover:scale-105 transition-transform flex items-center justify-center md:justify-start gap-2 mx-auto md:mx-0 shadow-lg shadow-stone-900/20 cursor-pointer inline-flex">
              <span class="material-symbols-outlined text-lg">dashboard</span> Buka Dashboard Instruktur
            </router-link>
          </div>
        </div>
      </section>

      <div class="grid grid-cols-1 gap-8">
        <!-- Account Information -->
        <section class="bg-surface-container-lowest p-8 md:p-10 rounded-lg">
          <div class="flex items-center gap-4 mb-8">
            <div class="w-12 h-12 rounded-full bg-primary-container flex items-center justify-center">
              <span class="material-symbols-outlined text-on-primary-container">person</span>
            </div>
            <h2 class="text-2xl font-bold tracking-tight">Account Information</h2>
          </div>
          <div class="grid md:grid-cols-2 gap-6">
            <div class="space-y-2">
              <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-1">Full Name</label>
              <input v-model="profile.full_name" class="w-full bg-surface-container-highest border-none rounded-xl px-5 py-4 text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" type="text" />
            </div>
            <div class="space-y-2">
              <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-1">Email Address</label>
              <input :value="user?.email" class="w-full bg-surface-container-highest border-none rounded-xl px-5 py-4 text-on-surface transition-all opacity-70" type="email" readonly />
            </div>
          </div>
          <div class="mt-8 flex justify-end">
            <button @click="saveChanges" :disabled="isSaving" class="bg-primary-container hover:shadow-lg hover:brightness-105 active:scale-95 transition-all text-on-primary-container font-bold px-8 py-3 rounded-full cursor-pointer">
              {{ isSaving ? 'Saving...' : 'Save Changes' }}
            </button>
          </div>
        </section>

        <!-- Settings Grid -->
        <div class="grid md:grid-cols-2 gap-8">
          <section class="bg-surface-container-lowest p-8 rounded-lg flex flex-col">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 rounded-full bg-secondary-container flex items-center justify-center">
                <span class="material-symbols-outlined text-secondary">notifications</span>
              </div>
              <h2 class="text-xl font-bold tracking-tight">Notifications</h2>
            </div>
            <div class="space-y-6 flex-grow">
              <div class="flex items-center justify-between p-4 bg-surface-container-low rounded-xl">
                <div>
                  <p class="font-bold text-on-surface">Email Notifications</p>
                  <p class="text-xs text-on-surface-variant">Weekly progress reports</p>
                </div>
                <button class="w-14 h-8 bg-primary-container rounded-full relative transition-all shadow-inner">
                  <div class="absolute right-1 top-1 w-6 h-6 bg-white rounded-full shadow-md"></div>
                </button>
              </div>
            </div>
          </section>

          <section class="bg-surface-container-lowest p-8 rounded-lg flex flex-col">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 rounded-full bg-tertiary-container flex items-center justify-center">
                <span class="material-symbols-outlined text-on-tertiary-container">security</span>
              </div>
              <h2 class="text-xl font-bold tracking-tight">Privacy Settings</h2>
            </div>
            <div class="space-y-6 flex-grow">
              <div class="flex items-center justify-between p-4 bg-surface-container-low rounded-xl">
                <div>
                  <p class="font-bold text-on-surface">Public Profile</p>
                  <p class="text-xs text-on-surface-variant">Let others see your profile</p>
                </div>
                <button class="w-14 h-8 bg-surface-container-highest rounded-full relative transition-all shadow-inner">
                  <div class="absolute left-1 top-1 w-6 h-6 bg-white rounded-full shadow-md"></div>
                </button>
              </div>
            </div>
          </section>
        </div>
      </div>
    </main>

    <!-- BottomNavBar (Mobile Only) -->
    <div class="md:hidden fixed bottom-0 left-0 w-full rounded-t-xl z-50 bg-[#fbf9f1]/90 backdrop-blur-lg shadow-[0_-10px_40px_rgba(0,0,0,0.05)]">
      <div class="flex justify-around items-center h-20 px-6 pb-2">
        <router-link to="/" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00]">
          <span class="material-symbols-outlined">home</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Beranda</span>
        </router-link>
        <router-link to="/courses" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00]">
          <span class="material-symbols-outlined">local_library</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Kelas</span>
        </router-link>
        <router-link to="/profile" class="flex flex-col items-center justify-center text-[#745b00]">
          <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">account_circle</span>
          <span class="text-[10px] uppercase tracking-widest font-bold">Profil</span>
        </router-link>
      </div>
    </div>
  </div>
</template>
