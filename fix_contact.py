import re

filepath = 'contact.html'
content = open(filepath, 'r', encoding='utf-8').read()

# Define the broken section to replace (from <!-- Hero Section --> to </section>)
old_section_pattern = r'  <!-- Hero Section -->.*?</section>'

new_section = '''  <!-- Contact Section -->
  <main style="padding-top: 80px;">
  <section class="section" id="contact">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Let\'s Connect</span>
        <h2 class="section-title">Let\'s Build <span>Smarter</span> Systems Together</h2>
        <p class="section-subtitle">Drop an inquiry to outline your systems design roadmap.</p>
      </div>

      <!-- Contact 2-column grid: Form + Animation Panel -->
      <div class="contact-grid">

        <!-- Contact Form -->
        <div class="contact-form-panel glass-card reveal">
          <h3 class="contact-form-title">Send a Message</h3>
          <form id="contact-form" novalidate>
            <!-- Honeypot Spam Protection -->
            <input type="text" name="_gotcha" style="display:none !important" tabindex="-1" autocomplete="off">
            <div class="form-group">
              <label for="form-name" class="form-label">Full Name</label>
              <input type="text" id="form-name" class="form-input" placeholder="e.g. John Doe" required>
            </div>

            <div class="form-group">
              <label for="form-email" class="form-label">Email Address</label>
              <input type="email" id="form-email" class="form-input" placeholder="e.g. john@example.com" required>
            </div>

            <div class="form-group">
              <label for="form-service" class="form-label">Select Core Service Required</label>
              <select id="form-service" class="form-input" style="appearance: none; background-image: url(\'data:image/svg+xml;utf8,<svg fill=&quot;%238B5CF6&quot; height=&quot;24&quot; viewBox=&quot;0 0 24 24&quot; width=&quot;24&quot; xmlns=&quot;http://www.w3.org/2000/svg&quot;><path d=&quot;M7 10l5 5 5-5z&quot;/></svg>\'); background-repeat: no-repeat; background-position: right 12px center;">
                <option value="closebot">Closebot Setup &amp; Optimization</option>
                <option value="ghl">GoHighLevel CRM Management</option>
                <option value="ai-app">Custom AI Application Development</option>
                <option value="automation">Business Workflow Integration</option>
              </select>
            </div>

            <div class="form-group">
              <label for="form-message" class="form-label">Operation Details &amp; Description</label>
              <textarea id="form-message" class="form-input" placeholder="Please outline the workflow bottleneck you wish to automate..." required></textarea>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;">
              Transmit Operations Request
              <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"></path>
              </svg>
            </button>
            <div id="form-feedback" class="form-status" role="alert"></div>
          </form>
        </div>

        <!-- Animated Info Panel -->
        <div class="contact-anim-panel reveal">

          <!-- Orbiting animation -->
          <div class="contact-orbit-wrap">
            <div class="contact-orbit-core">\u2709\ufe0f</div>
            <div class="contact-orbit-ring">
              <span class="contact-orbit-dot"></span>
            </div>
            <div class="contact-orbit-ring">
              <span class="contact-orbit-dot"></span>
            </div>
            <div class="contact-orbit-ring">
              <span class="contact-orbit-dot"></span>
            </div>
          </div>

          <!-- Floating Info Chips -->
          <div class="contact-stat-chips">
            <div class="contact-stat-chip">
              <div class="contact-stat-icon green">\u26a1</div>
              <div class="contact-stat-info">
                <div class="contact-stat-label">Response Time</div>
                <div class="contact-stat-value">Within 24 Hours</div>
              </div>
            </div>
            <div class="contact-stat-chip">
              <div class="contact-stat-icon gold">\U0001f91d</div>
              <div class="contact-stat-info">
                <div class="contact-stat-label">Discovery Session</div>
                <div class="contact-stat-value">Free 30-Min Call</div>
              </div>
            </div>
            <div class="contact-stat-chip">
              <div class="contact-stat-icon blue">\U0001f30d</div>
              <div class="contact-stat-info">
                <div class="contact-stat-label">Availability</div>
                <div class="contact-stat-value">Remote \u00b7 Worldwide</div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>
  </section>'''

new_content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)

if new_content == content:
    print("ERROR: Pattern not matched! No changes made.")
else:
    open(filepath, 'w', encoding='utf-8').write(new_content)
    print("SUCCESS: contact.html updated cleanly!")
