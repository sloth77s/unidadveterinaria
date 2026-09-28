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

print('=== CHECKING LINKS FOR .html EXTENSIONS ===')
for fname in all_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'href="([^"]*\.html)"', content)
    if matches:
        print(f'{fname}:')
        for m in matches:
            print(f'  {m}')