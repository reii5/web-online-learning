<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../lib/supabaseClient.js'

const router = useRouter()
const fullname = ref('')
const email = ref('')
const password = ref('')
const isLoading = ref(false)

const handleRegister = async () => {
  isLoading.value = true
  const { data, error } = await supabase.auth.signUp({
    email: email.value,
    password: password.value,
    options: {
      data: {
        full_name: fullname.value
      }
    }
  })

  if (error) {
    alert('Gagal mendaftar: ' + error.message)
    isLoading.value = false
  } else {
    alert('Berhasil mendaftar! Silakan cek email untuk verifikasi (jika diaktifkan) atau langsung masuk.')
    router.push('/login')
  }
}
</script>

<template>
  <div class="bg-surface text-on-surface min-h-screen flex items-center justify-center relative overflow-hidden py-12 font-['Plus_Jakarta_Sans']">
    <!-- Background Decor -->
    <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-primary-container/20 rounded-full blur-3xl -z-10 translate-x-1/2 -translate-y-1/2"></div>
    <div class="absolute bottom-0 left-0 w-[40rem] h-[40rem] bg-tertiary-container/20 rounded-full blur-3xl -z-10 -translate-x-1/3 translate-y-1/3"></div>

    <div class="w-full max-w-5xl mx-auto p-6 flex flex-col md:flex-row-reverse items-center gap-12 z-10">
      <!-- Right Side: Hero Text -->
      <div class="flex-1 text-center md:text-left">
        <router-link to="/" class="inline-block text-3xl font-extrabold text-stone-900 hover:text-primary transition-colors cursor-pointer mb-8">Sunbeam Learning</router-link>
        <h1 class="text-4xl md:text-5xl font-black text-[#745b00] tracking-tight leading-tight mb-6">
          Langkah Awal <br/>
          Menuju Karir <br/>
          Impianmu.
        </h1>
        <p class="text-on-surface-variant text-lg font-medium">Buat akun secara gratis, coba beberapa materi, dan lihat apakah kami cocok untukmu.</p>
      </div>

      <!-- Left Side: Register Card -->
      <div class="w-full max-w-md bg-white/60 backdrop-blur-2xl p-10 rounded-[2.5rem] shadow-[0_20px_50px_rgba(116,91,0,0.05)] border border-white">
        <h2 class="text-2xl font-bold mb-8 text-center text-[#745b00]">Buat Akun Baru</h2>
        
        <form @submit.prevent="handleRegister" class="space-y-6">
          <div class="space-y-2">
            <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-2">Nama Lengkap</label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-outline">person</span>
              <input v-model="fullname" type="text" required class="w-full pl-12 pr-4 py-4 bg-surface-container-highest/50 border-none rounded-full text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" placeholder="Budi Santoso">
            </div>
          </div>

          <div class="space-y-2">
            <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-2">Email Address</label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-outline">mail</span>
              <input v-model="email" type="email" required class="w-full pl-12 pr-4 py-4 bg-surface-container-highest/50 border-none rounded-full text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" placeholder="budi@example.com">
            </div>
          </div>

          <div class="space-y-2">
            <label class="block text-xs font-bold uppercase tracking-widest text-on-surface-variant ml-2">Password</label>
            <div class="relative">
              <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-outline">lock</span>
              <input v-model="password" type="password" required class="w-full pl-12 pr-12 py-4 bg-surface-container-highest/50 border-none rounded-full text-on-surface focus:ring-2 focus:ring-primary/40 focus:bg-surface-container-low transition-all" placeholder="••••••••">
            </div>
          </div>

          <button type="submit" :disabled="isLoading" class="w-full bg-[#f2c94c] text-[#745b00] py-4 rounded-full font-extrabold text-lg shadow-lg shadow-[#f2c94c]/30 hover:scale-[1.02] active:scale-95 transition-all cursor-pointer mt-4">
            {{ isLoading ? 'Loading...' : 'Daftar Sekarang' }}
          </button>
        </form>

        <div class="mt-8 text-center">
          <p class="text-sm font-medium text-on-surface-variant">Sudah punya akun? <router-link to="/login" class="text-primary font-bold hover:underline">Masuk di sini</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>
