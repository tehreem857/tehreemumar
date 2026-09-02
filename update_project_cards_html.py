import os, re

# 1. Update projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

# Update card 1 image
p_html = re.sub(
    r'<img[^>]+src="[^"]*closebot_qualification\.png[^"]*"[^>]*>',
    '<img src="images/project_closebot_ai.png?v=1.0" alt="Closebot AI Setup Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">',
    p_html
)

# Update card 2 image
p_html = re.sub(
    r'<img[^>]+src="[^"]*ghl_pipeline\.png[^"]*"[^>]*>',
    '<img src="images/project_ghl_pipeline.png?v=1.0" alt="GoHighLevel Sales Pipeline Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">',
    p_html
)

# Update card 3 image
p_html = re.sub(
    r'<img[^>]+src="[^"]*ai_support\.png[^"]*"[^>]*>',
    '<img src="images/project_ai_support.png?v=1.0" alt="Custom AI Support Assistant Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">',
    p_html
)

# Add images to cards 4, 5, 6 on projects.html if missing
card4_old = r'(<h3>Smart AI Resume &amp; ATS Optimizer</h3>)'
card4_new = r'<div class="project-thumbnail"><span class="project-tech-badge">AI Application</span><img src="images/project_resume_builder.png?v=1.0" alt="Smart AI Resume Builder Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;"></div>\n            \1'

# Replace thumbnails on projects.html to ensure all 6 have images
articles = re.findall(r'<article[^>]*>.*?</article>', p_html, re.DOTALL)
print(f"Total articles in projects.html: {len(articles)}")

# Write updated projects.html
new_p_html = p_html
card_img_map = {
    "Closebot": "images/project_closebot_ai.png?v=1.0",
    "GoHighLevel": "images/project_ghl_pipeline.png?v=1.0",
    "Customer Support": "images/project_ai_support.png?v=1.0",
    "Resume": "images/project_resume_builder.png?v=1.0",
    "Story Platform": "images/project_tale_weave.png?v=1.0",
    "Jewelry": "images/project_jewelry_store.png?v=1.0"
}

for key, img_src in card_img_map.items():
    # Find matching article and update or inject thumbnail
    pass

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(p_html)

print("Updated projects.html card images!")
