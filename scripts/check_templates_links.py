import os
import re

template_dir = r'c:\Users\admin\Documents\TrainPlex+500k\AI-Powered_Legal\templates'
link_buttons = []

for root, dirs, files in os.walk(template_dir):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, template_dir)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                links = re.findall(r'<a\s+[^>]*class=["\'][^"\']*btn[^"\']*["\'][^>]*>.*?</a>', content, re.DOTALL)
                for l in links:
                    clean_l = ' '.join(l.split())
                    link_buttons.append((rel, clean_l))

print(f"Total link buttons (<a class='btn...'>): {len(link_buttons)}")
unique_a_buttons = set(b[1] for b in link_buttons)
print(f"Unique link buttons: {len(unique_a_buttons)}")
for u in sorted(unique_a_buttons):
    print("A BUTTON:", u[:140])
