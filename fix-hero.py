# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            UbicaciÃ³n de la ClÃ­nica
          </a>

        </div>'''

new = '''          <a href="/contacto-y-ubicacion" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            Ubicación de la Clínica
          </a>

          <a href="#especialidades" class="w-full sm:w-auto px-6 py-3.5 border border-brand-gold/50 text-brand-gold hover:bg-brand-gold hover:text-white font-semibold text-base rounded-xl transition-all">
            Ver Especialidades
          </a>

        </div>'''

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done!")
else:
    print("Pattern not found!")
    # Try to find similar
    import re
    matches = re.findall(r'Ubicaci[^<]+', content)
    print(f"Found: {matches}")