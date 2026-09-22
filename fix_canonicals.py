import re
from pathlib import Path

base = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")
files = list(base.glob("*.html")) + list(base.glob("servicios/*.html"))

for f in files:
    content = f.read_text(encoding="utf-8")
    original = content
    
    # Fix canonical URLs to unidadveterinaria.com (no .html)
    content = re.sub(
        r'href="https://unidadveterinariadavidaguilar\.com/(.*?)\.html"',
        r'href="https://unidadveterinaria.com/\1"',
        content
    )
    content = re.sub(
        r'href="https://unidadveterinariadavidaguilar\.com/"',
        r'href="https://unidadveterinaria.com/"',
        content
    )
    content = re.sub(
        r'href="http://localhost:3000/"',
        r'href="https://unidadveterinaria.com/"',
        content
    )
    
    if content != original:
        f.write_text(content, encoding="utf-8")
        print(f"Updated: {f.name}")
    else:
        print(f"No change: {f.name}")