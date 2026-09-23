import os

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

for fname in all_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    issues = []
    patterns = [
        ('Ã¡', 'á'), ('Ã©', 'é'), ('Ã­', 'í'), ('Ã³', 'ó'), ('Ãº', 'ú'), ('Ã±', 'ñ'),
        ('Ã‰', 'É'), ('Ã"', 'Ó'), ('Ãš', 'Ú'), ('Ã', 'Á'), ('Ã', 'Í'),
        ('Ã¼', 'ü'), ('Ãœ', 'Ü'), ('Ã§', 'ç'), ('Ã‡', 'Ç'),
        ('Â¿', '¿'), ('Â¡', '¡'),
        ('â€¦', '…'),
        ('â€™', '’'),
        ('â€œ', '"'),
        ('â€', '"'),
        ('â€˜', '''),
        ('â€™', ''')
    ]
    issues = []
    for bad, good in [('Ã¡', 'á'), ('Ã©', 'é'), ('Ã­', 'í'), ('Ã³', 'ó'), ('Ãº', 'ú'), ('Ã±', 'ñ'),
                       ('Ã‰', 'É'), ('Ã"', 'Ó'), ('Ãš', 'Ú'), ('Ã', 'Á'), ('Ã', 'Í'),
                       ('Ã¼', 'ü'), ('Ãœ', 'Ü'), ('Ã§', 'ç'), ('Ã‡', 'Ç'),
                       ('Â¿', '¿'), ('Â¡', '¡'),
                       ('â€¦', '…'),
                       ('â€™', '’'),
                       ('â€œ', '"'), ('â€', '"'), ('â€˜', '''), ('â€™', ''')]:
        if bad in content:
            issues.append(bad + '->' + good)
    if issues:
        print(fname + ': ' + ', '.join(issues))

print("Done checking")