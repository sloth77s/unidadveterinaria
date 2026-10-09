# -*- coding: utf-8 -*-
with open('contacto-y-ubicacion.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with "Google Maps & Navigation" comment
target_line = -1
for i, line in enumerate(lines):
    if 'Google Maps & Navigation' in line:
        target_line = i
        break

print(f"Target line: {target_line}")
print(f"Content: {repr(lines[target_line])}")

# Insert before this line
new_lines = [
    '\n',
    '          <div class="mt-6 p-4 rounded-xl border border-brand-gold/30 bg-brand-royalBlue/10">\n',
    '            <h3 class="font-bold text-white mb-3 text-sm">Especialidades disponibles en esta sede</h3>\n',
    '            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">\n',
    '              <a href="/servicios/cardiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🫀 Cardiología</a>\n',
    '              <a href="/servicios/neurologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🧠 Neurología</a>\n',
    '              <a href="/servicios/oncologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🎗️ Oncología</a>\n',
    '              <a href="/servicios/radiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">📷 Radiología</a>\n',
    '              <a href="/servicios/medicina-interna-veterinaria" class="text-slate-300 hover:text-brand-gold">🩺 Medicina Interna</a>\n',
    '              <a href="/servicios/citopatologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🔬 Citopatología</a>\n',
    '            </div>\n',
    '          </div>\n',
    '\n',
    '\n'
]

lines[target_line:target_line] = new_lines

with open('contacto-y-ubicacion.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")