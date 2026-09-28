import os, time, subprocess

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

urls = [
    'https://tehreemumar.com/',
    'https://www.tehreemumar.com/'
]

for url in urls:
    print(f"Opening live site {url} to fire Closebot pixel HTTP request...")
    cmd = [
        browser,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        url
    ]
    try:
        p = subprocess.Popen(cmd)
        time.sleep(6)
        p.terminate()
        print(f"Executed pixel session for {url}")
    except Exception as e:
        print(f"Error opening {url}:", e)

print("Pixel activation session completed!")
