import os
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 480

emerald = (16, 185, 129)       # #10B981
gold = (245, 158, 11)          # #F59E0B
dark_slate = (15, 23, 42)      # #0F172A
light_bg = (248, 250, 252)     # #F8FAFC
white = (255, 255, 255)
border_color = (226, 232, 240)  # #E2E8F0
text_muted = (100, 116, 139)

try:
    font_title = ImageFont.truetype('arialbd.ttf', 30)
    font_sub = ImageFont.truetype('arialbd.ttf', 20)
    font_regular = ImageFont.truetype('arial.ttf', 17)
    font_small = ImageFont.truetype('arial.ttf', 14)
except:
    font_title = font_sub = font_regular = font_small = ImageFont.load_default()

# ==========================================
# CARD 4: Simple Closebot AI Setup
# ==========================================
img4 = Image.new('RGB', (W, H), white)
draw4 = ImageDraw.Draw(img4)

# Subtle outer container
draw4.rectangle([(50, 40), (750, 440)], fill=white, outline=border_color, width=2)
# Top accent line
draw4.rectangle([(50, 40), (750, 48)], fill=emerald)

# Clean title & icon
draw4.text((90, 80), "🤖 Closebot AI Setup", fill=dark_slate, font=font_title)
draw4.text((90, 125), "Automated Lead Qualification & Website Chat Widget", fill=text_muted, font=font_regular)

# Simple clean message card inside
draw4.rectangle([(90, 175), (710, 310)], fill=light_bg, outline=(209, 250, 229), width=2)
draw4.text((120, 200), "Closebot Agent", fill=emerald, font=font_sub)
draw4.text((120, 240), "\"Hello! I can answer your questions, qualify your inquiry,", fill=dark_slate, font=font_regular)
draw4.text((120, 268), "and help you book a consultation right away.\"", fill=dark_slate, font=font_regular)

# Bottom clean pill
draw4.rectangle([(90, 345), (320, 395)], fill=(236, 253, 245), outline=emerald, width=1)
draw4.text((120, 360), "● 85% Qualification Rate", fill=(4, 120, 87), font=font_regular)

draw4.rectangle([(340, 345), (570, 395)], fill=(254, 243, 199), outline=gold, width=1)
draw4.text((370, 360), "⚡ 3.2x Booking Speed", fill=(180, 83, 9), font=font_regular)

img4.save('images/project_closebot_ai.png', 'PNG')
print("Created simple clean images/project_closebot_ai.png")


# ==========================================
# CARD 5: Simple GoHighLevel Sales Pipeline
# ==========================================
img5 = Image.new('RGB', (W, H), white)
draw5 = ImageDraw.Draw(img5)

# Outer container
draw5.rectangle([(50, 40), (750, 440)], fill=white, outline=border_color, width=2)
draw5.rectangle([(50, 40), (750, 48)], fill=emerald)

# Clean title
draw5.text((90, 80), "⚡ GoHighLevel Sales Pipeline", fill=dark_slate, font=font_title)
draw5.text((90, 125), "Automated CRM Lead Tracking & Stage Workflows", fill=text_muted, font=font_regular)

# Simple horizontal pipeline steps
steps = ["1. New Lead Inflow", "2. AI Qualification", "3. Appointment Booked"]
colors = [dark_slate, emerald, gold]

for idx, step_text in enumerate(steps):
    sy = 180 + idx * 75
    draw5.rectangle([(90, sy), (710, sy + 55)], fill=light_bg, outline=border_color, width=1)
    draw5.rectangle([(90, sy), (100, sy + 55)], fill=colors[idx])
    draw5.text((120, sy + 16), step_text, fill=colors[idx], font=font_sub)
    draw5.text((480, sy + 18), "Automated Trigger Active ✔", fill=text_muted, font=font_small)

img5.save('images/project_ghl_pipeline.png', 'PNG')
print("Created simple clean images/project_ghl_pipeline.png")


# ==========================================
# CARD 6: Simple Custom AI Support Assistant
# ==========================================
img6 = Image.new('RGB', (W, H), white)
draw6 = ImageDraw.Draw(img6)

# Outer container
draw6.rectangle([(50, 40), (750, 440)], fill=white, outline=border_color, width=2)
draw6.rectangle([(50, 40), (750, 48)], fill=emerald)

# Clean title
draw6.text((90, 80), "🧠 Custom AI Customer Support", fill=dark_slate, font=font_title)
draw6.text((90, 125), "24/7 Python & Vector DB Documentation Assistant", fill=text_muted, font=font_regular)

# Simple stats box
draw6.rectangle([(90, 180), (380, 390)], fill=(236, 253, 245), outline=emerald, width=2)
draw6.text((120, 210), "Support Deflection", fill=(4, 120, 87), font=font_regular)
draw6.text((120, 245), "78%", fill=emerald, font=font_title)
draw6.text((120, 310), "Instant Document Retrieval", fill=dark_slate, font=font_small)

draw6.rectangle([(420, 180), (710, 390)], fill=(254, 243, 199), outline=gold, width=2)
draw6.text((450, 210), "Response Time", fill=(180, 83, 9), font=font_regular)
draw6.text((450, 245), "< 0.9 Sec", fill=gold, font=font_title)
draw6.text((450, 310), "24/7 Continuous Operation", fill=dark_slate, font=font_small)

img6.save('images/project_ai_support.png', 'PNG')
print("Created simple clean images/project_ai_support.png")
