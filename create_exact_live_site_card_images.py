import os
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 480

emerald = (16, 185, 129)       # #10B981
gold = (245, 158, 11)          # #F59E0B
dark_slate = (15, 23, 42)      # #0F172A
light_bg = (248, 250, 252)     # #F8FAFC
white = (255, 255, 255)
border_color = (226, 232, 240)  # #E2E8F0
purple_accent = (99, 102, 241)  # #6366F1

try:
    font_title = ImageFont.truetype('arialbd.ttf', 28)
    font_sub = ImageFont.truetype('arialbd.ttf', 20)
    font_regular = ImageFont.truetype('arial.ttf', 16)
    font_small = ImageFont.truetype('arial.ttf', 14)
    font_serif = ImageFont.truetype('georgiab.ttf', 24)
except:
    font_title = font_sub = font_regular = font_small = font_serif = ImageFont.load_default()

def draw_window_header(draw, url_text):
    draw.rectangle([(0, 0), (W, H)], fill=light_bg)
    draw.rectangle([(0, 0), (W, 50)], fill=white)
    draw.line([(0, 50), (W, 50)], fill=border_color, width=1)
    
    # Dots
    draw.ellipse([(18, 18), (30, 30)], fill=(239, 68, 68))
    draw.ellipse([(38, 18), (50, 30)], fill=(245, 158, 11))
    draw.ellipse([(58, 18), (70, 30)], fill=(16, 185, 129))
    
    # Address bar
    draw.rectangle([(110, 12), (690, 38)], fill=light_bg, outline=border_color, width=1)
    draw.text((130, 16), url_text, fill=(100, 116, 139), font=font_small)

# ==========================================
# 1. ResumeAI — Smart AI Resume Builder
# ==========================================
img1 = Image.new('RGB', (W, H), white)
draw1 = ImageDraw.Draw(img1)
draw_window_header(draw1, "https://tehreem857.github.io/resume-generator")

# ResumeAI Top Nav
draw1.rectangle([(0, 51), (W, 105)], fill=white)
draw1.line([(0, 105), (W, 105)], fill=border_color, width=1)
draw1.text((30, 68), "📄 ResumeAI", fill=dark_slate, font=font_sub)

# Action button top right
draw1.rectangle([(590, 64), (770, 96)], fill=emerald)
draw1.text((610, 72), "✨ AI Fast Generate", fill=white, font=font_small)

# Hero Section matching live site
draw1.rectangle([(30, 120), (520, 145)], fill=(236, 253, 245), outline=emerald)
draw1.text((45, 125), "✨ Multi-Step Wizard · 20+ Templates · Instant ATS Check", fill=(4, 120, 87), font=font_small)

draw1.text((30, 160), "Create a Job-Winning Resume", fill=dark_slate, font=font_title)
draw1.text((30, 195), "In 5 Minutes with AI", fill=emerald, font=font_title)
draw1.text((30, 235), "Skip the forms. Use our step-by-step AI wizard and optimize for ATS.", fill=(100, 116, 139), font=font_regular)

# Buttons
draw1.rectangle([(30, 275), (200, 315)], fill=emerald)
draw1.text((50, 288), "Choose Template →", fill=white, font=font_small)

draw1.rectangle([(215, 275), (370, 315)], fill=white, outline=border_color)
draw1.text((235, 288), "✨ AI Auto-Build", fill=dark_slate, font=font_small)

# Resume Template Preview Card on Right
draw1.rectangle([(440, 120), (770, 440)], fill=white, outline=border_color)
# Header bar on preview
draw1.rectangle([(440, 120), (770, 180)], fill=dark_slate)
draw1.text((460, 135), "ALEX MORGAN", fill=white, font=font_sub)
draw1.text((460, 160), "Senior Full Stack Engineer", fill=emerald, font=font_small)

