import glob
import re

for f in sorted(glob.glob('**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for idx, line in enumerate(lines, 1):
        if 'index.html' in line:
            print(f"{f}:{idx}: {line.strip()}")
