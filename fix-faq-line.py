# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines 369-380 (0-indexed: 368-379)
# We'll replace lines 368-380 (13 lines) with new content

old_lines = lines[368:381]  # 13 lines
print("Old lines:")
for i, line in enumerate(old_lines):
    print(f"{368+i}: {repr(line.rstrip())}")

# New lines to insert
new_lines = [
    '          </div>\n',
    '\n',
    '        </div>\n',
    '\n',
    '\n',
    '\n',
    '      </div>\n',
    '\n',
    '\n',
    '\n',
    '      <div class="mt-8 p-5 rounded-2xl border border-brand-gold/30 bg-brand-royalBlue/10">\n',
    '        <h3 class="font-bold text-white mb-3 text-sm">�Necesita una especialidad espec�fica?</h3>\n',
    '        <div class="grid grid-cols-2 gap-2 text-xs">\n',
    '          <a href="/servicios/cardiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🫀 Cardiología</a>\n',
    '          <a href="/servicios/neurologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🧠 Neurología</a>\n',
    '          <a href="/servicios/oncologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🎗️ Oncología</a>\n',
    '          <a href="/servicios/citopatologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🔬 Citopatología</a>\n',
    '          <a href="/servicios/radiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">📷 Radiología</a>\n',
    '          <a href="/servicios/medicina-interna-veterinaria" class="text-slate-300 hover:text-brand-gold">🩺 Medicina Interna</a>\n',
    '        </div>\n',
    '      </div>\n',
    '\n',
    '\n',
    '\n',
    '\n',
    '      <div class="mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">\n',
    '\n',
    '        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>\n'
]

# Replace
lines[368:381] = new_lines

with open('preguntas-frecuentes.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")