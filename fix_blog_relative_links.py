import glob

blog_files = glob.glob('blog/*.html')

for filepath in blog_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace broken relative blog links:
    # href="blog/xxx.html" inside a file that is already at /blog/xxx.html resolves to /blog/blog/xxx.html (404!)
    # Change to root-relative href="/blog/xxx.html"
    updated = content.replace('href="blog/', 'href="/blog/')
    updated = updated.replace("href='blog/", "href='/blog/")
    
    if updated != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Fixed blog links in: {filepath}")

print("All blog link fixes applied successfully!")
