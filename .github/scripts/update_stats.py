import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
os.makedirs('assets', exist_ok=True)

targets = {
    'assets/github-stats.svg': 'https://github-stats-extended.vercel.app/api?username=themuhammedguler&show_icons=true&count_private=true&include_all_commits=true&theme=react&hide_border=true',
    'assets/top-langs.svg': 'https://github-stats-extended.vercel.app/api/top-langs/?username=themuhammedguler&layout=compact&langs_count=8&theme=react&hide_border=true',
    'assets/streak-stats.svg': 'https://streak-stats.demolab.com?user=themuhammedguler&theme=react&hide_border=true'
}

for filepath, url in targets.items():
    print(f"Fetching {filepath} from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            if resp.status == 200:
                content = resp.read()
                # Ensure the returned payload is valid SVG
                if b'<svg' in content and b'</svg>' in content:
                    with open(filepath, 'wb') as f:
                        f.write(content)
                    print(f"Successfully updated {filepath} ({len(content)} bytes)")
                else:
                    print(f"Skipping {filepath}: payload does not appear to be a valid SVG.")
            else:
                print(f"Skipping {filepath}: received HTTP {resp.status}")
    except Exception as e:
        print(f"Error fetching {filepath}: {e}. Keeping existing cached file.")
