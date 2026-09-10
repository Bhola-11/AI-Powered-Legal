import urllib.request, json, re

cred_path = r'C:\Users\admin\.git-credentials'
lines = open(cred_path, 'r', encoding='utf-8').read().splitlines()
m = re.search(r'https?://([^:]+):([^@]+)@', [l for l in lines if 'github.com' in l][0])
token = m.group(2)

url = 'https://api.github.com/repos/Bhola-11/AI-Powered-Legal/pulls?state=all'
req = urllib.request.Request(url, headers={'Authorization': f'token {token}', 'User-Agent': 'Python'})
with urllib.request.urlopen(req) as resp:
    prs = json.loads(resp.read().decode('utf-8'))
    print(f'Total PRs on GitHub: {len(prs)}')
    for p in prs[:8]:
        num = p['number']
        title = p['title']
        merged = bool(p.get('merged_at'))
        print(f"PR #{num}: {title} (merged={merged})")
