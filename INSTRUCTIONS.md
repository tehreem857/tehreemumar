# Project Instructions — Tehreem Umar Portfolio

## Owner
- **Name:** Tehreem Umar
- **Email:** tehreems857@gmail.com
- **WhatsApp:** +92 369 197296
- **Website:** https://tehreemumar.com
- **GitHub:** https://github.com/tehreem857/tehreemumar
- **GitHub Username:** tehreem857

## Project Overview
AI Automation Specialist portfolio website — a luxury, dark-themed, single-page site built with vanilla HTML, CSS, and JavaScript (no frameworks). Hosted for free on **GitHub Pages** with custom domain `tehreemumar.com`.

## Tech Stack
- **Frontend:** Vanilla HTML5, CSS3, JavaScript (no React, no frameworks)
- **Fonts:** Outfit (headings) + Plus Jakarta Sans (body) via Google Fonts
- **Calendar:** Calendly inline widget embed
- **Hosting:** GitHub Pages (free tier)
- **Domain Registrar:** Namecheap
- **Previous Host:** Netlify (migrated away due to usage limits)

## Deployment Workflow
1. Edit files locally in `C:\Users\User\.gemini\antigravity\scratch\tehreem-portfolio\`
2. Push changes to GitHub via the GitHub REST API (using PowerShell scripts)
3. GitHub Pages auto-deploys from the `main` branch within ~60 seconds
4. **Important:** Always use `BypassSandbox: true` when pushing to GitHub (network access required)
5. **Important:** Do NOT push `.ps1` script files — they contain tokens and will be blocked by GitHub's secret scanner

## Design Theme
- **Style:** Glassmorphism + luxury dark tech aesthetic
- **Primary Background:** `#0F0908` (deep dark)
- **Secondary Background:** `#190F0D`
- **Accent Color:** Indian Yellow `#E3A857`
- **Secondary Accent:** Russet `#80461B`
- **Text:** White `#FFFFFF` primary, `#D4C9C6` secondary
- **Cards:** Glass-effect with blur, subtle gold borders
- **Light Mode:** Also supported via `[data-theme="light"]`

## Design Standards & Inspiration

- Follow **Emil Kowalski's design philosophy** for smooth motion, elegant animations, and refined micro-interactions.
- Apply **Impeccable Design** principles with exceptional attention to layout, spacing, typography, alignment, and visual hierarchy.
- Use **Taste Kill-quality references** for modern SaaS, portfolio, and agency website aesthetics.
- Prioritize **premium, polished, production-ready UI** over generic templates.
- Use subtle scroll animations, hover effects, and page transitions that feel natural and performant.
- Maintain consistent spacing, strong contrast, and excellent readability across all sections.
- Prefer clean, modern typography and high-end visual presentation.
- Every page should feel thoughtfully designed, visually balanced, and portfolio-worthy.

## File Structure
```
tehreem-portfolio/
├── index.html          # Single-page site (all sections)
├── css/styles.css      # All styles, variables, responsive breakpoints
├── js/main.js          # Scroll animations, carousel, form handling, theme toggle
└── images/             # AI-generated mockup images (PNG)
```

## Key Reminders
- Always match the Calendly widget colors to the site theme (`background_color=190f0d&text_color=ffffff&primary_color=e3a857`)
- Style `<select>` dropdown options explicitly for dark backgrounds
- Use `align-items: start` on grid layouts to prevent unwanted vertical stretching
- Keep all changes responsive (breakpoints at 1024px, 768px, 480px)
- Never use placeholder images — generate real ones with the image tool
