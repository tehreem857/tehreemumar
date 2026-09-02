import os, re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build clean project card blocks for projects.html
new_cards_html = """        <!-- Project 1: Closebot AI Chatbot -->
        <article class="project-card glass-card tilt-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">Closebot + GHL</span>
            <img src="images/project_closebot_ai.png?v=2.0" alt="Closebot AI Lead Qualification System UI Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>AI Lead Qualification System (Closebot)</h3>
            <p>Built a comprehensive Closebot SMS & web automation agent that interacts with prospects, filters low-fit inquiries, and updates GHL opportunity stages automatically.</p>
            <div class="project-results">
              <div class="project-results-label">Results Achieved</div>
              <div class="project-results-val">85% qualification deflection rate &bull; 3.2x Booking Velocity</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">Closebot</span>
              <span class="project-tag">GHL CRM</span>
              <span class="project-tag">OpenAI API</span>
              <span class="project-tag">Make.com</span>
            </div>
            <a href="contact.html" class="project-link">
              Book a Closebot Setup Consultation
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>

        <!-- Project 2: GHL Pipeline -->
        <article class="project-card glass-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">GoHighLevel</span>
            <img src="images/project_ghl_pipeline.png?v=2.0" alt="GoHighLevel Sales Pipeline Automation Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>GoHighLevel Sales Pipeline Automation</h3>
            <p>Designed a multi-stage lead workflow inside GoHighLevel that auto-assigns contacts, sends SMS booking reminders, and updates CRM opportunity stages.</p>
            <div class="project-results">
              <div class="project-results-label">Results Achieved</div>
              <div class="project-results-val">+42% Appointment Show Rate &bull; Zero Lost Leads</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">GoHighLevel</span>
              <span class="project-tag">Webhooks</span>
              <span class="project-tag">SMS Workflows</span>
              <span class="project-tag">Zapier</span>
            </div>
            <a href="contact.html" class="project-link">
              View Project Details
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>

        <!-- Project 3: AI Support Assistant -->
        <article class="project-card glass-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">Custom Agent</span>
            <img src="images/project_ai_support.png?v=2.0" alt="Custom AI Customer Support Assistant UI Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>Custom AI Customer Support Assistant</h3>
            <p>Developed a high-speed Python AI chatbot linked to internal documentation to instantly reply to high-frequency technical customer inquiries 24/7.</p>
            <div class="project-results">
              <div class="project-results-label">Results Achieved</div>
              <div class="project-results-val">78% Support Deflection Rate &bull; 0.9s Average Response Time</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">Python</span>
              <span class="project-tag">FastAPI</span>
              <span class="project-tag">Vector DB</span>
              <span class="project-tag">GPT-4</span>
            </div>
            <a href="contact.html" class="project-link">
              View Project Details
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>

        <!-- Project 4: Smart AI Resume Builder -->
        <article class="project-card glass-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">AI Application</span>
            <img src="images/project_resume_builder.png?v=2.0" alt="Smart AI Resume Builder Web Application UI Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>Smart AI Resume &amp; ATS Optimizer</h3>
            <p>Interactive web application that guides users through a multi-step resume builder with real-time AI content suggestions and instant PDF rendering.</p>
            <div class="project-results">
              <div class="project-results-label">Measurable Impact</div>
              <div class="project-results-val">Saved 15+ hrs/wk onboarding &bull; 95% ATS Pass Rate</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">JavaScript</span>
              <span class="project-tag">HTML5/CSS3</span>
              <span class="project-tag">html2pdf</span>
              <span class="project-tag">AI UX</span>
            </div>
            <a href="https://tehreem857.github.io/resume-generator" target="_blank" rel="noopener noreferrer" class="project-link">
              Launch Live App ↗
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>

        <!-- Project 5: TaleWeave Story Platform -->
        <article class="project-card glass-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">Creative Platform</span>
            <img src="images/project_tale_weave.png?v=2.0" alt="TaleWeave Interactive Story Platform UI Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>Interactive Web Story Platform</h3>
            <p>Single-Page Application with custom client-side router, state management store, reader view, and interactive storytelling experience.</p>
            <div class="project-results">
              <div class="project-results-label">Measurable Impact</div>
              <div class="project-results-val">High Engagement SPA Architecture &bull; 0.1s Instant Routing</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">Vanilla JS SPA</span>
              <span class="project-tag">State Store</span>
              <span class="project-tag">Custom Router</span>
            </div>
            <a href="https://tehreem857.github.io/tale-weave" target="_blank" rel="noopener noreferrer" class="project-link">
              Launch Live App ↗
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>

        <!-- Project 6: AURÉLIE Jewelry Shop -->
        <article class="project-card glass-card reveal">
          <div class="project-thumbnail">
            <span class="project-tech-badge">E-Commerce UI</span>
            <img src="images/project_jewelry_store.png?v=2.0" alt="Luxury Handmade Jewelry Web Store UI Preview" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0;">
          </div>
          <div class="project-info">
            <h3>Luxury Handmade Jewelry Web Store</h3>
            <p>Minimal, high-end e-commerce interface showcasing curated jewelry, smooth cart drawer, luxury typography, and elegant layout.</p>
            <div class="project-results">
              <div class="project-results-label">Measurable Impact</div>
              <div class="project-results-val">+38% Mobile Checkout Conversion &bull; Clean Luxury Design</div>
            </div>
            <div class="project-tags">
              <span class="project-tag">E-Commerce</span>
              <span class="project-tag">Responsive UI</span>
              <span class="project-tag">CSS Grid</span>
            </div>
            <a href="https://tehreem857.github.io/jewelry-shop" target="_blank" rel="noopener noreferrer" class="project-link">
              Launch Live App ↗
              <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"></path>
              </svg>
            </a>
          </div>
        </article>"""

# Replace projects grid content in projects.html
grid_pattern = r'<div class="projects-grid">.*?</div>\s*</div>\s*</section>'
replacement_grid = '<div class="projects-grid">\n' + new_cards_html + '\n      </div>\n    </div>\n  </section>'

updated_p_html = re.sub(grid_pattern, replacement_grid, html, flags=re.DOTALL)

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(updated_p_html)

print("Updated all 6 project cards in projects.html with clean, theme-matching UI preview images!")
