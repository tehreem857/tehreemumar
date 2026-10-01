import os, re, glob

html_files = [f for f in glob.glob('**/*.html', recursive=True) if 'google' not in f and '.system_generated' not in f]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove WhatsApp footer <li> link (entire line)
    content = re.sub(
        r'\s*<li><a href="https://wa\.me/923369197296"[^>]*>WhatsApp</a></li>',
        '',
        content,
        flags=re.IGNORECASE
    )

    # 2. Remove telephone from JSON-LD schema
    content = re.sub(
        r'\s*"telephone":\s*"\+923369197296",?\n?',
        '\n',
        content,
        flags=re.IGNORECASE
    )

    # 3. Remove entire WhatsApp contact card block on contact.html
    content = re.sub(
        r'<!--\s*WhatsApp Contact Method\s*-->.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

print("\nAll WhatsApp references and phone numbers removed!")
