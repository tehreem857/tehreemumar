import os
import glob
import re

blog_dir = r"C:\Users\User\.gemini\antigravity\scratch\tehreem-portfolio\blog"
html_files = glob.glob(os.path.join(blog_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add favicon and Google fonts link tags right after viewport meta
    favicon_fonts = """  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E⚡%3C/text%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">"""
    content = content.replace('  <meta name="viewport" content="width=device-width, initial-scale=1.0">', favicon_fonts)

    # 2. Replace all instances of 2025-06-02 with 2026-06-04
    content = content.replace('2025-06-02', '2026-06-04')

    # 3. Add dateModified to JSON-LD schemas
    content = content.replace('"datePublished": "2026-06-04",', '"datePublished": "2026-06-04",\n    "dateModified": "2026-06-04",')

    # 4, 5, 6, 7. Replace (Step-by-Step 2025) and (2025) with 2026
    content = content.replace('(Step-by-Step 2025)', '(Step-by-Step 2026)')
    content = content.replace('(2025)', '(2026)')

    # 8. Add og:site_name
    content = re.sub(r'(<meta property="og:image" content=".*">\n)', r'\1  <meta property="og:site_name" content="Tehreem Umar — AI Automation Consulting">\n', content)

    # 9. Remove @import from CSS
    content = content.replace("@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');", "")

    # 10. Add BreadcrumbList schema after the last </script> in <head>
    # Find the last </script> before <style>
    style_idx = content.find("<style>")
    last_script_idx = content.rfind("</script>", 0, style_idx)
    
    if last_script_idx != -1:
        # Determine the name for the breadcrumb based on filename
        if "closebot" in file_path:
            breadcrumb_name = "Closebot GoHighLevel Integration"
        elif "ai-lead" in file_path:
            breadcrumb_name = "AI Lead Qualification Chatbot Systems"
        else:
            breadcrumb_name = "GoHighLevel CRM Workflow Automation Guide"

        breadcrumb_schema = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://tehreemumar.com/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://tehreemumar.com/#blog" }},
      {{ "@type": "ListItem", "position": 3, "name": "{breadcrumb_name}" }}
    ]
  }}
  </script>
"""
        content = content[:last_script_idx + 9] + breadcrumb_schema + content[last_script_idx + 9:]

    # 11. Footer and Hero dates
    content = content.replace('© 2025', '© 2026')
    content = content.replace('June 2025', 'June 2026')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Fixed SEO issues in: {file_path}")

print("All blog files fixed.")
