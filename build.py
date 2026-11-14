#!/usr/bin/env python3
"""Builds the GitHub Pages bundle and the artifact page from src/game.html."""
import json, os, re
from PIL import Image, ImageDraw

NAME, SLUG, DESC, THEME = 'Minigolf', 'minigolf', 'Minigolf til mobil og browser', '#12352b'
ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, 'src/game.html'), encoding='utf-8').read()
SND = open(os.path.join(ROOT, 'src/snd.js'), encoding='utf-8').read()
src = src.replace('<script>/*SND*/</script>', '<script>' + SND + '</script>', 1)   # the recordings live in src/snd.js and are inlined: one self-contained page
VERSION = re.search(r"VERSION='(v[0-9.]+)'", src).group(1)  # single source: the game's VERSION constant
src = re.sub(r'<title>.*?</title>', f'<title>{NAME} {VERSION}</title>', src, count=1)

VIEWPORT = '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">'
i = src.index('</style>') + len('</style>')
head_part, body_part = src[:i], src[i:]

def page(extra_head):
    return ('<!DOCTYPE html>\n<html lang="da">\n<head>\n<meta charset="utf-8">\n' + VIEWPORT + '\n' + extra_head +
            head_part + '\n</head>\n<body>\n' + body_part + '\n</body>\n</html>\n')

# --- GitHub Pages version (index.html + a named copy of every release)
gh = page(f'''<meta name="theme-color" content="{THEME}">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{NAME}">
<meta name="description" content="{NAME} – {DESC} ({VERSION})">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
''')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(gh)
os.makedirs(os.path.join(ROOT, 'versions'), exist_ok=True)
open(os.path.join(ROOT, 'versions', f'{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(gh)

# --- artifact version (self-contained page, no manifest or icon files)
os.makedirs(os.path.join(ROOT, 'artifact'), exist_ok=True)
open(os.path.join(ROOT, 'artifact', f'{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(page(''))

manifest = {
    "name": NAME, "short_name": NAME, "description": DESC,
    "start_url": "./", "scope": "./", "display": "fullscreen", "orientation": "portrait",
    "background_color": THEME, "theme_color": THEME, "lang": "da",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
json.dump(manifest, open(os.path.join(ROOT, 'manifest.webmanifest'), 'w'), indent=2)
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')

def icon(n):
    s = 4 * n
    im = Image.new('RGB', (s, s), THEME)
    d = ImageDraw.Draw(im)
    m = s * .16
    d.rounded_rectangle([m - s*.03, m - s*.03, s - m + s*.03, s - m + s*.03], radius=s*.1, fill='#c08a49')
    d.rounded_rectangle([m, m, s - m, s - m], radius=s*.07, fill='#3aa655')
    r = s * .075
    cx, cy = s * .64, s * .36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill='#0d1f17')
    w = max(2, s // 60)
    d.line([(cx, cy), (cx, cy - s*.2)], fill='#f4f4f4', width=w)
    d.polygon([(cx, cy - s*.2), (cx + s*.13, cy - s*.15), (cx, cy - s*.1)], fill='#e8452c')
    r = s * .07
    bx, by = s * .36, s * .66
    d.ellipse([bx - r, by - r, bx + r, by + r], fill='#ffffff')
    return im.resize((n, n), Image.LANCZOS)

icon(192).save(os.path.join(ROOT, 'icon-192.png'))
icon(512).save(os.path.join(ROOT, 'icon-512.png'))
icon(180).save(os.path.join(ROOT, 'apple-touch-icon.png'))
print('built', NAME, VERSION)
