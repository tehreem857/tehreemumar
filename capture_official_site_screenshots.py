import os, subprocess
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
        'url': 'https://www.closebot.com/',
        'output': os.path.abspath('images/project_closebot_ai.png')
    },
    {
        'url': 'https://www.gohighlevel.com/',
        'output': os.path.abspath('images/project_ghl_pipeline.png')
    },
    {
        'url': 'https://openai.com/',
        'output': os.path.abspath('images/project_ai_support.png')
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
    print(f"Capturing exact live screenshot of {url}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    
    if os.path.exists(temp_file):
        im = Image.open(temp_file)
        w, h = im.size
        print(f"Raw screenshot captured: {temp_file} ({w}x{h})")
        
        # Crop top landing viewport (1280 x 760) for a clean preview
        cropped = im.crop((0, 0, 1280, min(h, 760)))
        cropped.save(out_file, 'PNG')
        print(f"Saved exact website preview to {out_file} ({cropped.size})")
        if os.path.exists(temp_file):
            os.remove(temp_file)
    else:
        print(f"Failed to capture screenshot for {url}: {res.stderr}")

print("Official site screenshots captured successfully!")
