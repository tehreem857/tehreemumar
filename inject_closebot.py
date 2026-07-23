import os
import glob

script_tag = """  <!-- Closebot -->
  <script src="https://api.closebot.com/scripts/cb.js?source=JHI94PrQQnZmAli4" async></script>
"""

# Find all HTML files
html_files = glob.glob('**/*.html', recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "api.closebot.com/scripts/cb.js" not in content:
        # Insert before </head>
        content = content.replace("</head>", script_tag + "</head>")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Already updated {file}")
