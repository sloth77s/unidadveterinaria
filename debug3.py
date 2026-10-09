# -*- coding: utf-8 -*-
with open('preguntas-frecuentes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the target div and replace using line-by-line approach
lines = content.split('\n')

# Find the line with the target div
target_line = -1
for i, line in enumerate(lines):
    if 'mt-12 text-center bg-brand-royalBlue/20' in line:
        target_line = i
        break

print(f"Target line: {target_line}")
print(f"Target line content: {repr(lines[target_line])}")

# The pattern is:
# line target_line-6: '  </div>'
# line target_line-5: ''
# line target_line-4: '        </div>'
# line target_line-3: ''
# line target_line-2: ''
# line target_line-1: '      </div>'
# line target_line-0: ''
# line target_line: '<div class="mt-12...'

# We want to insert after line target_line-1 (the '      </div>')
# Actually we want to replace from target_line-6 to target_line+1

# Let's find the exact pattern
for i in range(target_line-10, target_line+2):
    print(f"Line {i}: {repr(lines[i])}")