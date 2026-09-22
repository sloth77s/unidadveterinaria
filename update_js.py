import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")

html_files = list(root.glob("*.html")) + list(root.glob("servicios/*.html"))

# Pattern to find and remove inline script blocks at the end of body
# These are the mobile menu and specialties toggle scripts
script_pattern = r'\s*<script>\s*// Mobile hamburger menu toggle[\s\S]*?</script>\s*</body>'

for f in html_files:
    content = f.read_text(encoding="utf-8")
    
    # Determine the relative path to js folder
    if "servicios" in str(f):
        js_prefix = "../js/"
    else:
        js_prefix = "js/"
    
    # Replace the inline script block with shared JS reference
    content = re.sub(
        r'\s*<script>\s*// Mobile hamburger menu toggle[\s\S]*?</script>\s*</body>',
        f'\n  <script src="{js_prefix}ui-components.js"></script>\n</body>',
        content
    )
    
    # Also handle pages that might have slightly different comment
    content = re.sub(
        r'\s*<script>\s*const mobileMenuBtn = document\.getElementById\([\s\S]*?</script>\s*</body>',
        f'\n  <script src="{js_prefix}ui-components.js"></script>\n</body>',
        content
    )
    
    # For preguntas-frecuentes.html which has FAQ script + mobile scripts
    content = re.sub(
        r'\s*<script>\s*// FAQ Accordion interactive logic[\s\S]*?</script>\s*<script>\s*// Mobile hamburger menu toggle[\s\S]*?</script>\s*</body>',
        f'\n  <script src="{js_prefix}ui-components.js"></script>\n</body>',
        content
    )
    
    # For contacto-y-ubicacion.html which has main.js + mobile scripts
    content = re.sub(
        r'\s*<script src="js/main\.js"></script>\s*<script>\s*// Mobile hamburger menu toggle[\s\S]*?</script>\s*</body>',
        f'\n  <script src="{js_prefix}ui-components.js"></script>\n</body>',
        content
    )
    
    f.write_text(content, encoding="utf-8")
    print(f"Updated {f.name}")

print("Done!")