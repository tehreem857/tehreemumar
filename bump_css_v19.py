import re, glob

html_files = [f for f in glob.glob('**/*.html', recursive=True) if 'google' not in f]
for filepath in html_files:
    content = open(filepath, 'r', encoding='utf-8').read()
    is_blog = filepath.startswith('blog/')
    if is_blog:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="../css/styles.css?v=19.0"', content)
    else:
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="css/styles.css?v=19.0"', content)
    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Updated {filepath}")

print('Done - CSS cache buster v=19.0!')
