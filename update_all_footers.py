import os, re

root_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]
blog_dir = 'blog'
blog_files = [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')] if os.path.exists(blog_dir) else []

all_files = root_files + blog_files

print(f"Updating footers across {len(all_files)} HTML files...")

root_footer = """  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo"><img src="images/tehreem_logo.png" alt="tehreemumar.com" class="brand-logo-img"></a>
        <p style="margin-top: 14px; font-size: 0.98rem; color: #475569; max-width: 360px; line-height: 1.6;">A curious mind exploring technology, digital projects, and creative ideas.</p>
      </div>
      
      <div class="footer-nav-col">
        <h4 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 16px;">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="index.html" class="footer-link">Home</a></li>
          <li><a href="about.html" class="footer-link">About</a></li>
          <li><a href="projects.html" class="footer-link">Projects</a></li>
          <li><a href="contact.html" class="footer-link">Contact</a></li>
        </ul>
      </div>
      
      <div class="footer-nav-col">
        <h4 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 16px;">Connect</h4>
        <ul class="footer-links">
          <li><a href="https://www.linkedin.com/in/tehreem-umar" target="_blank" rel="noopener noreferrer" class="footer-link">LinkedIn</a></li>
          <li><a href="https://wa.me/923369197296" target="_blank" rel="noopener noreferrer" class="footer-link">WhatsApp</a></li>
          <li><a href="mailto:tehreems857@gmail.com" class="footer-link">Email</a></li>
        </ul>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <p>&copy; 2026 Tehreem Umar. All rights reserved.</p>
    </div>
  </footer>"""

blog_footer = """  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="logo"><img src="../images/tehreem_logo.png" alt="tehreemumar.com" class="brand-logo-img"></a>
        <p style="margin-top: 14px; font-size: 0.98rem; color: #475569; max-width: 360px; line-height: 1.6;">A curious mind exploring technology, digital projects, and creative ideas.</p>
      </div>
      
      <div class="footer-nav-col">
        <h4 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 16px;">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="../index.html" class="footer-link">Home</a></li>
          <li><a href="../about.html" class="footer-link">About</a></li>
          <li><a href="../projects.html" class="footer-link">Projects</a></li>
          <li><a href="../contact.html" class="footer-link">Contact</a></li>
        </ul>
      </div>
      
      <div class="footer-nav-col">
        <h4 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 16px;">Connect</h4>
        <ul class="footer-links">
          <li><a href="https://www.linkedin.com/in/tehreem-umar" target="_blank" rel="noopener noreferrer" class="footer-link">LinkedIn</a></li>
          <li><a href="https://wa.me/923369197296" target="_blank" rel="noopener noreferrer" class="footer-link">WhatsApp</a></li>
          <li><a href="mailto:tehreems857@gmail.com" class="footer-link">Email</a></li>
        </ul>
      </div>
    </div>
    
    <div class="container footer-bottom">
      <p>&copy; 2026 Tehreem Umar. All rights reserved.</p>
    </div>
  </footer>"""

for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_blog = filepath.startswith('blog/')
    replacement = blog_footer if is_blog else root_footer
    
    new_content = re.sub(r'<!-- Footer -->.*?</footer>', replacement, content, flags=re.DOTALL)
    if new_content == content:
        # Fallback if comment wasn't found
        new_content = re.sub(r'<footer class="footer">.*?</footer>', replacement, content, flags=re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated footer in {filepath}")

print("All footers successfully updated across entire site!")
