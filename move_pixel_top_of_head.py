import os, glob, re

pixel_block = """  <!-- Closebot Sales Intelligence Pixel -->
  <script src="https://api.closebot.com/scripts/cb.js?source=1FbJSO4BUGj8QTeQ" async></script>"""

html_files = [f for f in glob.glob('**/*.html', recursive=True) if 'google' not in f and '.system_generated' not in f]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing Closebot script tags
    content = re.sub(
        r'<!--\s*Closebot.*-->\s*<script\s+src="https://api\.closebot\.com/scripts/cb\.js\?source=[^"]*"\s*async></script>',
        '',
        content,
        flags=re.IGNORECASE
    )
    content = re.sub(
        r'<script\s+src="https://api\.closebot\.com/scripts/cb\.js\?source=[^"]*"\s*async></script>',
        '',
        content,
        flags=re.IGNORECASE
    )
    
    # Place right after <head>
    if '<head>' in content:
        content = content.replace('<head>', f'<head>\n{pixel_block}')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Placed Closebot pixel at top of <head> in {filepath}")

print("Moved pixel to top of <head> across all HTML files!")
