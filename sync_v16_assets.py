import os, re

root_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]
blog_dir = 'blog'
blog_files = [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')] if os.path.exists(blog_dir) else []
all_htmls = root_files + blog_files

for filepath in all_htmls:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_blog = filepath.startswith('blog/')
    
    # Bump css/js cache busters to v=16.0
    if is_blog:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="../css/styles.css?v=16.0"', content)
        content = re.sub(r'src="[^"]*main\.js[^"]*"', 'src="../js/main.js?v=16.0"', content)
    else:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="css/styles.css?v=16.0"', content)
        content = re.sub(r'src="[^"]*main\.js[^"]*"', 'src="js/main.js?v=16.0"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated cache buster tags (v=16.0) across {len(all_htmls)} HTML files!")
