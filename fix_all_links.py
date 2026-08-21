import os, re

# Fix root HTML files
root_htmls = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]

# Fix blog HTML files
blog_dir = 'blog'
blog_htmls = [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')] if os.path.exists(blog_dir) else []

all_files = root_htmls + blog_htmls

print(f"Auditing {len(all_files)} total HTML files...")

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    is_blog_subpage = filepath.startswith('blog/')
    
    # 1. Fix leading slashes in blog links: /blog/xxx.html -> blog/xxx.html (or ../blog/xxx.html if subpage)
    if is_blog_subpage:
        content = re.sub(r'href="/blog/([^"]+)"', r'href="\1"', content)
        content = re.sub(r'href="index.html#([^"]+)"', r'href="../index.html#\1"', content)
    else:
        content = re.sub(r'href="/blog/([^"]+)"', r'href="blog/\1"', content)
    
    # 2. Fix footer links pointing to old anchor tags index.html#about etc. on subpages
    content = content.replace('href="index.html#about"', 'href="about.html"')
    content = content.replace('href="index.html#services"', 'href="services.html"')
    content = content.replace('href="index.html#projects"', 'href="projects.html"')
    content = content.replace('href="index.html#skills"', 'href="skills.html"')
    content = content.replace('href="index.html#process"', 'href="process.html"')
    content = content.replace('href="index.html#testimonials"', 'href="reviews.html"')
    content = content.replace('href="index.html#contact"', 'href="contact.html"')

    # 3. Ensure plain white background data-theme="light"
    if 'data-theme="dark"' in content:
        content = content.replace('data-theme="dark"', 'data-theme="light"')
        
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[FIXED] {filepath}")
    else:
        print(f"[OK] {filepath}")

print("All links, background theme & path references audited and updated!")
