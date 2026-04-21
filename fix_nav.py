import os
import glob
import re

app_dir = r"d:\WebProject\app"
html_files = glob.glob(os.path.join(app_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure main.css is linked so any custom styles are preserved
    if 'styles/main.css' not in content:
        content = content.replace('</head>', '    <link rel="stylesheet" href="styles/main.css">\n</head>')

    # 2. Fix Top Navigation Links
    # Convert "Harga" back to "Mentor Chat" and link to chat.html
    content = re.sub(r'<a([^>]+href=")[^"]*("[^>]*>)\s*Harga\s*</a>', r'<a\g<1>chat.html\g<2>Mentor Chat</a>', content)
    
    # 3. Fix Bottom Navigation (Mobile)
    # Convert div to a if it's a div
    content = re.sub(r'<div([^>]+tap-highlight-none[^>]*)>([\s\S]*?)</div>', r'<a href="#"\1>\2</a>', content)
    
    # Update hrefs for bottom nav
    content = re.sub(r'<a([^>]+)href="[^"]*"([^>]*>)([\s\S]*?)>Beranda</span>\s*</a>', r'<a\1href="index.html"\2\3>Beranda</span></a>', content)
    
    # "Cari" or "Explore"
    content = re.sub(r'<a([^>]+)href="[^"]*"([^>]*>)([\s\S]*?)>(Cari|Explore)</span>\s*</a>', r'<a\1href="courses.html"\2\3>\4</span></a>', content)
    
    # "Kelas" or "Library"
    content = re.sub(r'<a([^>]+)href="[^"]*"([^>]*>)([\s\S]*?)>(Kelas|Library)</span>\s*</a>', r'<a\1href="courses.html"\2\3>\4</span></a>', content)
    
    # "Profil" or "Profile"
    content = re.sub(r'<a([^>]+)href="[^"]*"([^>]*>)([\s\S]*?)>(Profil|Profile)</span>\s*</a>', r'<a\1href="profile.html"\2\3>\4</span></a>', content)

    # 4. Fix Sidebar Navigation (if any)
    content = re.sub(r'<a([^>]+href=")[^"]*("[^>]*>\s*<span[^>]*>grid_view</span>\s*<span[^>]*>)\s*Semua Kursus\s*</span>\s*</a>', r'<a\g<1>courses.html\g<2>Semua Kursus</span></a>', content)
    
    # 5. Make sure the generic "href='#'" or "javascript:void(0)" in top nav for Kelas/Instruktur is fixed just in case
    content = re.sub(r'<a([^>]+)href="(?:#|javascript:void\(0\))"([^>]*>)\s*Kelas\s*</a>', r'<a\1href="courses.html"\2Kelas</a>', content)
    content = re.sub(r'<a([^>]+)href="(?:#|javascript:void\(0\))"([^>]*>)\s*Instruktur\s*</a>', r'<a\1href="instructor.html"\2Instruktur</a>', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation links updated in all HTML files.")
