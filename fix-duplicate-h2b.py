# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the first h2 with � encoding and remove it
for i, line in enumerate(lines):
    if '�Tiene alguna otra inquietud sobre su paciente?</h2>' in line:
        print(f"Removing line {i}: {repr(line)}")
        del lines[i]
        break

with open('preguntas-frecuentes.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")