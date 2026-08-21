import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]

for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    hash_matches = re.findall(r'<a\s+[^>]*href=["\']#["\'][^>]*>(.*?)</a>', content, re.DOTALL)
    if hash_matches:
        print(f"File {fname} HAS href='#' links:")
        for inner in hash_matches:
            clean_text = re.sub(r'<[^>]+>', '', inner).strip().encode('ascii', 'ignore').decode('ascii')
            print(f"   text: '{clean_text}'")
