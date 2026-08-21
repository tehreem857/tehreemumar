import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]

for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
    print(f"\n=== FILE: {fname} ===")
    for href, inner in matches:
        clean_text = re.sub(r'<[^>]+>', '', inner).strip().encode('ascii', 'ignore').decode('ascii')
        clean_text = ' '.join(clean_text.split())
        if 'index.html' in href or href == '#' or href.startswith('#'):
            print(f"  [INDEX/HASH LINK] href: {href:30s} | text: {clean_text}")
