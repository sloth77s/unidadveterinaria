# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 520 (encoding) and line 523 (new link format)
# Line 520: '            Ubicación de la Cl�\xadnica\n' -> '            Ubicación de la Clínica\n'
# Line 523: '          <a href=#especialidades class=w-full\n' -> proper format

# Fix encoding on line 520 (0-indexed: 519)
if 'Cl�\xadnica' in lines[519]:
    lines[519] = lines[519].replace('Cl�\xadnica', 'Clínica')
    print(f"Fixed line 520 encoding")

# Fix line 523 (0-indexed: 522)
if '<a href=#especialidades class=w-full' in lines[522]:
    lines[522] = '          <a href="#especialidades" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">\n'
    print(f"Fixed line 523 format")
    # Need to add the text and closing tag
    # Insert after line 522
    lines.insert(523, '            Ver Especialidades\n')
    lines.insert(524, '          </a>\n')
    print(f"Added link text and closing tag")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")