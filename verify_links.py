import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]

all_issues = []

for fname in sorted(html_files):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n==========================================")
    print(f"FILE: {fname}")
    print(f"==========================================")
    
    # Extract links
    matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
    for href, inner in matches:
        clean_text = re.sub(r'<[^>]+>', '', inner).strip()
        clean_text = ' '.join(clean_text.split())
        if not clean_text:
            clean_text = "[Icon/Image Link]"
        print(f"  Target: {href:30s} | Label: {clean_text}")

        # Check for obvious misdirections
        # 1. 'View My Work' should go to projects.html
        if 'View My Work' in clean_text and href != 'projects.html':
            all_issues.append((fname, clean_text, href, 'projects.html'))
        # 2. 'Book Consultation' / 'Book a Consultation' should go to contact.html
        if ('Book Consultation' in clean_text or 'Book a Consultation' in clean_text) and href != 'contact.html':
            all_issues.append((fname, clean_text, href, 'contact.html'))
        # 3. 'About' nav/button should go to about.html
        if clean_text == 'About' and href != 'about.html':
            all_issues.append((fname, clean_text, href, 'about.html'))
        # 4. 'Services' nav/button should go to services.html
        if clean_text == 'Services' and href != 'services.html':
            all_issues.append((fname, clean_text, href, 'services.html'))
        # 5. 'Projects' nav/button should go to projects.html
        if clean_text == 'Projects' and href != 'projects.html':
            all_issues.append((fname, clean_text, href, 'projects.html'))
        # 6. 'Skills' nav/button should go to skills.html
        if clean_text == 'Skills' and href != 'skills.html':
            all_issues.append((fname, clean_text, href, 'skills.html'))
        # 7. 'Process' nav/button should go to process.html
        if clean_text == 'Process' and href != 'process.html':
            all_issues.append((fname, clean_text, href, 'process.html'))
        # 8. 'Reviews' nav/button should go to reviews.html
        if clean_text == 'Reviews' and href != 'reviews.html':
            all_issues.append((fname, clean_text, href, 'reviews.html'))
        # 9. 'Blog' / 'Blogs' nav/button should go to blogs.html
        if clean_text in ['Blog', 'Blogs'] and href != 'blogs.html':
            all_issues.append((fname, clean_text, href, 'blogs.html'))
        # 10. 'Contact' nav/button should go to contact.html
        if clean_text == 'Contact' and href != 'contact.html':
            all_issues.append((fname, clean_text, href, 'contact.html'))

print("\n\n------------------------------------------")
print("SUMMARY OF LINK MISMATCH ISSUES FOUND:")
print("------------------------------------------")
if not all_issues:
    print("No mismatches found!")
else:
    for fname, label, actual, expected in all_issues:
        print(f"File: {fname} | Label: '{label}' | Actual href: '{actual}' -> Expected: '{expected}'")
