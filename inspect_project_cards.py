import re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
print(f"Total project cards on projects.html: {len(articles)}")

for i, a in enumerate(articles, 1):
    title = re.search(r'<h3>(.*?)</h3>', a)
    badge = re.search(r'class="project-tech-badge">(.*?)</span>', a)
    img = re.search(r'<img[^>]+src="([^"]+)"', a)
    t_str = title.group(1) if title else 'No title'
    b_str = badge.group(1) if badge else 'No badge'
    i_str = img.group(1) if img else 'No img'
    print(f"Card {i}: {t_str} | Badge: {b_str} | Current Img: {i_str}")
