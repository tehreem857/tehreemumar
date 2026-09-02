import os
from PIL import Image

screenshots = {
    'images/project_resume_builder.png': (1280, 750),
    'images/project_tale_weave.png': (1280, 750),
    'images/project_jewelry_store.png': (1280, 750)
}

for img_path, crop_box in screenshots.items():
    if os.path.exists(img_path):
        im = Image.open(img_path)
        w, h = im.size
        # Crop upper region of page (top header & hero)
        cropped = im.crop((0, 0, w, min(h, 750)))
        # Resize to clean 800x480 thumbnail
        thumbnail = cropped.resize((800, 480), Image.Resampling.LANCZOS)
        thumbnail.save(img_path, 'PNG')
        print(f"Processed real live screenshot for {img_path} (Final Size: {thumbnail.size})")

print("All real live website screenshots processed successfully!")
