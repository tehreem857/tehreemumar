import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Download Google Signature Font 'DancingScript-Medium.ttf' or 'AlexBrush-Regular.ttf'
font_url = "https://raw.githubusercontent.com/google/fonts/main/ofl/alexbrush/AlexBrush-Regular.ttf"
font_path = "AlexBrush-Regular.ttf"

if not os.path.exists(font_path):
    print("Downloading Alex Brush signature font...")
    urllib.request.urlretrieve(font_url, font_path)

font_url_2 = "https://raw.githubusercontent.com/google/fonts/main/ofl/dancingscript/DancingScript-Bold.ttf"
font_path_2 = "DancingScript-Bold.ttf"

if not os.path.exists(font_path_2):
    print("Downloading Dancing Script signature font...")
    urllib.request.urlretrieve(font_url_2, font_path_2)

# Open Option A robot image
img_orig = Image.open(r'C:\Users\User\.gemini\antigravity\brain\ac5b52c7-ef26-4b6d-ab79-4dd60a16f513\neon_pencil_robot_logo_a_1788323620463.jpg')
w, h = img_orig.size

# Crop ONLY the neon pencil robot head icon on the left
robot_crop = img_orig.crop((int(w * 0.08), int(h * 0.15), int(w * 0.42), int(h * 0.85)))

# Convert white bg of robot crop to transparent
robot_rgba = robot_crop.convert('RGBA')
arr = np.array(robot_rgba)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
white_bg = (r > 240) & (g > 240) & (b > 240)
arr[:,:,3][white_bg] = 0
robot_transparent = Image.fromarray(arr)

# Resize robot icon to 320x320
robot_transparent = robot_transparent.resize((320, 320), Image.Resampling.LANCZOS)

# Palette
emerald = (16, 185, 129, 255)
gold = (245, 158, 11, 255)

# --- CONCEPT 1: Alex Brush Signature Font ---
c1 = Image.new('RGBA', (1400, 480), (255, 255, 255, 255))
c1.paste(robot_transparent, (50, 80), robot_transparent)
draw1 = ImageDraw.Draw(c1)

font_signature1 = ImageFont.truetype(font_path, 150)

draw1.text((410, 140), "Tehreem Umar", fill=emerald, font=font_signature1)

out1 = r'C:\Users\User\.gemini\antigravity\brain\ac5b52c7-ef26-4b6d-ab79-4dd60a16f513\signature_logo_option_1.png'
c1.save(out1)
print("Saved Signature Option 1:", out1)

# --- CONCEPT 2: Dancing Script Signature Font ---
c2 = Image.new('RGBA', (1400, 480), (255, 255, 255, 255))
c2.paste(robot_transparent, (50, 80), robot_transparent)
draw2 = ImageDraw.Draw(c2)

font_signature2 = ImageFont.truetype(font_path_2, 130)
draw2.text((410, 160), "Tehreem Umar", fill=emerald, font=font_signature2)

out2 = r'C:\Users\User\.gemini\antigravity\brain\ac5b52c7-ef26-4b6d-ab79-4dd60a16f513\signature_logo_option_2.png'
c2.save(out2)
print("Saved Signature Option 2:", out2)
