import { supabase } from './supabase.js';

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const { data: { user } } = await supabase.auth.getUser();

        if (user) {
            // Fetch profile to get name/avatar
            const { data: profile } = await supabase
                .from('profiles')
                .select('full_name, avatar_url')
                .eq('id', user.id)
                .single();

            // Find all login buttons on the page to replace them
            const loginBtns = document.querySelectorAll('button[onclick*="login.html"]');
            
            loginBtns.forEach(btn => {
                // Replace login button with a profile avatar link
                const profileLink = document.createElement('a');
                profileLink.href = 'profile.html';
                profileLink.className = 'w-10 h-10 rounded-full overflow-hidden border-2 border-primary-container flex items-center justify-center bg-surface-container hover:scale-105 transition-transform shadow-md';
                profileLink.title = profile?.full_name || 'My Profile';
                
                if (profile && profile.avatar_url) {
                    const img = document.createElement('img');
                    img.src = profile.avatar_url;
                    img.className = 'w-full h-full object-cover';
                    img.alt = 'User Avatar';
                    profileLink.appendChild(img);
                } else {
                    const icon = document.createElement('span');
                    icon.className = 'material-symbols-outlined text-primary text-xl';
                    icon.innerText = 'person';
                    profileLink.appendChild(icon);
                }

                btn.replaceWith(profileLink);
            });
        }
    } catch (e) {
        console.error('Auth state error:', e);
    }
});
