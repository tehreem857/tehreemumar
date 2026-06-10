import json

schemas = [
    """
  {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Tehreem Umar — AI Automation Consulting",
    "url": "https://tehreemumar.com",
    "email": "tehreems857@gmail.com",
    "telephone": "+923691972960",
    "description": "AI Automation Consultant specializing in Closebot setup, GoHighLevel CRM workflow automation, custom AI agent development, funnel building, and business process automation.",
    "areaServed": "Worldwide",
    "serviceType": ["AI Automation", "GoHighLevel CRM", "Closebot Setup", "AI Agent Development", "Business Automation", "Funnel Building"],
    "sameAs": ["https://linkedin.com/"],
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "AI Automation Services",
      "itemListElement": [
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Closebot Setup & Optimization",
            "description": "Full Closebot AI chatbot configuration, lead qualification automation, and GoHighLevel CRM integration."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "GoHighLevel CRM Workflow Automation",
            "description": "End-to-end GoHighLevel CRM setup, pipeline automation, funnel building, and trigger-based workflow design."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Custom AI Agent Development",
            "description": "Custom AI-powered business tools, LLM-based chatbots, internal knowledge bases, and API integrations."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Business Process Automation",
            "description": "End-to-end workflow automation using Make.com, Zapier, and custom webhook-based integrations."
          }
        }
      ]
    }
  }
    """,
    """
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Tehreem Umar AI Automation Consulting",
    "url": "https://tehreemumar.com"
  }
    """,
    """
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Tehreem Umar",
    "jobTitle": "AI Automation Consultant & GoHighLevel CRM Expert",
    "url": "https://tehreemumar.com",
    "email": "tehreems857@gmail.com",
    "knowsAbout": ["AI Automation", "GoHighLevel CRM", "Closebot", "Business Process Automation", "AI Agent Development", "Funnel Building", "Make.com", "Zapier"]
  }
    """
]

for i, schema in enumerate(schemas):
    try:
        json.loads(schema)
        print(f"Schema {i+1} is valid JSON.")
    except Exception as e:
        print(f"Schema {i+1} is INVALID: {e}")
