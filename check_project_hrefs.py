import os, re

for f in sorted(os.listdir('.')):
    if f.endswith('.html') and not f.startswith('google'):
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
        matches = re.findall(r'href=["\'][^"\']*projects[^"\']*["\']', c)
        print(f"{f:20s}: {matches}")
