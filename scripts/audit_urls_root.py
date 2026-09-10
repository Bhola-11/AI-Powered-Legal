import os

for app in sorted(os.listdir('apps')):
    u = os.path.join('apps', app, 'urls.py')
    if os.path.exists(u):
        with open(u, 'r', encoding='utf-8') as f:
            c = f.read()
            has_root = "path(''," in c or 'path("",' in c
            print(f"{app:20}: has_root={has_root}")
