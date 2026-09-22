import os
for fname in ['aviso-legal.html', 'politica-de-privacidad.html', 'politica-de-cookies.html']:
    path = f'unidad-veterinaria-david-aguilar/{fname}'
    with open(path, 'rb') as f:
        raw = f.read(100)
        has_bom = raw.startswith(b'\xef\xbb\xbf')
        print(f'{fname}: has_bom={has_bom}, starts={raw[:20]}')