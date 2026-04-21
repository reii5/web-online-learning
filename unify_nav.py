import os
import glob
import re

app_dir = r"d:\WebProject\app"
html_files = glob.glob(os.path.join(app_dir, "*.html"))

# We will define the standard Top Nav and standard Bottom Nav HTML blocks
# Based on index.html's design

TOP_NAV = """
<div class="hidden md:flex items-center gap-8">
<a class="text-[#745b00] font-bold hover:border-b-2 hover:border-[#f2c94c] transition-colors" href="courses.html">Kelas</a>
<a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="instructor.html">Instruktur</a>
<a class="text-stone-600 font-medium hover:text-[#745b00] transition-colors" href="chat.html">Mentor Chat</a>
</div>
"""

BOTTOM_NAV = """
<!-- BottomNavBar (Mobile Only) -->
<div class="md:hidden fixed bottom-0 left-0 w-full rounded-t-xl z-50 bg-[#fbf9f1]/90 backdrop-blur-lg shadow-[0_-10px_40px_rgba(0,0,0,0.05)]">
<div class="flex justify-around items-center h-20 px-6 pb-2">
<a href="index.html" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00] tap-highlight-none">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">home</span>
<span class="text-[10px] uppercase tracking-widest font-bold">Beranda</span>
</a>
<a href="courses.html" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00] tap-highlight-none">
<span class="material-symbols-outlined">search</span>
<span class="text-[10px] uppercase tracking-widest font-bold">Cari</span>
</a>
<a href="courses.html" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00] tap-highlight-none">
<span class="material-symbols-outlined">local_library</span>
<span class="text-[10px] uppercase tracking-widest font-bold">Kelas</span>
</a>
<a href="profile.html" class="flex flex-col items-center justify-center text-stone-400 hover:text-[#745b00] tap-highlight-none">
<span class="material-symbols-outlined">account_circle</span>
<span class="text-[10px] uppercase tracking-widest font-bold">Profil</span>
</a>
</div>
</div>
"""

# Let's replace the nav sections in all files
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Top Nav (Desktop)
    # The top nav usually has <nav class="hidden md:flex... or <div class="hidden md:flex items-center gap-8">
    # Profile uses <nav class="hidden md:flex items-center gap-8">
    content = re.sub(r'<nav class="hidden md:flex items-center gap-8">[\s\S]*?</nav>', TOP_NAV.replace('<div', '<nav').replace('</div>', '</nav>'), content)
    content = re.sub(r'<div class="hidden md:flex items-center gap-8">[\s\S]*?</div>', TOP_NAV, content)

    # 2. Replace Bottom Nav (Mobile)
    # They usually start with <!-- BottomNavBar... and end before </body>
    content = re.sub(r'<!-- BottomNavBar.*?-->[\s\S]*?(?=</body>)', BOTTOM_NAV + '\n', content)
    # For profile.html, it might just be <nav class="fixed bottom-0...
    content = re.sub(r'<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-2 bg-stone-50/80 dark:bg-stone-900/80 backdrop-blur-2xl rounded-t-\[3rem\] shadow-\[0_-10px_40px_rgba\(0,0,0,0.05\)\] md:hidden">[\s\S]*?</nav>', BOTTOM_NAV, content)
    # Courses.html bottom nav
    content = re.sub(r'<div class="fixed bottom-0 left-0 w-full rounded-t-\[3rem\].*?>[\s\S]*?</nav>\n</div>', BOTTOM_NAV, content)
    
    # 3. Add link to main.css in head if not exists
    if 'styles/main.css' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="styles/main.css">\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbars unified.")
