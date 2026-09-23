with open('robots.txt', 'rb') as f:
    raw = f.read()
decoded = raw.decode('utf-8-sig')

replacements = {
    'ConfiguraciÃ³n': 'Configuración',
    'pÃ¡ginas': 'páginas',
    'permitimos': 'permitimos',
    'pÃ¡ginas': 'páginas',
    'tienen': 'tienen',
    'contenido': 'contenido',
    'No': 'No',
    'bloquear': 'bloquear',
    'recursos': 'recursos',
    'estÃ¡ticos': 'estáticos',
    'preferido': 'preferido'
}

fixed = decoded
for bad, good in replacements.items():
    fixed = fixed.replace(bad, good)

with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(fixed)

print('Fixed robots.txt')