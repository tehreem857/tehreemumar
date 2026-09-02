import os
from PIL import Image, ImageDraw, ImageFont

# Set up canvas size 800x480
W, H = 800, 480

emerald = (16, 185, 129)      # #10B981
gold = (245, 158, 11)         # #F59E0B
dark_slate = (15, 23, 42)     # #0F172A
light_bg = (248, 250, 252)    # #F8FAFC
white = (255, 255, 255)
border_color = (226, 232, 240) # #E2E8F0

try:
    font_title = ImageFont.truetype('arialbd.ttf', 32)
    font_bold = ImageFont.truetype('arialbd.ttf', 22)
    font_regular = ImageFont.truetype('arial.ttf', 18)
    font_small = ImageFont.truetype('arial.ttf', 15)
except:
    font_title = font_bold = font_regular = font_small = ImageFont.load_default()

def draw_window_header(draw, title_text):
    # Draw browser / app window top bar
    draw.rectangle([(0, 0), (W, H)], fill=light_bg)
    draw.rectangle([(0, 0), (W, 55)], fill=white)
    draw.line([(0, 55), (W, 55)], fill=border_color, width=2)
    
    # Window buttons (red, yellow, green)
    draw.ellipse([(20, 20), (32, 32)], fill=(239, 68, 68))
    draw.ellipse([(42, 20), (54, 32)], fill=(245, 158, 11))
    draw.ellipse([(64, 20), (76, 32)], fill=(16, 185, 129))
    
    # Window title address bar
    draw.rectangle([(120, 14), (680, 40)], fill=light_bg, outline=border_color, width=1)
    draw.text((140, 19), title_text, fill=(100, 116, 139), font=font_small)

# --- 1. Closebot AI Chatbot Setup ---
img1 = Image.new('RGB', (W, H), white)
draw1 = ImageDraw.Draw(img1)
draw_window_header(draw1, "https://tehreemumar.com/closebot-ai-system")

# Sidebar
draw1.rectangle([(20, 75), (240, 450)], fill=white, outline=border_color)
draw1.text((40, 95), "Closebot AI", fill=emerald, font=font_bold)
draw1.rectangle([(40, 140), (220, 175)], fill=(236, 253, 245), outline=emerald)
draw1.text((55, 148), "● Active Agent", fill=emerald, font=font_small)

# Chat Area
draw1.rectangle([(260, 75), (780, 450)], fill=white, outline=border_color)
# User message bubble
draw1.rectangle([(450, 110), (750, 160)], fill=(241, 245, 249))
draw1.text((465, 125), "Can you qualify leads automatically?", fill=dark_slate, font=font_regular)
# Bot response bubble
draw1.rectangle([(290, 180), (680, 260)], fill=emerald)
draw1.text((310, 195), "Yes! I filter inquiries, capture details,", fill=white, font=font_regular)
draw1.text((310, 222), "and sync qualified leads to GHL CRM.", fill=white, font=font_regular)

# Metrics card
draw1.rectangle([(290, 280), (520, 420)], fill=(254, 243, 199), outline=gold)
draw1.text((310, 300), "QUALIFICATION", fill=(180, 83, 9), font=font_small)
draw1.text((310, 330), "85% FASTER", fill=gold, font=font_title)
draw1.text((310, 375), "Automated Booking", fill=dark_slate, font=font_small)

draw1.rectangle([(540, 280), (750, 420)], fill=(236, 253, 245), outline=emerald)
draw1.text((560, 300), "CONVERSION", fill=(4, 120, 87), font=font_small)
draw1.text((560, 330), "3.2X UP", fill=emerald, font=font_title)
draw1.text((560, 375), "Live GHL Sync", fill=dark_slate, font=font_small)

img1.save('images/project_closebot_ai.png', 'PNG')
print("Created images/project_closebot_ai.png")

# --- 2. GoHighLevel Sales Pipeline ---
img2 = Image.new('RGB', (W, H), white)
draw2 = ImageDraw.Draw(img2)
draw_window_header(draw2, "https://tehreemumar.com/ghl-pipeline-automation")

# Kanban columns
col_w = 230
spacing = 20
cols = ["New Lead", "AI Qualified", "Booked Call"]
cols_color = [dark_slate, emerald, gold]

for idx, col in enumerate(cols):
    cx = 30 + idx * (col_w + spacing)
    draw2.rectangle([(cx, 80), (cx + col_w, 450)], fill=light_bg, outline=border_color)
    draw2.rectangle([(cx, 80), (cx + col_w, 125)], fill=cols_color[idx])
    draw2.text((cx + 15, 95), col, fill=white, font=font_bold)
    
    # Cards in column
    draw2.rectangle([(cx + 15, 145), (cx + col_w - 15, 260)], fill=white, outline=border_color)
    draw2.text((cx + 30, 165), f"Contact #{idx*2 + 101}", fill=dark_slate, font=font_bold)
    draw2.text((cx + 30, 195), "SMS Follow-up Active", fill=(100, 116, 139), font=font_small)
    draw2.rectangle([(cx + 30, 220), (cx + 140, 245)], fill=(236, 253, 245))
    draw2.text((cx + 40, 225), "Stage Updated", fill=emerald, font=font_small)

img2.save('images/project_ghl_pipeline.png', 'PNG')
print("Created images/project_ghl_pipeline.png")

