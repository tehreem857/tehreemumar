import glob
import re

nav_root = '''<div class="nav-actions">
        <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle Dark/Light Mode" title="Toggle Dark/Light Mode">
          <svg class="sun-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m0 13.5V21M4.93 4.93l1.59 1.59m10.96 10.96l1.59 1.59m-17.5 0l1.59-1.59M17.47 6.52l1.59-1.59M5.25 12H3m18 0h-2.25m-2.25 0a6 6 0 11-12 0 6 6 0 0112 0z"></path>
          </svg>
          <svg class="moon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z"></path>
          </svg>
        </button>
        
        <a href="contact.html" class="btn btn-primary nav-cta-btn" style="padding: 10px 22px; font-size: 0.9rem; font-weight: 700; box-shadow: 0 4px 16px rgba(16, 185, 129, 0.35);">Book Consultation</a>
        
        <button class="mobile-menu-btn" id="mobile-menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
          <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>'''

nav_blog = nav_root.replace('href="contact.html"', 'href="../contact.html"')

pattern = re.compile(r'<div class="nav-actions">.*?</div>', re.DOTALL)

files = glob.glob('C:/Users/User/.gemini/antigravity/scratch/tehreem-portfolio/*.html') + glob.glob('C:/Users/User/.gemini/antigravity/scratch/tehreem-portfolio/blog/*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'blog' in f and ('blog/' in f or 'blog\\' in f):
        new_content = pattern.sub(nav_blog, content)
    else:
        new_content = pattern.sub(nav_root, content)
        
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated navbar in: {f}')

print("Done updating navbar across all pages.")
