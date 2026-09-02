import os, re
from PIL import Image, ImageDraw, ImageFont
import numpy as np

print("--- CREATING APPROVED LOGO ASSETS ---")

# 1. Load the approved cute robot logo image
orig_img = Image.open(r'C:\Users\User\.gemini\antigravity\brain\ac5b52c7-ef26-4b6d-ab79-4dd60a16f513\cute_robot_signature_style2.png')

# Crop tight bounding box around the logo content
img_rgba = orig_img.convert('RGBA')
arr = np.array(img_rgba)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# Non-white pixels (where r<250 or g<250 or b<250)
non_white = (r < 240) | (g < 240) | (b < 240)
# Make white pixels fully transparent
arr[:,:,3][~non_white] = 0
transparent_logo = Image.fromarray(arr)

# Get bounding box of visible content
bbox = transparent_logo.getbbox()
if bbox:
    transparent_logo = transparent_logo.crop(bbox)

# Add small padding (15px around)
padded_w = transparent_logo.width + 30
padded_h = transparent_logo.height + 30
final_logo = Image.new('RGBA', (padded_w, padded_h), (255, 255, 255, 0))
final_logo.paste(transparent_logo, (15, 15), transparent_logo)

# Save main logo asset
logo_path = 'images/tehreem_logo.png'
final_logo.save(logo_path, 'PNG')
print(f"Saved logo asset to {logo_path} (Size: {final_logo.size})")

# Also save transparent version logo_transparent.png
final_logo.save('images/logo_transparent.png', 'PNG')
final_logo.save('images/logo.png', 'PNG')

# Create square favicon from the robot icon
robot_crop = orig_img.crop((int(orig_img.width * 0.04), int(orig_img.height * 0.12), int(orig_img.width * 0.28), int(orig_img.height * 0.88)))
robot_arr = np.array(robot_crop.convert('RGBA'))
r, g, b, a = robot_arr[:,:,0], robot_arr[:,:,1], robot_arr[:,:,2], robot_arr[:,:,3]
robot_arr[:,:,3][(r > 240) & (g > 240) & (b > 240)] = 0
favicon_img = Image.fromarray(robot_arr)

# Square canvas 128x128
fav_square = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
fav_cropped = favicon_img.crop(favicon_img.getbbox()) if favicon_img.getbbox() else favicon_img
fav_cropped.thumbnail((110, 110), Image.Resampling.LANCZOS)
offset_x = (128 - fav_cropped.width) // 2
offset_y = (128 - fav_cropped.height) // 2
fav_square.paste(fav_cropped, (offset_x, offset_y), fav_cropped)
fav_square.save('favicon.png', 'PNG')
print("Saved favicon.png")

# 2. Update CSS for optimal logo sizing
css_path = 'css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Ensure .brand-logo-img has balanced, proportional height
logo_css_rule = """
.brand-logo-img {
  height: 48px;
  width: auto;
  max-width: 240px;
  display: block;
  object-fit: contain;
  transition: transform 0.3s ease;
}
.brand-logo-img:hover {
  transform: scale(1.03);
}
@media (max-width: 640px) {
  .brand-logo-img {
    height: 40px;
    max-width: 190px;
  }
}
"""

if '.brand-logo-img' in css:
    css = re.sub(r'\.brand-logo-img\s*\{[^}]*\}', logo_css_rule.strip(), css, flags=re.DOTALL)
else:
    css += "\n" + logo_css_rule

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated logo sizing CSS in styles.css!")

# 3. Update all HTML files with cache buster v=15.0
root_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('google')]
blog_dir = 'blog'
blog_files = [os.path.join(blog_dir, f) for f in os.listdir(blog_dir) if f.endswith('.html')] if os.path.exists(blog_dir) else []
all_htmls = root_files + blog_files

for filepath in all_htmls:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_blog = filepath.startswith('blog/')
    
    # Bump logo img src cache busters
    if is_blog:
        content = re.sub(r'src="[^"]*tehreem_logo\.png[^"]*"', 'src="../images/tehreem_logo.png?v=15.0"', content)
        content = re.sub(r'href="[^"]*favicon\.png[^"]*"', 'href="../favicon.png?v=15.0"', content)
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="../css/styles.css?v=15.0"', content)
    else:
        content = re.sub(r'src="[^"]*tehreem_logo\.png[^"]*"', 'src="images/tehreem_logo.png?v=15.0"', content)
        content = re.sub(r'href="[^"]*favicon\.png[^"]*"', 'href="favicon.png?v=15.0"', content)
        content = re.sub(r'href="[^"]*styles\.css[^"]*"', 'href="css/styles.css?v=15.0"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated cache-busting parameters across {len(all_htmls)} HTML files!")
