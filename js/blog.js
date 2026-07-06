/**
 * Blog Pages — Premium Animations JS
 * tehreemumar.com — Shared across all blog pages
 */

document.addEventListener('DOMContentLoaded', () => {

  // ==========================================
  // 0. Light / Dark Theme Toggle
  // ==========================================
  const themeToggleBtn = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;

  const applyTheme = (theme) => {
    document.body.setAttribute('data-theme', theme);
    const isLight = theme === 'light';
    const blogNav = document.querySelector('.blog-nav');
    if (blogNav) {
      if (window.scrollY > 40) {
        blogNav.style.background = isLight ? 'rgba(249,249,251,0.96)' : 'rgba(10,10,15,0.96)';
      } else {
        blogNav.style.background = isLight ? 'rgba(249,249,251,0.85)' : 'rgba(10,10,15,0.85)';
      }
    }
  };

  if (savedTheme === 'light' || (!savedTheme && systemPrefersLight)) {
    applyTheme('light');
  } else {
    applyTheme('dark');
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.body.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      document.body.style.transition = 'background-color 0.6s cubic-bezier(0.16, 1, 0.3, 1), color 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      applyTheme(newTheme);
      localStorage.setItem('theme', newTheme);
    });
  }

  // ==========================================
  // 1. Scroll Progress Bar
  // ==========================================
  const progressBar = document.querySelector('.scroll-progress-bar');
  if (progressBar) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          const scrollTop = window.scrollY;
          const docHeight = document.documentElement.scrollHeight - window.innerHeight;
          progressBar.style.width = (scrollTop / docHeight * 100) + '%';
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // ==========================================
  // 2. Cursor Glow Follower
  // ==========================================
  const cursorDot = document.querySelector('.cursor-dot');
  const cursorOutline = document.querySelector('.cursor-outline');
  
  if (cursorDot && cursorOutline && window.matchMedia('(pointer: fine)').matches) {
    let mouseX = 0, mouseY = 0;
    let outlineX = 0, outlineY = 0;
    let rafId = null;

    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      
      cursorDot.style.display = 'block';
      cursorOutline.style.display = 'block';
      
      // Immediate tracking for dot
      cursorDot.style.left = mouseX + 'px';
      cursorDot.style.top = mouseY + 'px';
      
      if (!rafId) rafId = requestAnimationFrame(animateOutline);
    });

    function animateOutline() {
      outlineX += (mouseX - outlineX) * 0.15;
      outlineY += (mouseY - outlineY) * 0.15;
      cursorOutline.style.left = outlineX + 'px';
      cursorOutline.style.top = outlineY + 'px';
      
      if (Math.abs(mouseX - outlineX) > 0.5 || Math.abs(mouseY - outlineY) > 0.5) {
        rafId = requestAnimationFrame(animateOutline);
      } else {
        rafId = null;
      }
    }

    document.addEventListener('mouseleave', () => {
      cursorDot.style.display = 'none';
      cursorOutline.style.display = 'none';
    });

    // Add hover states for interactive elements
    const interactives = document.querySelectorAll('a, button, .hover-target');
    interactives.forEach(el => {
      el.addEventListener('mouseenter', () => {
        cursorOutline.style.width = '70px';
        cursorOutline.style.height = '70px';
        cursorOutline.style.backgroundColor = 'rgba(212, 175, 55, 0.15)';
      });
      el.addEventListener('mouseleave', () => {
        cursorOutline.style.width = '40px';
        cursorOutline.style.height = '40px';
        cursorOutline.style.backgroundColor = 'transparent';
      });
    });
  }

  // ==========================================
  // 3. Floating Particles in Hero
  // ==========================================
  const particlesContainer = document.querySelector('.particles-container');
  if (particlesContainer) {
    for (let i = 0; i < 20; i++) {
      const p = document.createElement('div');
      p.className = 'particle';
      p.style.left = Math.random() * 100 + '%';
      p.style.animationDuration = (6 + Math.random() * 12) + 's';
      p.style.animationDelay   = (Math.random() * 8) + 's';
      const size = (1.5 + Math.random() * 2.5) + 'px';
      p.style.width = size;
      p.style.height = size;
      particlesContainer.appendChild(p);
    }
  }

  // ==========================================
  // 4. Scroll Reveal (IntersectionObserver)
  // ==========================================
  const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Stagger siblings
        const parent = entry.target.parentElement;
        const siblings = parent ? Array.from(parent.querySelectorAll(':scope > .reveal, :scope > .reveal-left, :scope > .reveal-right')) : [];
        if (siblings.length > 1) {
          const idx = siblings.indexOf(entry.target);
          entry.target.style.transitionDelay = `${idx * 0.1}s`;
        }
        entry.target.classList.add('active');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  // Fallback: already-visible elements
  setTimeout(() => {
    revealEls.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        el.classList.add('active');
      }
    });
  }, 100);

  // ==========================================
  // 5. Button Spotlight Effect
  // ==========================================
  document.querySelectorAll('.btn').forEach(btn => {
    if (!btn.querySelector('.btn-spotlight')) {
      const spot = document.createElement('span');
      spot.className = 'btn-spotlight';
      btn.appendChild(spot);
    }
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      btn.style.setProperty('--spot-x', (e.clientX - rect.left) + 'px');
      btn.style.setProperty('--spot-y', (e.clientY - rect.top)  + 'px');
    });
  });

  // ==========================================
  // 6. Step Card Tilt (3D hover)
  // ==========================================
  document.querySelectorAll('.step-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rx = ((y - cy) / cy) * -4;
      const ry = ((x - cx) / cx) * 4;
      card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-3px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(800px) rotateX(0) rotateY(0) translateY(0)';
      card.style.transition = 'transform 0.6s cubic-bezier(0.16,1,0.3,1), border-color 0.4s, box-shadow 0.4s';
      setTimeout(() => { card.style.transition = ''; }, 600);
    });
  });

  // ==========================================
  // 7. Mobile Nav Toggle
  // ==========================================
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const navLinks  = document.querySelector('.nav-links');
  if (mobileBtn && navLinks) {
    mobileBtn.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-open');
      const open = navLinks.classList.contains('mobile-open');
      mobileBtn.setAttribute('aria-expanded', open);
    });
    // Close on link click
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => navLinks.classList.remove('mobile-open'));
    });
  }

  // ==========================================
  // 8. Navbar scroll effect
  // ==========================================
  const blogNav = document.querySelector('.blog-nav');
  if (blogNav) {
    window.addEventListener('scroll', () => {
      const isLight = document.body.getAttribute('data-theme') === 'light';
      if (window.scrollY > 40) {
        blogNav.style.background = isLight ? 'rgba(249,249,251,0.96)' : 'rgba(10,10,15,0.96)';
        blogNav.style.boxShadow  = isLight ? '0 4px 30px rgba(139,92,246,0.03)' : '0 4px 30px rgba(0,0,0,0.3)';
        blogNav.style.borderBottom = '1px solid var(--border)';
      } else {
        blogNav.style.background = isLight ? 'rgba(249,249,251,0.85)' : 'rgba(10,10,15,0.85)';
        blogNav.style.boxShadow  = 'none';
        blogNav.style.borderBottom = '1px solid transparent';
      }
    }, { passive: true });
  }

});
