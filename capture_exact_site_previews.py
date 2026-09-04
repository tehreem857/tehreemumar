import os, time, subprocess
from PIL import Image

chrome_paths = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
]

browser = None
for p in chrome_paths:
    if os.path.exists(p):
        browser = p
        break

print(f"Using browser: {browser}")

sites = [
    {
        'url': 'https://tehreem857.github.io/resume-generator/',
        'output': os.path.abspath('images/project_resume_builder.png')
    },
    {
        'url': 'https://tehreem857.github.io/tale-weave/',
        'output': os.path.abspath('images/project_tale_weave.png')
    },
    {
        'url': 'https://tehreem857.github.io/jewelry-shop/',
        'output': os.path.abspath('images/project_jewelry_store.png')
    }
]

for s in sites:
    url = s['url']
    out_file = s['output']
    temp_file = out_file.replace('.png', '_raw.png')
    
    cmd = [
        browser,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--window-size=1280,800',
        '--hide-scrollbars',
        f'--screenshot={temp_file}',
        url
    ]
    print(f"Capturing exact landing screenshot for {url}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(temp_file):
        im = Image.open(temp_file)
        w, h = im.size
        print(f"Raw screenshot captured: {temp_file} ({w}x{h})")
        
        # Crop top landing viewport (1280 x 760) for a clean website preview
        cropped = im.crop((0, 0, 1280, min(h, 760)))
        cropped.save(out_file, 'PNG')
        print(f"Saved exact website preview to {out_file} ({cropped.size})")
        if os.path.exists(temp_file):
            os.remove(temp_file)
    else:
        print(f"Failed to capture screenshot for {url}: {res.stderr}")

print("Exact site preview screenshots captured successfully!")
