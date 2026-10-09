# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and remove the duplicate h2 (should be around line 395 now)
# The duplicate is: '        <h2 class="text-base font-bold text-white">�Tiene alguna otra inquietud sobre su paciente?</h2>\n'
# It appears twice - we want to keep only the second one (the one in the CTA section)

# Find all occurrences of this line
indices = [i for i, line in enumerate(lines) if '�Tiene alguna otra inquietud sobre su paciente?</h2>' in line]
print(f"Found at lines: {indices}")

# Remove the first occurrence (the duplicate)
if len(indices) >= 2:
    del lines[indices[0]]
    print(f"Removed duplicate at line {indices[0]}")

with open('preguntas-frecuentes.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")