/**
 * cursor.js - Magnetic Trail Cursor Effect
 * Works independently on every page.
 */
(function () {
  // Only run on desktop (pointer: fine means mouse, not touch)
  if (!window.matchMedia('(pointer: fine)').matches) return;

  const dot = document.querySelector('.cursor-dot');
  const outline = document.querySelector('.cursor-outline');
  if (!dot || !outline) return;

  let mouseX = 0, mouseY = 0;
  let outlineX = 0, outlineY = 0;
  let rafId = null;

  // Show cursors initially hidden, reveal on first move
  dot.style.display = 'none';
  outline.style.display = 'none';

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    // Snap dot instantly
    dot.style.left = mouseX + 'px';
    dot.style.top  = mouseY + 'px';
    dot.style.display = 'block';
    outline.style.display = 'block';

    // Smooth trailing animation via rAF
    if (!rafId) {
      rafId = requestAnimationFrame(animateOutline);
    }
  });

  function animateOutline() {
    outlineX += (mouseX - outlineX) * 0.12;
    outlineY += (mouseY - outlineY) * 0.12;

    outline.style.left = outlineX + 'px';
    outline.style.top  = outlineY + 'px';

    rafId = requestAnimationFrame(animateOutline);
  }

  // Hide when mouse leaves window
  document.addEventListener('mouseleave', () => {
    dot.style.display = 'none';
    outline.style.display = 'none';
  });

  document.addEventListener('mouseenter', () => {
    dot.style.display = 'block';
    outline.style.display = 'block';
  });

  // Magnetic expand on interactive elements
  const interactives = document.querySelectorAll('a, button, .hover-target, input, textarea');
  interactives.forEach(el => {
    el.addEventListener('mouseenter', () => {
      outline.style.width = '70px';
      outline.style.height = '70px';
      outline.style.backgroundColor = 'rgba(139, 92, 246, 0.15)';
    });
    el.addEventListener('mouseleave', () => {
      outline.style.width = '40px';
      outline.style.height = '40px';
      outline.style.backgroundColor = 'transparent';
    });
  });
})();
