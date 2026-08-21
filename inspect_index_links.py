import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
print("ALL LINKS ON index.html:")
for href, inner in matches:
    clean_text = re.sub(r'<[^>]+>', '', inner).strip().encode('ascii', 'ignore').decode('ascii')
    clean_text = ' '.join(clean_text.split())
    print(f"  href: {href:40s} | text: {clean_text}")
