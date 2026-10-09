# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact pattern
import re
# Look for the anchor link pattern
pattern = r'(<a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3\.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">\s*Ubicación de la Clínica\s*</a>\s*</div>)'

match = re.search(pattern, content)
if match:
    print("Found with regex!")
    print(repr(match.group(0)[:200]))
else:
    print("Not found with regex either")
    # Show context around line 518
    lines = content.split('\n')
    for i, line in enumerate(lines[515:525], 516):
        print(f"{i}: {repr(line)}")