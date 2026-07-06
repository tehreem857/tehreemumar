document.addEventListener('DOMContentLoaded', () => {
  
  // ==========================================
  // 1. Sticky Header & Mobile Nav Menu
  // ==========================================
  const header = document.getElementById('header');
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const links = document.querySelectorAll('.nav-link');

  // Add scroll class to navbar
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    highlightNavOnScroll();
  });

  // Mobile navigation drawer toggle
  mobileMenuToggle.addEventListener('click', () => {
    const isExpanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';
    mobileMenuToggle.setAttribute('aria-expanded', !isExpanded);
    navLinks.classList.toggle('mobile-active');
  });

  // Close mobile nav drawer when clicking any link
  links.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenuToggle.setAttribute('aria-expanded', 'false');
      navLinks.classList.remove('mobile-active');
    });
  });

  // Highlight current nav item on scroll
  function highlightNavOnScroll() {
    const sections = document.querySelectorAll('section');
    const scrollPos = window.scrollY + 150;

    sections.forEach(section => {
      if (scrollPos >= section.offsetTop && scrollPos < section.offsetTop + section.offsetHeight) {
        const id = section.getAttribute('id');
        links.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  // ==========================================
  // 2. Light / Dark Theme Toggle
  // ==========================================
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  // Set default theme from localStorage or OS Preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  
  if (savedTheme === 'light' || (!savedTheme && systemPrefersLight)) {
    document.body.setAttribute('data-theme', 'light');
  } else {
    document.body.setAttribute('data-theme', 'dark');
  }

  themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.body.style.transition = 'background-color 0.6s cubic-bezier(0.16, 1, 0.3, 1), color 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });

  // ==========================================
  // 3. Scroll Reveal Animations (Staggered Intersection Observer)
  // ==========================================
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Check if this element is inside a grid/container with siblings
        const parent = entry.target.parentElement;
        const siblings = parent ? Array.from(parent.querySelectorAll(':scope > .reveal')) : [];
        
        if (siblings.length > 1) {
          const idx = siblings.indexOf(entry.target);
          entry.target.style.transitionDelay = `${idx * 0.08}s`;
        }
        
        entry.target.classList.add('active');
        
        // Trigger skill progress bars if this is the skills section
        if (entry.target.closest('#skills')) {
          animateSkillBars();
        }

        // Trigger stat counters if this is the about section
        if (entry.target.closest('#about')) {
          animateStatCounters();
        }

        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -80px 0px'
  });

  revealElements.forEach(elem => {
    revealObserver.observe(elem);
  });

  // Trigger skill bars filling up
  function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skill-bar');
    skillBars.forEach(bar => {
      const widthVal = bar.getAttribute('data-width');
      bar.style.width = widthVal;
    });
  }

  // Animate stat counters
  function animateStatCounters() {
    const statItems = document.querySelectorAll('.stat-item h4');
    statItems.forEach(item => {
      const text = item.textContent;
      const match = text.match(/(\d+)/);
      if (!match) return;
      
      const target = parseInt(match[1]);
      const suffix = text.replace(match[1], '').trim();
      const prefix = text.substring(0, text.indexOf(match[1]));
      let current = 0;
      const duration = 1500;
      const startTime = performance.now();
      
      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        current = Math.round(target * eased);
        item.textContent = prefix + current + suffix;
        if (progress < 1) requestAnimationFrame(update);
      }
      requestAnimationFrame(update);
    });
  }

  // Fallback for elements already in viewport
  setTimeout(() => {
    revealElements.forEach(elem => {
      const rect = elem.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        elem.classList.add('active');
        if (elem.closest('#skills')) animateSkillBars();
        if (elem.closest('#about')) animateStatCounters();
      }
    });
  }, 100);

  // ==========================================
  // 4. Testimonial Carousel
  // ==========================================
  const track = document.getElementById('testimonial-track');
  const slides = Array.from(track.children);
  const nextBtn = document.getElementById('carousel-next');
  const prevBtn = document.getElementById('carousel-prev');
  const dotsNav = document.getElementById('carousel-dots');
  
  let currentIndex = 0;
  let autoplayTimer;

  // Create indicator dots dynamically
  slides.forEach((_, index) => {
    const dot = document.createElement('button');
    dot.classList.add('carousel-dot');
    if (index === 0) dot.classList.add('active');
    dot.setAttribute('aria-label', `Go to testimonial slide ${index + 1}`);
    dotsNav.appendChild(dot);
  });

  const dots = Array.from(dotsNav.children);

  const updateSlidePosition = (targetIndex) => {
    // Subtle scale + opacity transition for outgoing/incoming slides
    if (slides[currentIndex]) {
      slides[currentIndex].style.opacity = '0.6';
      slides[currentIndex].style.transform = 'scale(0.96)';
    }
    
    track.style.transform = `translateX(-${targetIndex * 100}%)`;
    
    requestAnimationFrame(() => {
      setTimeout(() => {
        slides.forEach(slide => {
          slide.style.opacity = '1';
          slide.style.transform = 'scale(1)';
        });
      }, 80);
    });
    
    // Update active dot
    dots.forEach(dot => dot.classList.remove('active'));
    dots[targetIndex].classList.add('active');
    currentIndex = targetIndex;
  };

  const nextSlide = () => {
    const targetIndex = (currentIndex + 1) % slides.length;
    updateSlidePosition(targetIndex);
  };

  const prevSlide = () => {
    const targetIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlidePosition(targetIndex);
  };

  // Button triggers
  nextBtn.addEventListener('click', () => {
    nextSlide();
    resetAutoplay();
  });

  prevBtn.addEventListener('click', () => {
    prevSlide();
    resetAutoplay();
  });

  // Dot triggers
  dotsNav.addEventListener('click', e => {
    const targetDot = e.target.closest('.carousel-dot');
    if (!targetDot) return;
    
    const targetIndex = dots.indexOf(targetDot);
    updateSlidePosition(targetIndex);
    resetAutoplay();
  });

  // Autoplay functionality
  const startAutoplay = () => {
    autoplayTimer = setInterval(nextSlide, 6000);
  };

  const resetAutoplay = () => {
    clearInterval(autoplayTimer);
    startAutoplay();
  };

  startAutoplay();

  // Drag / Swipe Gestures on Mobile
  let startX = 0;
  let isDragging = false;

  track.addEventListener('touchstart', e => {
    startX = e.touches[0].clientX;
    isDragging = true;
    clearInterval(autoplayTimer);
  });

  track.addEventListener('touchmove', e => {
    if (!isDragging) return;
    const currentX = e.touches[0].clientX;
    const diff = startX - currentX;
    
    // Threshold swipe to trigger change
    if (Math.abs(diff) > 50) {
      if (diff > 0) {
        nextSlide();
      } else {
        prevSlide();
      }
      isDragging = false;
    }
  });

  track.addEventListener('touchend', () => {
    isDragging = false;
    startAutoplay();
  });

  // ==========================================
  // 5. Contact Form Submission Handling
  // ==========================================
  const contactForm = document.getElementById('contact-form');
  const formFeedback = document.getElementById('form-feedback');

  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const name = document.getElementById('form-name').value.trim();
    const email = document.getElementById('form-email').value.trim();
    const message = document.getElementById('form-message').value.trim();
    const gotcha = contactForm.querySelector('input[name="_gotcha"]')?.value || "";
    const submitBtn = contactForm.querySelector('button[type="submit"]');
    
    // Basic Client-side Validation
    if (!name || !email || !message) {
      showFeedback('Please fill out all required fields to submit.', 'error');
      return;
    }

    if (!isValidEmail(email)) {
      showFeedback('Please provide a valid email address.', 'error');
      return;
    }

    // Change button state to loading
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      Transmitting Request...
      <svg class="spinner" width="18" height="18" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" style="animation: spin 1s linear infinite; margin-left: 8px;">
        <circle cx="12" cy="12" r="10" stroke="rgba(255,255,255,0.2)"></circle>
        <path d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" fill="currentColor"></path>
      </svg>
    `;

    // Formspree endpoint
    const FORM_ENDPOINT = "https://formspree.io/f/mykadknj";
    try {
      const response = await fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, email, message, _gotcha: gotcha })
      });

      if (response.ok) {
        showFeedback('Integration Request Transmitted Successfully. Redirecting...', 'success');
        contactForm.reset();
        setTimeout(() => {
          window.location.href = "/thank-you.html";
        }, 1000);
      } else {
        const errData = await response.json();
        showFeedback(errData.error || 'Failed to transmit request.', 'error');
      }
    } catch (err) {
      showFeedback('Network error. Please try again later.', 'error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnText;
    }
  });

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function showFeedback(msg, type) {
    formFeedback.textContent = msg;
    formFeedback.className = `form-status ${type}`;
    
    // Clear feedback warning after 8 seconds
    if (type === 'error') {
      setTimeout(() => {
        if (formFeedback.className.includes('error')) formFeedback.className = 'form-status';
      }, 8000);
    }
  }

  // ==========================================
  // 6. Copy Clipboard Helper Actions
  // ==========================================
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-copy');
      const originalText = btn.innerHTML;
      
      navigator.clipboard.writeText(textToCopy).then(() => {
        btn.innerHTML = `
          <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"></path></svg>
          Copied!
        `;
        btn.style.color = '#4CAF50';
        
        setTimeout(() => {
          btn.innerHTML = originalText;
          btn.style.color = '';
        }, 2500);
      }).catch(err => {
        console.error('Failed to copy text: ', err);
      });
    });
  });

  // ==========================================
  // 7. Subtle Parallax Glow on Scroll
  // ==========================================
  const glowCircles = document.querySelectorAll('.glow-circle');
  
  if (glowCircles.length > 0) {
    let ticking = false;
    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(() => {
          const scrollY = window.scrollY;
          glowCircles.forEach((glow, i) => {
            const speed = 0.03 + (i * 0.015);
            glow.style.transform = `translateY(${scrollY * speed}px)`;
          });
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  // ==========================================
  // 8. Cursor Glow Follower
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
        cursorOutline.style.backgroundColor = 'rgba(139, 92, 246, 0.15)'; /* Neon Purple */
      });
      el.addEventListener('mouseleave', () => {
        cursorOutline.style.width = '40px';
        cursorOutline.style.height = '40px';
        cursorOutline.style.backgroundColor = 'transparent';
      });
    });
  }

  // ==========================================
  // 9. Scroll Progress Bar
  // ==========================================
  const scrollProgressBar = document.querySelector('.scroll-progress-bar');
  if (scrollProgressBar) {
    let scrollTicking = false;
    window.addEventListener('scroll', () => {
      if (!scrollTicking) {
        requestAnimationFrame(() => {
          const scrollTop = window.scrollY;
          const docHeight = document.documentElement.scrollHeight - window.innerHeight;
          const scrollPercent = (scrollTop / docHeight) * 100;
          scrollProgressBar.style.width = scrollPercent + '%';
          scrollTicking = false;
        });
        scrollTicking = true;
      }
    });
  }

  // ==========================================
  // 10. 3D Tilt Card Effect
  // ==========================================
  const tiltCards = document.querySelectorAll('.tilt-card');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
      card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      setTimeout(() => { card.style.transition = ''; }, 600);
    });
  });

  // ==========================================
  // 11. Magnetic Button Spotlight
  // ==========================================
  const magneticBtns = document.querySelectorAll('.btn');
  magneticBtns.forEach(btn => {
    // Add spotlight element if not already present
    if (!btn.querySelector('.btn-spotlight')) {
      const spotlight = document.createElement('span');
      spotlight.className = 'btn-spotlight';
      btn.appendChild(spotlight);
    }

    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      btn.style.setProperty('--spot-x', x + 'px');
      btn.style.setProperty('--spot-y', y + 'px');
    });
  });

  // ==========================================
  // 12. Hero Title Character Reveal
  // ==========================================
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle && !heroTitle.dataset.split) {
    heroTitle.dataset.split = 'true';
    const childNodes = Array.from(heroTitle.childNodes);
    heroTitle.innerHTML = '';
    let charIndex = 0;

    childNodes.forEach(node => {
      if (node.nodeType === Node.TEXT_NODE) {
        const text = node.textContent;
        for (let i = 0; i < text.length; i++) {
          if (text[i] === ' ') {
            const space = document.createElement('span');
            space.className = 'char-space';
            heroTitle.appendChild(space);
          } else {
            const span = document.createElement('span');
            span.className = 'char';
            span.textContent = text[i];
            span.style.animationDelay = (charIndex * 0.025) + 's';
            heroTitle.appendChild(span);
          }
          charIndex++;
        }
      } else if (node.nodeType === Node.ELEMENT_NODE) {
        // Preserve child elements (like <span> for gradient text)
        const clone = node.cloneNode(false);
        const innerText = node.textContent;
        for (let i = 0; i < innerText.length; i++) {
          if (innerText[i] === ' ') {
            const space = document.createElement('span');
            space.className = 'char-space';
            clone.appendChild(space);
          } else {
            const span = document.createElement('span');
            span.className = 'char';
            span.textContent = innerText[i];
            span.style.animationDelay = (charIndex * 0.025) + 's';
            clone.appendChild(span);
          }
          charIndex++;
        }
        heroTitle.appendChild(clone);
      }
    });
  }

  // ==========================================
  // 13. Floating Particles in Hero
  // ==========================================
  const particlesContainer = document.querySelector('.particles-container');
  if (particlesContainer) {
    const particleCount = 25;
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.className = 'particle';
      particle.style.left = Math.random() * 100 + '%';
      particle.style.animationDuration = (8 + Math.random() * 15) + 's';
      particle.style.animationDelay = (Math.random() * 10) + 's';
      particle.style.width = (2 + Math.random() * 3) + 'px';
      particle.style.height = particle.style.width;
      particlesContainer.appendChild(particle);
    }
  }

  // ==========================================
  // 14. Directional Scroll Reveals
  // ==========================================
  const directionalElements = document.querySelectorAll('.reveal-left, .reveal-right');
  const dirRevealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        dirRevealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -60px 0px'
  });

  directionalElements.forEach(el => dirRevealObserver.observe(el));

  // ==========================================
  // 15. Add Animated Border Glow to Glass Cards
  // ==========================================
  document.querySelectorAll('.glass-card').forEach(card => {
    if (!card.querySelector('.card-border-glow')) {
      const glow = document.createElement('div');
      glow.className = 'card-border-glow';
      card.insertBefore(glow, card.firstChild);
    }
  });

});

// Spin Animation Keyframes injected in CSS (helper)
const style = document.createElement('style');
style.textContent = `
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;
document.head.appendChild(style);
