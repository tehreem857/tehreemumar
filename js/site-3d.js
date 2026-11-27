/* Tehreem Umar — 3D site UI behaviour (non-WebGL parts) */
(function () {
  const root = document.documentElement;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.add('js');

  /* Loader: hide when the 3D scene is ready, or after a safety timeout */
  const loader = document.getElementById('loader');
  let loaderDone = false;
  function hideLoader() {
    if (loaderDone) return;
    loaderDone = true;
    if (loader) loader.classList.add('done');
    introReveal();
  }
  window.addEventListener('scene-ready', () => { root.classList.add('scene-on'); hideLoader(); });
  if (loader) {
    window.addEventListener('load', () => setTimeout(hideLoader, 400));
    setTimeout(hideLoader, 2500);
  } else {
    // inner pages: no loader, reveal content straight away
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', hideLoader);
    else hideLoader();
  }

  /* Mark the current page in the nav */
  const here = location.pathname.split('/').pop() || 'index.html';
  const navKey = document.body.dataset.nav; // e.g. service pages highlight "Services"
  document.querySelectorAll('.nav-links a').forEach((a) => {
    const file = a.getAttribute('href').split('/').pop();
    if (file === here || (navKey && file === navKey + '.html')) a.classList.add('active');
  });

  /* Contact form: preselect the service when arriving from a service page */
  const SERVICE_OPTIONS = {
    closebot: 'Closebot Setup & Optimization',
    gohighlevel: 'GoHighLevel CRM Management',
    website: 'Website Development',
    webapp: 'Custom AI Application Development',
  };
  const wanted = SERVICE_OPTIONS[new URLSearchParams(location.search).get('service')];
  const serviceSelect = document.getElementById('form-service');
  if (wanted && serviceSelect) {
    const opt = [...serviceSelect.options].find((o) => o.value === wanted);
    if (opt) serviceSelect.value = wanted;
  }

  /* Skill bars fill when visible */
  const bars = document.querySelectorAll('.bar i[data-w]');
  if (bars.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.style.width = en.target.dataset.w; io.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    bars.forEach((b) => io.observe(b));
  }

  /* Contact form: validate, then submit natively to Web3Forms */
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      const val = (id) => (document.getElementById(id)?.value || '').trim();
      const fb = document.getElementById('form-feedback');
      const fail = (msg) => { e.preventDefault(); fb.textContent = msg; fb.className = 'form-status error'; };
      if (!val('form-name') || !val('form-email') || !val('form-message')) return fail('Please fill out all required fields.');
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val('form-email'))) return fail('Please provide a valid email address.');
      const svc = document.getElementById('form-service');
      document.getElementById('form-subject').value = `New Booking from ${val('form-name')} — ${svc.options[svc.selectedIndex].text}`;
      const btn = form.querySelector('button[type="submit"]');
      btn.textContent = 'Sending…';
      btn.style.pointerEvents = 'none';
      btn.style.opacity = '0.7';
    });
  }

  /* Header state */
  const header = document.getElementById('header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Mobile menu */
  const menuBtn = document.getElementById('menu-btn');
  const links = document.getElementById('nav-links');
  menuBtn.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.style.overflow = open ? 'hidden' : '';
  });
  links.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' && links.classList.contains('open')) menuBtn.click();
  });

  /* 3D tilt + spotlight on cards (pointer devices only) */
  if (!reduce && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.tilt').forEach((el) => {
      el.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width;
        const y = (e.clientY - r.top) / r.height;
        el.style.setProperty('--mx', x * 100 + '%');
        el.style.setProperty('--my', y * 100 + '%');
        el.style.transform = `rotateX(${(0.5 - y) * 8}deg) rotateY(${(x - 0.5) * 10}deg) translateZ(0)`;
      });
      el.addEventListener('pointerleave', () => { el.style.transform = ''; });
    });
  }

  /* Reveal animations */
  function introReveal() {
    const hasGsap = typeof window.gsap !== 'undefined';
    const all = document.querySelectorAll('.reveal');
    if (!hasGsap || reduce) {
      all.forEach((el) => { el.style.opacity = 1; el.style.transform = 'none'; });
      return;
    }
    gsap.registerPlugin(ScrollTrigger);
    const heroEls = document.querySelectorAll('.hero .reveal');
    gsap.to(heroEls, { opacity: 1, y: 0, duration: 1.2, ease: 'expo.out', stagger: 0.12, delay: 0.1 });

    document.querySelectorAll('.reveal').forEach((el) => {
      if (el.closest('.hero')) return;
      gsap.to(el, {
        opacity: 1, y: 0, duration: 1.1, ease: 'expo.out',
        scrollTrigger: { trigger: el, start: 'top 88%' },
      });
    });
  }
})();

/* Global Closebot widget handler (same logic as main.js) */
window.triggerClosebotWidget = function (e) {
  if (e && e.preventDefault) e.preventDefault();
  const cbBtn = document.querySelector('.cb-btn') || document.querySelector('[data-cb].cb-btn');
  if (cbBtn) { cbBtn.click(); return; }
  const cbPanel = document.querySelector('.cb-panel') || document.querySelector('[data-cb].cb-panel');
  if (cbPanel) {
    cbPanel.classList.remove('hidden');
    cbPanel.style.opacity = '1';
    cbPanel.style.pointerEvents = 'auto';
    cbPanel.style.transform = 'translateY(0)';
    return;
  }
  if (typeof window.Closebot === 'function') { try { window.Closebot('open'); return; } catch (err) {} }
  if (typeof window.CloseBot === 'function') { try { window.CloseBot('open'); return; } catch (err) {} }
  const alt = ['#closebot-chat-button', '#closebot-widget-launcher', '#closebot-launcher', '.cb-launcher', '#cb-button', '#cb-widget-btn', 'button[id*="closebot"]', 'div[id*="closebot"]', 'iframe[src*="closebot"]'];
  for (const sel of alt) { const el = document.querySelector(sel); if (el) { el.click(); return; } }
  window.location.href = 'contact.html';
};
