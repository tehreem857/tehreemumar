import re

with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
print("ALL LINKS ON projects.html:")
for href, inner in matches:
    clean_text = re.sub(r'<[^>]+>', '', inner).strip()
    clean_text = ' '.join(clean_text.split())
    if not clean_text:
        clean_text = "[Logo/Icon/Image]"
    print(f"  href: {href:35s} | text: {clean_text}")