# Body lines
draw1.rectangle([(460, 200), (740, 215)], fill=(226, 232, 240))
draw1.rectangle([(460, 225), (680, 240)], fill=(226, 232, 240))
draw1.rectangle([(460, 260), (750, 330)], fill=(241, 245, 249), outline=border_color)
draw1.text((475, 275), "ATS Match Score: 98/100", fill=emerald, font=font_sub)
draw1.text((475, 305), "✔ Key Tech Skills Verified", fill=(4, 120, 87), font=font_small)

# Direct Export badge bottom left
draw1.rectangle([(30, 345), (410, 440)], fill=light_bg, outline=border_color)
draw1.text((50, 360), "5 Min Setup", fill=dark_slate, font=font_sub)
draw1.text((50, 395), "PDF / DOCX Direct Export", fill=emerald, font=font_regular)

img1.save('images/project_resume_builder.png', 'PNG')
print("Created live-matched images/project_resume_builder.png")


# ==========================================
# 2. TaleWeave — Interactive Web Story Platform
# ==========================================
img2 = Image.new('RGB', (W, H), white)
draw2 = ImageDraw.Draw(img2)
draw_window_header(draw2, "https://tehreem857.github.io/tale-weave")

# TaleWeave Header
draw2.rectangle([(0, 51), (W, 105)], fill=white)
draw2.line([(0, 105), (W, 105)], fill=border_color, width=1)
draw2.text((30, 66), "✒️ TaleWeave", fill=(88, 28, 135), font=font_serif)

# Nav items
draw2.text((420, 72), "Home", fill=purple_accent, font=font_small)
draw2.text((480, 72), "Stories", fill=dark_slate, font=font_small)
draw2.text((550, 72), "About", fill=dark_slate, font=font_small)
draw2.text((610, 72), "Contact", fill=dark_slate, font=font_small)
draw2.rectangle([(680, 65), (760, 95)], fill=(243, 232, 255), outline=purple_accent)
draw2.text((695, 72), "Admin", fill=purple_accent, font=font_small)

# Hero Tagline
draw2.rectangle([(30, 120), (770, 160)], fill=(250, 245, 255))
draw2.text((45, 130), "Original tales crafted with love and ink. Escape into cozy worlds, chapter by chapter.", fill=(88, 28, 135), font=font_regular)

# Story Cards Grid matching live TaleWeave
# Story 1
draw2.rectangle([(30, 180), (260, 440)], fill=white, outline=border_color)
draw2.rectangle([(30, 180), (260, 280)], fill=(238, 242, 255))
draw2.text((45, 220), "⚔️ Chronicles of Astra", fill=purple_accent, font=font_sub)
draw2.text((45, 295), "Fantasy / Adventure", fill=gold, font=font_small)
draw2.text((45, 320), "Chapter 14 Available", fill=dark_slate, font=font_regular)
draw2.rectangle([(45, 385), (245, 420)], fill=purple_accent)
draw2.text((85, 395), "Read Story →", fill=white, font=font_small)

# Story 2
draw2.rectangle([(285, 180), (515, 440)], fill=white, outline=border_color)
draw2.rectangle([(285, 180), (515, 280)], fill=(236, 253, 245))
draw2.text((300, 220), "🔍 Whispers in Fog", fill=emerald, font=font_sub)
draw2.text((300, 295), "Mystery / Fiction", fill=gold, font=font_small)
draw2.text((300, 320), "Interactive Branching", fill=dark_slate, font=font_regular)
draw2.rectangle([(300, 385), (500, 420)], fill=emerald)
draw2.text((340, 395), "Read Story →", fill=white, font=font_small)

# Story 3
draw2.rectangle([(540, 180), (770, 440)], fill=white, outline=border_color)
draw2.rectangle([(540, 180), (770, 280)], fill=(254, 243, 199))
draw2.text((555, 220), "☕ Cozy Cafe Tales", fill=(180, 83, 9), font=font_sub)
draw2.text((555, 295), "Slice of Life", fill=gold, font=font_small)
draw2.text((555, 320), "Cozy Audio Mode", fill=dark_slate, font=font_regular)
draw2.rectangle([(555, 385), (755, 420)], fill=gold)
draw2.text((595, 395), "Read Story →", fill=white, font=font_small)

