import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]

print("--- AUDITING ALL PAGES AND LINKS ---")

nav_standard = """      <nav class="nav-links" id="nav-links" aria-label="Main Navigation">
        <a href="about.html" class="nav-link">About</a>
        <a href="services.html" class="nav-link">Services</a>
        <a href="projects.html" class="nav-link">Projects</a>
        <a href="skills.html" class="nav-link">Skills</a>
        <a href="process.html" class="nav-link">Process</a>
        <a href="reviews.html" class="nav-link">Reviews</a>
        <a href="blogs.html" class="nav-link">Blog</a>
        <a href="contact.html" class="nav-link">Contact</a>
      </nav>"""

for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check body data-theme
    if 'data-theme="dark"' in content:
        print(f"[{fname}] Updating data-theme to light")
        content = content.replace('data-theme="dark"', 'data-theme="light"')

    # Check navbar links consistency
    if '<nav class="nav-links"' in content:
        # replace nav block
        content = re.sub(r'<nav class="nav-links"[^>]*>.*?</nav>', nav_standard, content, flags=re.DOTALL)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbar links & data-theme light synced across all pages!")
