# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<div class="mt-12 text-center bg-brand-royalBlue/20')
segment = content[idx-50:idx+300]
print(repr(segment))