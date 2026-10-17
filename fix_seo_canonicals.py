import re
import glob

# 1. Update internal links in root HTML files: replace href="index.html" with href="/"
# Also replace any href="./index.html" with href="/"
root_htmls = [
    'about.html', 'blogs.html', 'contact.html', 'index.html',
    'process.html', 'projects.html', 'reviews.html', 'services.html', 'skills.html'
]

for filename in root_htmls:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href="index.html" with href="/"
    updated = re.sub(r'href=["\']index\.html["\']', 'href="/"', content)
    updated = re.sub(r'href=["\']\./index\.html["\']', 'href="/"', updated)
    
    if updated != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated internal home links in {filename}")

# 2. Fix Canonical Tags across the sub-pages
canonical_fixes = {
    'blogs.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/blogs.html'),
    'contact.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/contact.html'),
    'process.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/process.html'),
    'projects.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/projects.html'),
    'reviews.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/reviews.html'),
    'skills.html': ('https://tehreemumar.com/', 'https://tehreemumar.com/skills.html'),
}

for filename, (old_canon, new_canon) in canonical_fixes.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the canonical tag specifically
    target = f'<link rel="canonical" href="{old_canon}">'
    replacement = f'<link rel="canonical" href="{new_canon}">'
    if target in content:
        updated = content.replace(target, replacement)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Fixed canonical in {filename} -> {new_canon}")
    else:
        print(f"Target canonical not found in {filename}!")

# Also fix og:url in these files to match the page url
og_fixes = {
    'about.html': 'https://tehreemumar.com/about.html',
    'blogs.html': 'https://tehreemumar.com/blogs.html',
    'contact.html': 'https://tehreemumar.com/contact.html',
    'process.html': 'https://tehreemumar.com/process.html',
    'projects.html': 'https://tehreemumar.com/projects.html',
    'reviews.html': 'https://tehreemumar.com/reviews.html',
    'services.html': 'https://tehreemumar.com/services.html',
    'skills.html': 'https://tehreemumar.com/skills.html',
}

for filename, page_url in og_fixes.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Update og:url if it's pointing to root
    updated = re.sub(
        r'<meta property="og:url" content="https://tehreemumar\.com/?"',
        f'<meta property="og:url" content="{page_url}"',
        content
    )
    if updated != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated og:url in {filename} -> {page_url}")

# 3. Add noindex to cursor-demo.html
with open('cursor-demo.html', 'r', encoding='utf-8') as f:
    cursor_content = f.read()
if 'noindex' not in cursor_content:
    cursor_content = cursor_content.replace(
        '<meta charset="UTF-8">',
        '<meta charset="UTF-8">\n<meta name="robots" content="noindex, nofollow">'
    )
    with open('cursor-demo.html', 'w', encoding='utf-8') as f:
        f.write(cursor_content)
    print("Added noindex to cursor-demo.html")

print("\nAll canonical & link fixes applied successfully!")
