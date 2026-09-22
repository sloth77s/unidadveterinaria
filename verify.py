import os
import re

all_files = [
    'index.html',
    'aviso-legal.html',
    'politica-de-privacidad.html',
    'politica-de-cookies.html',
    'contacto-y-ubicacion.html',
    'preguntas-frecuentes.html',
]

for fname in os.listdir('servicios'):
    if fname.endswith('.html'):
        all_files.append('servicios/' + fname)

print('=== FINAL VERIFICATION ===')
all_ok = True
for fname in all_files:
    with open(fname, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    has_html_in_href = bool(re.search(r'href="[^"]*\.html"', content))
    has_com = 'unidadveterinaria.com' in content and 'pages.dev' not in content
    has_meta = '<meta charset="UTF-8">' in content
    has_accents = any(c in content for c in ['á', 'é', 'í', 'ó', 'ú', 'ñ'])
    has_mojibake = 'Ã' in content
    
    issues = []
    if has_html_in_href:
        issues.append('.html in href')
    if has_com:
        issues.append('.com domain without pages.dev')
    if has_mojibake:
        issues.append('mojibake')
    if not has_accents:
        issues.append('no accents')
    if not has_meta:
        issues.append('missing meta charset')
    
    if issues:
        print(f'{fname}: ISSUES - {issues}')
        all_ok = False
    else:
        print(f'{fname}: OK')

print()
if all_ok:
    print('=== ALL CLEAN ===')
else:
    print('=== ISSUES FOUND ===')