# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact location
idx = content.find('mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">\n\n        <h2 class="text-base font-bold text-white">')
print(f"Found at {idx}")
print(repr(content[idx:idx+300]))