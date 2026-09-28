import os, glob, re

new_pixel_tag = """  <!-- Closebot -->
  <script src="https://api.closebot.com/scripts/cb.js?source=1FbJSO4BUGj8QTeQ" async></script>
"""

# Find all HTML files recursively (excluding scratch or system dirs if any)
html_files = glob.glob('**/*.html', recursive=True)

updated_count = 0
for filepath in html_files:
    if 'google' in filepath or '.system_generated' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if closebot script tag exists
    if 'api.closebot.com/scripts/cb.js' in content:
        # Replace existing closebot script tag / source with new source=1FbJSO4BUGj8QTeQ
        new_content = re.sub(
            r'<!--\s*Closebot\s*-->\s*<script\s+src="https://api\.closebot\.com/scripts/cb\.js\?source=[^"]*"\s*async></script>',
            new_pixel_tag.strip(),
            content,
            flags=re.IGNORECASE
        )
        # Also handle standalone cb.js tag if comments differ
        new_content = re.sub(
            r'<script\s+src="https://api\.closebot\.com/scripts/cb\.js\?source=[^"]*"\s*async></script>',
            '<script src="https://api.closebot.com/scripts/cb.js?source=1FbJSO4BUGj8QTeQ" async></script>',
            new_content,
            flags=re.IGNORECASE
        )
    else:
        # Insert before </head>
        new_content = content.replace("</head>", new_pixel_tag + "</head>")

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated Closebot pixel in {filepath}")
        updated_count += 1
    else:
        print(f"No changes needed for {filepath}")

print(f"\nFinished updating Closebot pixel on {updated_count} HTML files!")