img2.save('images/project_tale_weave.png', 'PNG')
print("Created live-matched images/project_tale_weave.png")


# ==========================================
# 3. AURÉLIE — Luxury Handmade Jewelry Store
# ==========================================
img3 = Image.new('RGB', (W, H), white)
draw3 = ImageDraw.Draw(img3)
draw_window_header(draw3, "https://tehreem857.github.io/jewelry-shop")

# Header matching live site
draw3.rectangle([(0, 51), (W, 105)], fill=white)
draw3.line([(0, 105), (W, 105)], fill=border_color, width=1)
draw3.text((30, 65), "AURÉLIE", fill=dark_slate, font=font_serif)
draw3.text((155, 74), "STUDIO", fill=gold, font=font_small)

# Nav items
draw3.text((520, 72), "Shop", fill=dark_slate, font=font_sub)
draw3.text((590, 72), "Manage", fill=(100, 116, 139), font=font_regular)
# Shopping Bag icon
draw3.rectangle([(680, 64), (770, 96)], fill=light_bg, outline=border_color)
draw3.text((695, 72), "🛒 Bag (3)", fill=emerald, font=font_small)

# Hero subtitle matching live site
draw3.text((30, 120), "HANDCRAFTED WITH INTENTION", fill=gold, font=font_small)
draw3.text((30, 142), "Timeless, Minimalist Jewelry", fill=dark_slate, font=font_title)

# Filter Bar matching live site
filters = ["All Pieces", "Rings", "Necklaces", "Earrings", "Bracelets"]
fx = 30
for i, f_name in enumerate(filters):
    fw = len(f_name) * 10 + 20
    bg = dark_slate if i == 0 else light_bg
    fg = white if i == 0 else dark_slate
    draw3.rectangle([(fx, 185), (fx + fw, 215)], fill=bg, outline=border_color)
    draw3.text((fx + 10, 193), f_name, fill=fg, font=font_small)
    fx += fw + 10

# Product Grid Cards
# Product 1
draw3.rectangle([(30, 235), (260, 440)], fill=white, outline=border_color)
draw3.rectangle([(40, 245), (250, 350)], fill=(254, 243, 199))
draw3.ellipse([(110, 260), (180, 330)], fill=white, outline=gold, width=4)
draw3.text((45, 365), "Solitaire Gold Ring", fill=dark_slate, font=font_sub)
draw3.text((45, 395), "$240.00", fill=gold, font=font_sub)
draw3.rectangle([(170, 390), (250, 425)], fill=emerald)
draw3.text((182, 400), "+ Add", fill=white, font=font_small)

# Product 2
draw3.rectangle([(285, 235), (515, 440)], fill=white, outline=border_color)
draw3.rectangle([(295, 245), (505, 350)], fill=(236, 253, 245))
draw3.ellipse([(365, 260), (435, 330)], fill=emerald, outline=white, width=3)
draw3.text((300, 365), "Emerald Drop Pendant", fill=dark_slate, font=font_sub)
draw3.text((300, 395), "$380.00", fill=emerald, font=font_sub)
draw3.rectangle([(425, 390), (505, 425)], fill=emerald)
draw3.text((437, 400), "+ Add", fill=white, font=font_small)

# Product 3
draw3.rectangle([(540, 235), (770, 440)], fill=white, outline=border_color)
draw3.rectangle([(550, 245), (760, 350)], fill=(241, 245, 249))
draw3.ellipse([(620, 260), (690, 330)], fill=dark_slate, outline=gold, width=3)
draw3.text((555, 365), "Pearl Sculpted Cuff", fill=dark_slate, font=font_sub)
draw3.text((555, 395), "$195.00", fill=dark_slate, font=font_sub)
draw3.rectangle([(680, 390), (760, 425)], fill=emerald)
draw3.text((692, 400), "+ Add", fill=white, font=font_small)

img3.save('images/project_jewelry_store.png', 'PNG')
print("Created live-matched images/project_jewelry_store.png")
