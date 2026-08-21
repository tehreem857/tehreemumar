import os, re

root_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]
blog_dir = 'blog'
blog_files = [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')] if os.path.exists(blog_dir) else []

all_files = root_files + blog_files

print(f"Syncing script/CSS versions and nav links across {len(all_files)} files...")

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    is_blog = filepath.startswith('blog/')

    # Sync styles.css version
    if is_blog:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="../css/styles.css?v=12.0"', content)
        content = re.sub(r'src="[^"]*main\.js[^"]*"', 'src="../js/main.js?v=12.0"', content)
    else:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="css/styles.css?v=12.0"', content)
        content = re.sub(r'src="[^"]*main\.js[^"]*"', 'src="js/main.js?v=12.0"', content)

    # Ensure body data-theme="light"
    if 'data-theme=' in content:
        content = re.sub(r'data-theme="[^"]*"', 'data-theme="light"', content)

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [UPDATED] {filepath}")
    else:
        print(f"  [OK] {filepath}")

print("Done syncing asset versions!")
