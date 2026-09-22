import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")

html_files = list(root.glob("*.html")) + list(root.glob("servicios/*.html"))

# Pattern to find and remove the inline tailwind config script
tailwind_config_pattern = r'\s*<script>\s*tailwind\.config\s*=\s*\{[\s\S]*?\}\s*</script>'

for f in html_files:
    content = f.read_text(encoding="utf-8")
    
    # Determine the relative path to js folder
    if "servicios" in str(f):
        js_prefix = "../js/"
    else:
        js_prefix = "js/"
    
    # Remove inline tailwind config
    content = re.sub(tailwind_config_pattern, '', content)
    
    # Add the shared config script before the closing </head> tag
    shared_script = f'  <script src="{js_prefix}tailwind-config.js"></script>\n'
    content = content.replace('</head>', shared_script + '</head>')
    
    f.write_text(content, encoding="utf-8")
    print(f"Updated {f.name}")

print("Done!")