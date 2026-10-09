# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the encoding of "Ubicación de la Clínica" and fix the new link format
old_lines = [
    '          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">',
    '',
    '            Ubicación de la Cl�\xadnica',
    '',
    '          </a>',
    '          <a href=#especialidades class=w-full',
    '',
    '        </div>'
]

new_lines = [
    '          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">',
    '',
    '            Ubicación de la Clínica',
    '',
    '          </a>',
    '          <a href="#especialidades" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">',
    '',
    '            Ver Especialidades',
    '',
    '          </a>',
    '        </div>'
]

old_block = '\n'.join(old_lines)
new_block = '\n'.join(new_lines)

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Block not found, trying alternative...")
    # Try with the actual characters
    alt_old = old_block.replace('Ubicación de la Cl�\xadnica', 'Ubicación de la Clínica')
    if alt_old in content:
        content = content.replace(alt_old, new_block)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed with alt!")
    else:
        print("Still not found")
        # Show what we have
        idx = content.find('Ubicación de la Cl')
        if idx >= 0:
            print(f"Found at {idx}: {repr(content[idx:idx+100])}")