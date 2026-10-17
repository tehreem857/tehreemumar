import glob
import re

print("=== CHECKING BLOG LINKS ===")
for f in sorted(glob.glob('blog/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    bad_links = re.findall(r'href=["\']blog/[^"\']+["\']', content)
    print(f"{f}: {bad_links}")
