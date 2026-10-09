# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Use the exact string from file (with � for special chars)
old = '''      </div>


      <div class="mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">

        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>'''

new = '''      </div>


      <div class="mt-8 p-5 rounded-2xl border border-brand-gold/30 bg-brand-royalBlue/10">
        <h3 class="font-bold text-white mb-3 text-sm">�Necesita una especialidad espec�fica?</h3>
        <div class="grid grid-cols-2 gap-2 text-xs">
          <a href="/servicios/cardiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🫀 Cardiología</a>
          <a href="/servicios/neurologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🧠 Neurología</a>
          <a href="/servicios/oncologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🎗️ Oncología</a>
          <a href="/servicios/citopatologia-veterinaria" class="text-slate-300 hover:text-brand-gold">🔬 Citopatología</a>
          <a href="/servicios/radiologia-veterinaria" class="text-slate-300 hover:text-brand-gold">📷 Radiología</a>
          <a href="/servicios/medicina-interna-veterinaria" class="text-slate-300 hover:text-brand-gold">🩺 Medicina Interna</a>
        </div>
      </div>


      <div class="mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">

        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>'''

# Try to find with the exact bytes
idx = content.find('      </div>\n\n      <div class="mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">\n\n        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>')

if idx >= 0:
    print(f"Found at {idx}")
    content = content[:idx] + new + content[idx+len(old):]
    with open('preguntas-frecuentes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done!")
else:
    print("Not found with exact string")
    # Find what we have
    idx2 = content.find('mt-12 text-center bg-brand-royalBlue/20')
    if idx2 >= 0:
        print(f"Found partial at {idx2}: {repr(content[idx2:idx2+200])}")