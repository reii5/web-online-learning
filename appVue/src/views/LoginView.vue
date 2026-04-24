<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../lib/supabaseClient.js'

const router = useRouter()
const email = ref('')
const password = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  const { data, error } = await supabase.auth.signInWithPassword({
    email: email.value,
    password: password.value
  })

  if (error) {
    alert('Gagal masuk: ' + error.message)
    isLoading.value = false
  } else {
    alert('Berhasil masuk!')
    router.push('/profile') // Or to profile if that's what the user prefers
  }
}
</script>

<template>
  <div class="bg-surface text-on-surface min-h-screen flex items-center justify-center relative overflow-hidden font-['Plus_Jakarta_Sans']">
    <!-- Background Decor -->
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-primary-container/20 rounded-full blur-3xl -z-10 translate-x-1/2 -translate-y-1/2"></div>
    <div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] bg-secondary-container/20 rounded-full blur-3xl -z-10 -translate-x-1/3 translate-y-1/3"></div>

    <div class="w-full max-w-5xl mx-auto p-6 md:p-12 flex flex-col md:flex-row items-center gap-12 z-10">
      <!-- Left Side: Hero Text -->
      <div class="flex-1 text-center md:text-left">
        <router-link to="/" class="inline-block text-3xl font-extrabold text-stone-900 hover:text-primary transition-colors cursor-pointer mb-8">Sunbeam Learning</router-link>
        <h1 class="text-4xl md:text-6xl font-black text-[#745b00] tracking-tight leading-tight mb-6">
          Lanjutkan <br/>
          Perjalanan <br/>
          Belajarmu.
        </h1>
        <p class="text-on-surface-variant text-lg font-medium">Akses ribuan materi, lanjutkan proyekmu, dan hubungi mentor-mu hari ini.</p>
      </div>

      <!-- Right Side: Login Card -->
      <div class="w-full max-w-md bg-white/60 backdrop-blur-2xl p-10 rounded-[2.5rem] shadow-[0_20px_50px_rgba(116,91,0,0.05)] border border-white">
        <h2 class="text-2xl font-bold mb-8 text-center text-[#745b00]">Selamat Datang Kembali!</h2>
        
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div class="space-y-2">
            <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-2">Email Address</label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-outline">mail</span>
              <input v-model="email" type="email" required class="w-full pl-12 pr-4 py-4 bg-surface-container-highest/50 border-none rounded-full text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" placeholder="budi@example.com">
            </div>
          </div>

          <div class="space-y-2">
            <div class="flex justify-between items-center ml-2">
              <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant">Password</label>
              <a href="#" class="text-xs font-bold text-primary hover:underline">Lupa password?</a>
            </div>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-outline">lock</span>
              <input v-model="password" type="password" required class="w-full pl-12 pr-12 py-4 bg-surface-container-highest/50 border-none rounded-full text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" placeholder="••••••••">
              <button type="button" class="absolute right-4 top-1/2 -translate-y-1/2 text-outline hover:text-primary transition-colors">
                <span class="material-symbols-outlined">visibility</span>
              </button>
            </div>
          </div>

          <button type="submit" :disabled="isLoading" class="w-full bg-[#f2c94c] text-[#745b00] py-4 rounded-full font-extrabold text-lg shadow-lg shadow-[#f2c94c]/30 hover:scale-[1.02] active:scale-95 transition-all cursor-pointer">
            {{ isLoading ? 'Loading...' : 'Masuk Sekarang' }}
          </button>
        </form>

        <div class="mt-8 text-center">
          <p class="text-sm font-medium text-on-surface-variant">Belum punya akun? <router-link to="/register" class="text-primary font-bold hover:underline">Daftar di sini</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>
