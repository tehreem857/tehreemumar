import re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update image cache version tags to v=7.0 across all cards
html = re.sub(r'images/project_resume_builder\.png\?v=\d+\.\d+', 'images/project_resume_builder.png?v=7.0', html)
html = re.sub(r'images/project_tale_weave\.png\?v=\d+\.\d+', 'images/project_tale_weave.png?v=7.0', html)
html = re.sub(r'images/project_jewelry_store\.png\?v=\d+\.\d+', 'images/project_jewelry_store.png?v=7.0', html)
html = re.sub(r'images/project_closebot_ai\.png\?v=\d+\.\d+', 'images/project_closebot_ai.png?v=7.0', html)
html = re.sub(r'images/project_ghl_pipeline\.png\?v=\d+\.\d+', 'images/project_ghl_pipeline.png?v=7.0', html)
html = re.sub(r'images/project_ai_support\.png\?v=\d+\.\d+', 'images/project_ai_support.png?v=7.0', html)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated image tags in projects.html with v=7.0!")
