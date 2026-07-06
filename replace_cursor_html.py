import os
import glob

# Path to the portfolio directory
base_dir = r"C:\Users\User\.gemini\antigravity\scratch\tehreem-portfolio"

# Find all HTML files
html_files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "blog", "*.html"))

target_string = '<div class="cursor-glow" aria-hidden="true"></div>'
replacement_string = '<div class="cursor-dot"></div>\n  <div class="cursor-outline"></div>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_string in content:
        new_content = content.replace(target_string, replacement_string)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No match in {filepath}")
