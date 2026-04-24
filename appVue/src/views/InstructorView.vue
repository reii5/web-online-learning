<script setup>
// Static layout for instructor profile view
</script>

<template>
  <div class="bg-background text-on-surface antialiased font-['Plus_Jakarta_Sans']">
    <!-- TopAppBar -->
    <header class="sticky top-0 w-full z-50 bg-[#fbf9f1]/80 backdrop-blur-xl border-none shadow-[0_20px_50px_rgba(27,28,23,0.05)]">
      <div class="flex justify-between items-center px-8 h-20 w-full max-w-screen-2xl mx-auto">
        <router-link to="/" class="text-xl font-extrabold text-stone-900 hover:text-primary transition-colors cursor-pointer">Sunbeam Learning</router-link>

        <div class="hidden md:flex items-center gap-8">
          <router-link to="/" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Beranda</router-link>
          <router-link to="/courses" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Kelas</router-link>
          <router-link to="/instructor" class="text-[#745b00] font-bold border-b-2 border-[#f2c94c] transition-colors">Instruktur</router-link>
          <router-link to="/chat" class="text-stone-600 font-medium hover:text-[#745b00] transition-colors">Mentor Chat</router-link>
        </div>

        <div class="flex items-center gap-6">
          <span class="material-symbols-outlined text-stone-600 cursor-pointer hover:text-primary transition-all">notifications</span>
          <router-link to="/login" class="bg-primary text-on-primary px-6 py-2.5 rounded-full font-bold hover:scale-95 duration-200 ease-out transition-transform inline-block">Masuk</router-link>
        </div>
      </div>
    </header>

    <main class="max-w-screen-2xl mx-auto px-6 md:px-12 py-8 space-y-24">
      <!-- Hero Section -->
      <section class="relative grid md:grid-cols-2 gap-12 items-center">
        <div class="order-2 md:order-1 space-y-6">
          <div class="inline-flex items-center px-4 py-1.5 rounded-full bg-secondary-container text-on-secondary-container font-medium text-sm">
            Verified Instructor
          </div>
          <h1 class="text-6xl md:text-8xl font-extrabold tracking-tight text-primary">Alex Rivera</h1>
          <p class="text-2xl md:text-3xl text-on-surface-variant font-medium">Senior Dev &amp; Casual Mentor</p>
          <p class="text-lg text-on-surface-variant leading-relaxed max-w-lg">
            Blending technical rigor with a playful approach. I help curious minds master the art of coding through tactile, project-based exploration.
          </p>
          <div class="flex gap-4 pt-4">
            <button class="px-8 py-4 bg-primary-container text-on-primary-container rounded-full font-bold shadow-lg hover:opacity-90 transition-opacity active:scale-95">Follow Alex</button>
            <router-link to="/chat" class="px-8 py-4 bg-surface-container-high text-on-surface rounded-full font-bold hover:bg-surface-container-highest transition-colors">Message</router-link>
          </div>
        </div>
        <div class="order-1 md:order-2 relative aspect-square">
          <div class="absolute inset-0 bg-primary-container/20 rounded-xl -rotate-6 scale-95"></div>
          <div class="absolute inset-0 bg-secondary-container/20 rounded-xl rotate-3 scale-95"></div>
          <img class="relative z-10 w-full h-full object-cover rounded-xl shadow-2xl" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDdjiP_NDUKNFyvPW7nLKE2zgJCdIIPqx-nmGI09ECwQJ-BmDjg6F2QCesA9XvqEmffTz89lfNJG7J_EaVx2XCTGcSmptXjofQsZRzr5YAsQNbOrwLagxvJxICBvZZcB7JLYx9a0u69gdXjbYVhy3bIAM3VWBso4T45zLRDK7C0z9KlayLkfXYM7lKyOmsIJBfOaUREW7HaU2XAt0YGFiNM3gaGEkA5NMo0Rbj8eiTGWuA0PwDrHirZJn3ngD3_JF60g48wqEdVfg8"/>
        </div>
      </section>

      <!-- Stats Section -->
      <section class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-surface-container-lowest p-8 rounded-lg shadow-sm flex items-center space-x-6 border-b-4 border-primary-container">
          <div class="w-16 h-16 rounded-2xl bg-primary-container/30 flex items-center justify-center">
            <span class="material-symbols-outlined text-primary text-3xl">groups</span>
          </div>
          <div>
            <h3 class="text-3xl font-extrabold text-on-surface">2.4k+</h3>
            <p class="text-on-surface-variant uppercase tracking-widest text-xs font-bold">Students Taught</p>
          </div>
        </div>
        <div class="bg-surface-container-lowest p-8 rounded-lg shadow-sm flex items-center space-x-6 border-b-4 border-secondary-container">
          <div class="w-16 h-16 rounded-2xl bg-secondary-container/30 flex items-center justify-center">
            <span class="material-symbols-outlined text-secondary text-3xl">star</span>
          </div>
          <div>
            <h3 class="text-3xl font-extrabold text-on-surface">4.9/5</h3>
            <p class="text-on-surface-variant uppercase tracking-widest text-xs font-bold">Average Rating</p>
          </div>
        </div>
        <div class="bg-surface-container-lowest p-8 rounded-lg shadow-sm flex items-center space-x-6 border-b-4 border-tertiary-container">
          <div class="w-16 h-16 rounded-2xl bg-tertiary-container/30 flex items-center justify-center">
            <span class="material-symbols-outlined text-tertiary text-3xl">school</span>
          </div>
          <div>
            <h3 class="text-3xl font-extrabold text-on-surface">12+</h3>
            <p class="text-on-surface-variant uppercase tracking-widest text-xs font-bold">Expert Courses</p>
          </div>
        </div>
      </section>

      <!-- Biography Section -->
      <section class="bg-surface-container-low rounded-xl p-12 md:p-20 grid md:grid-cols-5 gap-12">
        <div class="md:col-span-2">
          <h2 class="text-4xl font-extrabold text-primary mb-6">About the Mentor</h2>
          <div class="w-24 h-2 bg-primary-container rounded-full"></div>
        </div>
        <div class="md:col-span-3 space-y-6">
          <p class="text-xl text-on-surface-variant font-medium italic leading-relaxed">
            "I believe learning should feel like play. When we treat code as a toy instead of a tool, the fear of breaking things vanishes, and that's when real creativity begins."
          </p>
          <p class="text-lg text-on-surface-variant leading-relaxed">
            Alex has spent over 15 years in the tech industry, leading engineering teams at top Silicon Valley firms. However, his true passion lies in demystifying complex logic for creative minds. 
          </p>
          <p class="text-lg text-on-surface-variant leading-relaxed">
            His **Tactile Learning Methodology** focuses on immediate application—building real-world projects that you can touch, see, and interact with from the very first lesson. No boring theory without a purpose.
          </p>
        </div>
      </section>

      <!-- Footer -->
      <footer class="bg-surface-container-low mt-24 pt-20 pb-12 rounded-t-[3rem]">
        <div class="max-w-screen-2xl mx-auto px-8 grid grid-cols-1 md:grid-cols-4 gap-12">
          <div class="col-span-1 md:col-span-1 space-y-6">
            <div class="text-2xl font-extrabold text-primary tracking-tight">Sunbeam Learning</div>
            <p class="text-on-surface-variant">Making high-end education accessible, tactile, and fun for the next generation of creators.</p>
          </div>
          <div>
            <h4 class="font-bold text-on-surface mb-6">Explore</h4>
            <ul class="space-y-4 text-on-surface-variant">
              <li><router-link class="hover:text-primary transition-colors" to="/courses">Course Catalog</router-link></li>
              <li><a class="hover:text-primary transition-colors" href="#">Mentorship Program</a></li>
            </ul>
          </div>
        </div>
      </footer>
    </main>
  </div>
</template>
