<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  router.back()
}
</script>

<template>
  <div class="bg-surface text-on-surface selection:bg-primary-container selection:text-on-primary-container min-h-screen flex flex-col font-['Plus_Jakarta_Sans']">
    <!-- TopAppBar -->
    <header class="bg-[#fbf9f1]/80 backdrop-blur-lg shadow-[0_20px_50px_rgba(27,28,23,0.05)] sticky top-0 z-50">
      <div class="flex justify-between items-center w-full px-6 py-4 max-w-screen-xl mx-auto">
        <div class="flex items-center gap-4">
          <button @click="goBack" class="hover:bg-[#f2c94c]/10 rounded-full transition-colors p-2 flex items-center justify-center active:scale-95 duration-200 cursor-pointer">
            <span class="material-symbols-outlined text-[#745b00]">arrow_back</span>
          </button>
          <div class="flex items-center gap-3">
            <div class="relative">
              <img class="w-10 h-10 rounded-full object-cover border-2 border-primary-container" src="https://lh3.googleusercontent.com/aida-public/AB6AXuChp1RNZ3q_IBVfa9g1IOWBFCa4TR0rRQBSbjLicHv-4Sye8YbKDzf-tx22794YqyzuJjirwotgtzBEDo-CrV61t1mXOig4S_A_wW_6v1QvBZjFGuaJ4N7-wcEARgpkBHCI8KLTsf1Ts9VQacCjAQG1DZK4e84IgdyoHo7DGdpA-zMqNqYjCLXMFTOz5sBo7jdDqXhB73z46cU0RPmJEWGyX-xEmEmg7l9SfJ9QcLRdA4TMysaSUf6B4INXiF8OOd1ZtYdPpWaO6qo"/>
              <span class="absolute bottom-0 right-0 w-3 h-3 bg-[#9ecfd1] border-2 border-surface rounded-full"></span>
            </div>
            <div>
              <h1 class="font-bold tracking-tight text-[#745b00] text-lg">Alex Rivera</h1>
              <p class="text-[10px] font-bold uppercase tracking-widest text-[#356668]">Active Now</p>
            </div>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <button class="hover:bg-[#f2c94c]/10 rounded-full transition-colors p-2 flex items-center justify-center active:scale-95 duration-200">
            <span class="material-symbols-outlined text-[#745b00]">call</span>
          </button>
          <button class="hover:bg-[#f2c94c]/10 rounded-full transition-colors p-2 flex items-center justify-center active:scale-95 duration-200">
            <span class="material-symbols-outlined text-[#745b00]">videocam</span>
          </button>
          <button class="hover:bg-[#f2c94c]/10 rounded-full transition-colors p-2 flex items-center justify-center active:scale-95 duration-200">
            <span class="material-symbols-outlined text-[#745b00]">info</span>
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content Canvas -->
    <main class="flex-1 max-w-5xl w-full mx-auto p-6 md:p-8 flex flex-col gap-8">
      <!-- Chat Log Area -->
      <div class="flex-1 bg-surface-container-low rounded-xl p-6 md:p-10 overflow-y-auto space-y-8 min-h-[614px]">
        <!-- System Timestamp -->
        <div class="flex justify-center">
          <span class="bg-surface-container-high px-4 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest text-on-surface-variant">Today, Oct 24</span>
        </div>
        
        <!-- Mentor Message -->
        <div class="flex flex-col items-start gap-2 max-w-[80%]">
          <div class="bg-surface-container-lowest text-on-surface p-5 rounded-lg rounded-tl-none shadow-sm text-[15px] leading-relaxed">
            Hi there! I've just reviewed your latest project proposal on the Sustainable Urban Design challenge. Your approach to the vertical garden integration is quite innovative.
          </div>
          <span class="text-[10px] font-bold uppercase tracking-widest text-outline px-2">10:15 AM</span>
        </div>
        
        <!-- User Message -->
        <div class="flex flex-col items-end gap-2 ml-auto max-w-[80%]">
          <div class="bg-primary-container text-on-primary-container p-5 rounded-lg rounded-tr-none shadow-sm text-[15px] leading-relaxed">
            Thanks, Alex! I was worried it might be too ambitious for the current budget constraints. Do you think we should scale back the irrigation system?
          </div>
          <span class="text-[10px] font-bold uppercase tracking-widest text-outline px-2">10:18 AM</span>
        </div>
        
        <!-- Mentor Message -->
        <div class="flex flex-col items-start gap-2 max-w-[80%]">
          <div class="bg-surface-container-lowest text-on-surface p-5 rounded-lg rounded-tl-none shadow-sm text-[15px] leading-relaxed">
            Not necessarily. We could look at passive rainwater harvesting instead of a motorized system. It aligns better with the sustainability goals anyway. Would you like to see some diagrams of how that might work?
          </div>
          <span class="text-[10px] font-bold uppercase tracking-widest text-outline px-2">10:20 AM</span>
        </div>
        
        <!-- Shared Resource Card -->
        <div class="flex flex-col items-start gap-2 max-w-[80%]">
          <div class="bg-white p-4 rounded-lg shadow-sm border border-outline-variant/10 flex items-center gap-4 hover:bg-surface-bright transition-colors cursor-pointer group">
            <div class="w-12 h-12 bg-secondary-container rounded-lg flex items-center justify-center text-on-secondary-container">
              <span class="material-symbols-outlined">description</span>
            </div>
            <div class="flex-1">
              <p class="font-bold text-sm text-on-surface">Rainwater_Harvesting_Guide.pdf</p>
              <p class="text-xs text-on-surface-variant">2.4 MB • Shared by Alex</p>
            </div>
            <span class="material-symbols-outlined text-outline group-hover:text-primary transition-colors">download</span>
          </div>
          <span class="text-[10px] font-bold uppercase tracking-widest text-outline px-2">10:21 AM</span>
        </div>
        
        <!-- User Message -->
        <div class="flex flex-col items-end gap-2 ml-auto max-w-[80%]">
          <div class="bg-primary-container text-on-primary-container p-5 rounded-lg rounded-tr-none shadow-sm text-[15px] leading-relaxed">
            That would be incredibly helpful. Let me take a look at the guide and I'll get back to you with a revised sketch.
          </div>
          <span class="text-[10px] font-bold uppercase tracking-widest text-outline px-2">10:22 AM</span>
        </div>
      </div>
      
      <!-- Input Section -->
      <div class="flex items-center gap-4 bg-surface-container-lowest p-3 rounded-full shadow-[0_10px_40px_rgba(27,28,23,0.04)] mb-20 md:mb-8">
        <button class="w-12 h-12 flex items-center justify-center text-primary hover:bg-primary-container/20 rounded-full transition-all active:scale-90">
          <span class="material-symbols-outlined">add</span>
        </button>
        <div class="flex-1 px-4">
          <input class="w-full bg-transparent border-none focus:outline-none focus:ring-0 text-on-surface placeholder:text-outline py-2" placeholder="Message Alex Rivera..." type="text"/>
        </div>
        <button class="w-12 h-12 bg-primary-container text-on-primary-container flex items-center justify-center rounded-full shadow-lg shadow-primary-container/30 hover:scale-105 active:scale-95 transition-all">
          <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">send</span>
        </button>
      </div>
    </main>
  </div>
</template>