# --- 3. Custom AI Support Assistant ---
img3 = Image.new('RGB', (W, H), white)
draw3 = ImageDraw.Draw(img3)
draw_window_header(draw3, "https://tehreemumar.com/ai-support-assistant")

draw3.rectangle([(40, 85), (760, 440)], fill=white, outline=border_color)
draw3.text((70, 110), "AI Support Resolution Hub", fill=dark_slate, font=font_title)

# Stats row
draw3.rectangle([(70, 170), (270, 290)], fill=(236, 253, 245), outline=emerald)
draw3.text((90, 190), "Resolution Rate", fill=(4, 120, 87), font=font_small)
draw3.text((90, 220), "99.4%", fill=emerald, font=font_title)

draw3.rectangle([(300, 170), (500, 290)], fill=(254, 243, 199), outline=gold)
draw3.text((320, 190), "Avg Response Time", fill=(180, 83, 9), font=font_small)
draw3.text((320, 220), "< 2 Sec", fill=gold, font=font_title)

draw3.rectangle([(530, 170), (730, 290)], fill=light_bg, outline=border_color)
draw3.text((550, 190), "24/7 Availability", fill=(100, 116, 139), font=font_small)
draw3.text((550, 220), "100%", fill=dark_slate, font=font_title)

img3.save('images/project_ai_support.png', 'PNG')
print("Created images/project_ai_support.png")

# --- 4. Smart AI Resume & ATS Optimizer ---
img4 = Image.new('RGB', (W, H), white)
draw4 = ImageDraw.Draw(img4)
draw_window_header(draw4, "https://tehreem857.github.io/resume-generator")

draw4.rectangle([(40, 80), (450, 440)], fill=white, outline=border_color)
draw4.text((60, 105), "AI Resume Builder", fill=dark_slate, font=font_title)
draw4.text((60, 150), "● Real-time ATS Score Optimization", fill=emerald, font=font_regular)
draw4.rectangle([(60, 200), (410, 260)], fill=emerald)
draw4.text((120, 218), "ATS Match Score: 98/100", fill=white, font=font_bold)

draw4.rectangle([(480, 80), (760, 440)], fill=light_bg, outline=border_color)
draw4.rectangle([(510, 110), (730, 410)], fill=white, outline=border_color)
draw4.text((530, 130), "RESUME PREVIEW", fill=gold, font=font_bold)
draw4.line([(530, 160), (710, 160)], fill=border_color, width=2)
draw4.rectangle([(530, 180), (690, 195)], fill=(226, 232, 240))
draw4.rectangle([(530, 210), (650, 225)], fill=(226, 232, 240))

img4.save('images/project_resume_builder.png', 'PNG')
print("Created images/project_resume_builder.png")

# --- 5. TaleWeave Interactive Story Platform ---
img5 = Image.new('RGB', (W, H), white)
draw5 = ImageDraw.Draw(img5)
draw_window_header(draw5, "https://tehreem857.github.io/tale-weave")

draw5.rectangle([(40, 85), (760, 440)], fill=white, outline=border_color)
draw5.text((70, 110), "TaleWeave - Interactive Web Stories", fill=dark_slate, font=font_title)

# Card Grid
draw5.rectangle([(70, 170), (380, 400)], fill=(236, 253, 245), outline=emerald)
draw5.text((90, 190), "Interactive Web App", fill=emerald, font=font_bold)
draw5.text((90, 230), "Custom choice branching", fill=dark_slate, font=font_regular)

draw5.rectangle([(410, 170), (720, 400)], fill=(254, 243, 199), outline=gold)
draw5.text((430, 190), "High Engagement SPA", fill=gold, font=font_bold)
draw5.text((430, 230), "Fast dynamic loading", fill=dark_slate, font=font_regular)

img5.save('images/project_tale_weave.png', 'PNG')
print("Created images/project_tale_weave.png")

# --- 6. Luxury Handmade Jewelry Web Store ---
img6 = Image.new('RGB', (W, H), white)
draw6 = ImageDraw.Draw(img6)
draw_window_header(draw6, "https://tehreem857.github.io/jewelry-shop")

draw6.rectangle([(40, 85), (760, 440)], fill=white, outline=border_color)
draw6.text((70, 110), "AURÉLIE - Luxury Jewelry Store", fill=dark_slate, font=font_title)

draw6.rectangle([(70, 170), (280, 410)], fill=light_bg, outline=border_color)
draw6.rectangle([(90, 190), (260, 310)], fill=(254, 243, 199), outline=gold)
draw6.text((105, 330), "Fine Gold Ring", fill=dark_slate, font=font_bold)
draw6.text((105, 360), "$240.00", fill=gold, font=font_bold)

draw6.rectangle([(310, 170), (520, 410)], fill=light_bg, outline=border_color)
draw6.rectangle([(330, 190), (500, 310)], fill=(236, 253, 245), outline=emerald)
draw6.text((345, 330), "Emerald Pendant", fill=dark_slate, font=font_bold)
draw6.text((345, 360), "$380.00", fill=emerald, font=font_bold)

draw6.rectangle([(550, 170), (730, 270)], fill=emerald)
draw6.text((570, 200), "+38% Mobile", fill=white, font=font_bold)
draw6.text((570, 230), "Checkout Conversion", fill=white, font=font_small)

img6.save('images/project_jewelry_store.png', 'PNG')
print("Created images/project_jewelry_store.png")
