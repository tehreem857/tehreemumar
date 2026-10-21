import re

# Comprehensive SEO Upgrade Map
seo_updates = {
    'services.html': {
        'title': 'AI Automation & GoHighLevel CRM Services | Tehreem Umar',
        'desc': 'Explore AI automation services by Tehreem Umar: Closebot AI chatbot setup, GoHighLevel CRM workflows, automated sales funnels, and custom AI agents.',
        'h1_target': '<h2 class="section-title">My <span>Services</span></h2>',
        'h1_replacement': '<h1 class="section-title">AI Automation &amp; GoHighLevel <span>Services</span></h1>'
    },
    'projects.html': {
        'title': 'AI & CRM Automation Case Studies | Projects | Tehreem Umar',
        'desc': 'View completed client projects by Tehreem Umar: Closebot qualification chatbots, GoHighLevel pipeline workflows, sales funnels, and AI web applications.',
        'h1_target': '<h2 class="section-title">Selected <span>Work</span></h2>',
        'h1_replacement': '<h1 class="section-title">AI Automation &amp; CRM <span>Projects</span></h1>'
    },
    'skills.html': {
        'title': 'GoHighLevel & AI Automation Tech Stack | Skills | Tehreem Umar',
        'desc': 'Discover the tools and technologies Tehreem Umar specializes in: Closebot AI, GoHighLevel CRM, Make.com, OpenAI API, Python, and webhook integrations.',
        'h1_target': '<h2 class="section-title">Technical <span>Expertise</span></h2>',
        'h1_replacement': '<h1 class="section-title">AI Automation &amp; CRM <span>Tech Stack</span></h1>'
    },
    'process.html': {
        'title': 'AI Automation Consulting Process & Workflow | Tehreem Umar',
        'desc': 'Learn how Tehreem Umar audits, architectures, builds, and deploys high-converting AI chatbots and GoHighLevel CRM workflow automations for businesses.',
        'h1_target': '<h2 class="section-title">How I <span>Work</span></h2>',
        'h1_replacement': '<h1 class="section-title">AI Automation Implementation <span>Process</span></h1>'
    },
    'reviews.html': {
        'title': 'Client Reviews & Testimonials | Tehreem Umar - AI Consultant',
        'desc': 'Read client testimonials and reviews for Tehreem Umar. Real feedback on Closebot AI chatbots, GoHighLevel CRM builds, and business automation workflows.',
        'h1_target': '<h2 class="section-title">Client <span>Feedback</span></h2>',
        'h1_replacement': '<h1 class="section-title">Client Reviews &amp; <span>Testimonials</span></h1>'
    },
    'blogs.html': {
        'title': 'AI Automation & GoHighLevel Insights & Guides | Tehreem Umar',
        'desc': 'In-depth practical guides on Closebot AI setup, GoHighLevel CRM workflow automation, and custom chatbot development written by AI consultant Tehreem Umar.',
        'h1_target': '<h2 class="section-title">AI Automation &amp; <span>GoHighLevel</span> Resource Hub</h2>',
        'h1_replacement': '<h1 class="section-title">AI Automation &amp; <span>GoHighLevel</span> Resource Hub</h1>'
    },
    'contact.html': {
        'title': 'Book an AI Automation & GoHighLevel Consultation | Tehreem Umar',
        'desc': 'Schedule a discovery session with Tehreem Umar to audit your business systems and build Closebot AI chatbots or GoHighLevel CRM workflow automations.',
        'h1_target': '<h2 class="section-title">Let\'s Build <span>Smarter</span> Systems Together</h2>',
        'h1_replacement': '<h1 class="section-title">Book an AI Automation &amp; CRM <span>Consultation</span></h1>'
    },
    'about.html': {
        'title': 'About Tehreem Umar | AI Automation Consultant & GHL Specialist',
        'desc': 'Learn more about Tehreem Umar, an AI Automation Consultant specializing in Closebot conversational systems, GoHighLevel CRM workflows, and digital tools.',
        'h1_target': None,
        'h1_replacement': None
    }
}

for filename, data in seo_updates.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Title
    content = re.sub(r'<title>.*?</title>', f"<title>{data['title']}</title>", content, flags=re.DOTALL)
    
    # Update Meta Description
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']', f'<meta name="description" content="{data["desc"]}"', content)
    
    # Update OpenGraph Title & Description
    content = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']', f'<meta property="og:title" content="{data["title"]}"', content)
    content = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']', f'<meta property="og:description" content="{data["desc"]}"', content)
    content = re.sub(r'<meta\s+property=["\']twitter:title["\']\s+content=["\'].*?["\']', f'<meta property="twitter:title" content="{data["title"]}"', content)
    content = re.sub(r'<meta\s+property=["\']twitter:description["\']\s+content=["\'].*?["\']', f'<meta property="twitter:description" content="{data["desc"]}"', content)

    # Update H1 if target specified
    if data['h1_target'] and data['h1_target'] in content:
        content = content.replace(data['h1_target'], data['h1_replacement'])
        print(f"Upgraded H1 in {filename}")
    elif data['h1_target']:
        print(f"Warning: H1 target not found in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated SEO tags in {filename}")

print("\nOn-Page SEO Upgrade Complete!")
