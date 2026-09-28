import os
import re

all_files = [
    'index.html',
    'aviso-legal.html',
    'contacto-y-ubicacion.html',
    'politica-de-cookies.html',
    'politica-de-privacidad.html',
    'preguntas-frecuentes.html',
]

for fname in os.listdir('servicios'):
    if fname.endswith('.html'):
        all_files.append('servicios/' + fname)

print('=== CHECKING CANONICAL URLs ===')
for fname in all_files:
    with open(fname, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    m = re.search(r'canonical.*href=["\']([^"\']+)', content)
    if m:
        url = m.group(1)
        if 'unidadveterinaria.com' in url and 'pages.dev' not in url:
            print(f'ISSUE: {fname} has old domain in canonical: {url}')
        elif 'pages.dev' in url:
            print(f'OK: {fname} -> {url}')
        else:
            print(f'CHECK: {fname} -> {url}')
    else:
        print(f'NO CANONICAL: {fname}')

# Check _redirects
print()
print('=== REDIRECTS CHECK ===')
with open('_redirects', 'r') as f:
    content = f.read()
if '/servicios/ /servicios/ 200' in content:
    print('WARNING: Found /servicios/ /servicios/ 200 - redirect loop!')
if '/* /index.html 200' in content:
    print('WARNING: Catch-all redirect /* /index.html 200 found')
if '/servicios/* /servicios/:splat 301' in content:
    print('WARNING: /servicios/* catch-all redirect found')
else:
    print('_redirects: OK - no redirect loops detected')