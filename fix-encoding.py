# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 520 encoding
if 'UbicaciÃ³n' in lines[519]:
    lines[519] = lines[519].replace('UbicaciÃ³n', 'Ubicación')
    lines[519] = lines[519].replace('ClÃ­nica', 'Clínica')
    print(f"Fixed line 520 encoding")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")