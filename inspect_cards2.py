import re

with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

cards = re.findall(r'<article[^>]*>.*?</article>', content, re.DOTALL)

for i, c in enumerate(cards, 1):
    title = re.search(r'<h3>(.*?)</h3>', c)
    t_text = title.group(1) if title else "No Title"
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', c, re.DOTALL)
    print(f"Card {i}: {t_text}")
    for href, inner in links:
        clean_text = re.sub(r'<[^>]+>', '', inner).strip().encode('ascii', 'ignore').decode('ascii')
        print(f"   Link href: {href:40s} | text: {clean_text}")
