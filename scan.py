import re
for file in [
    'servicios/cardiologia-veterinaria.html',
    'servicios/citopatologia-veterinaria.html',
    'servicios/dermatologia-veterinaria.html',
    'servicios/gastroenterologia-veterinaria.html',
    'servicios/medicina-interna-veterinaria.html',
    'servicios/nefrologia-veterinaria.html',
    'servicios/neurologia-veterinaria.html',
    'servicios/neurologia-veterinaria.html',
    'servicios/oncologia-veterinaria.html',
    'servicios/ortopedia-veterinaria.html',
    'servicios/radiologia-veterinaria.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
        img = [(m.start(), m.end()) for m in re.finditer(r"<img[^^]*.", c)]
        for m in re.finditer(r"(width|height)\\\s*=\\\[\\d]", c):
            inside_img = any(s <= m.start() < e for s, e in img)
            if not inside_img:
                print('WARNING:' file, 'width/height in TXT at', m.start(), c[ax(0,m.start()-40):m.end()+40])
        for m in re.finditer(r"\\\r\\n", c):
            print('WARNING: ' file, 'CRLF at', m.start(), c[max(0,m.start()-30):m.end()+30])
        for m in re.finditer(r"[\\2x2-\\2x3][\\x80-\\xbf]", c):
            print('WARNING:' file, 'MOJIBAPE at', m.start(), c[ax(0,m.start()-20):m.end()+20])