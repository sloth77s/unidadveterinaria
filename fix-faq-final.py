# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Exact old string with correct newlines
old = '''  </div>

        </div>




      </div>




      <div class="mt-12 text-center bg-brand-royalBlue/20 p-6 rounded-2xl border border-brand-gold/30">

        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>'''

new = '''  </div>

        </div>




      </div>




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

if old in content:
    content = content.replace(old, new)
    with open('preguntas-frecuentes.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done!")
else:
    print("Not found")
    # Show context
    idx = content.find('<div class="mt-12 text-center bg-brand-royalBlue/20')
    print(repr(content[idx-80:idx]))