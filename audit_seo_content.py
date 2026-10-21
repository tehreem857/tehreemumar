import glob
import re

print("=== AUDITING TITLES, DESCRIPTIONS, H1s, & KEYWORDS ===")
for f in sorted(glob.glob('*.html')) + sorted(glob.glob('blog/*.html')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_m.group(1).strip() if title_m else 'MISSING'
    
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    desc = desc_m.group(1).strip() if desc_m else 'MISSING'
    
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    h1 = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else 'MISSING'
    
    print(f"\n--- {f} ---")
    print(f"Title: {title}")
    print(f"Desc : {desc}")
    print(f"H1   : {h1}")
