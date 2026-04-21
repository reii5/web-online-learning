import os
import re

design_dir = r"d:\WebProject\design\stitch_casual_learning_hub"
app_dir = r"d:\WebProject\app"

mappings = {
    "homepage/code.html": "index.html",
    "course_listing/code.html": "courses.html",
    "course_details/code.html": "course-detail.html",
    "instructor_profile_alex_rivera/code.html": "instructor.html",
    "lesson_view/code.html": "lesson.html",
    "mentor_chat/code.html": "chat.html",
    "user_profile_management/code.html": "profile.html"
}

for src_rel, dest_rel in mappings.items():
    src_path = os.path.join(design_dir, src_rel)
    dest_path = os.path.join(app_dir, dest_rel)
    
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        continue
        
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the Brand Logo text
    content = content.replace('Casual Edu-Platform', 'Sunbeam Learning')
    
    # 2. Top Navigation Links (Desktop)
    # The design has: <a class="..." href="#">Courses</a>
    content = re.sub(r'<a([^>]+)href="#"([^>]*)>Courses</a>', r'<a\1href="courses.html"\2>Kelas</a>', content)
    content = re.sub(r'<a([^>]+)href="#"([^>]*)>Mentors</a>', r'<a\1href="instructor.html"\2>Instruktur</a>', content)
    content = re.sub(r'<a([^>]+)href="#"([^>]*)>Pricing</a>', r'<a\1href="courses.html"\2>Harga</a>', content)
    
    # Mobile nav
    content = content.replace('>Home<', '>Beranda<')
    content = content.replace('>Search<', '>Cari<')
    content = content.replace('>Library<', '>Kelas<')
    content = content.replace('>Profile<', '>Profil<')
    
    # 3. Fix Sign In Button -> Link to Profile
    # It looks like: <button class="...">\n                    Sign In\n                </button>
    content = re.sub(r'<button([^>]+)Sign In\s*</button>', r'<a href="profile.html"\1>Masuk</a>', content, flags=re.IGNORECASE|re.DOTALL)
    
    # 4. Link some common "View All" or similar buttons if they have '#'
    content = content.replace('href="#"', 'href="javascript:void(0)"')
    
    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Copy and string replacement complete.")
