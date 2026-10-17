import glob
import re

print("=== CHECKING CANONICAL TAGS AND INDEX.HTML LINKS ===")
for f in sorted(glob.glob('**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    canonical = re.findall(r'<link\s+rel=["\']canonical["\'][^>]*>', content)
    index_links = re.findall(r'href=["\']([^"\']*index\.html[^"\']*)["\']', content)
    print(f"{f}:")
    print(f"  Canonical: {canonical}")
    print(f"  index.html links ({len(index_links)}): {index_links[:3]}")

print("\n=== CHECKING SITEMAP.XML ===")
with open('sitemap.xml', 'r', encoding='utf-8') as file:
    print(file.read())

print("\n=== CHECKING ROBOTS.TXT ===")
with open('robots.txt', 'r', encoding='utf-8') as file:
    print(file.read())
