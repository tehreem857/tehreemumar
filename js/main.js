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
    
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });

  // ==========================================
  // 3. Scroll Reveal Animations (Intersection Observer)
  // ==========================================
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Once visible, trigger skill progress bars if this is the skills section
        if (entry.target.id === 'skills') {
          animateSkillBars();
        }
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
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

  // Fallback for elements already in viewport
  setTimeout(() => {
    revealElements.forEach(elem => {
      const rect = elem.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        elem.classList.add('active');
        if (elem.id === 'skills') animateSkillBars();
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
    track.style.transform = `translateX(-${targetIndex * 100}%)`;
    
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

    // Mock API request network delay
    try {
      await new Promise(resolve => setTimeout(resolve, 1800));
      
      // Success response
      showFeedback('Integration Request Transmitted Successfully. Tehreem will review and reply within 12 hours.', 'success');
      contactForm.reset();
    } catch (err) {
      showFeedback('Failed to transmit request. Please retry or contact tehreems857@gmail.com directly.', 'error');
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
