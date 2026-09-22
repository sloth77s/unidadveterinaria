import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")

html_files = list(root.glob("*.html")) + list(root.glob("servicios/*.html"))

# Production domain
domain = "https://unidadveterinariadavidaguilar.com"

for f in html_files:
    content = f.read_text(encoding="utf-8")
    
    # Replace localhost URLs with production domain in canonical and og:url
    # Pattern for canonical
    content = re.sub(
        r'<link rel="canonical" href="http://localhost:8080/([^"]*)">',
        rf'<link rel="canonical" href="{domain}/\1">',
        content
    )
    content = re.sub(
        r'<link rel="canonical" href="http://localhost:8080/">',
        rf'<link rel="canonical" href="{domain}/">',
        content
    )
    
    # Pattern for og:url
    content = re.sub(
        r'<meta property="og:url" content="http://localhost:8080/([^"]*)">',
        rf'<meta property="og:url" content="{domain}/\1">',
        content
    )
    content = re.sub(
        r'<meta property="og:url" content="http://localhost:8080/">',
        rf'<meta property="og:url" content="{domain}/">',
        content
    )
    
    # Pattern for JSON-LD url
    content = re.sub(
        r'"url": "http://localhost:8080/([^"]*)"',
        rf'"url": "{domain}/\1"',
        content
    )
    content = re.sub(
        r'"url": "http://localhost:8080/"',
        rf'"url": "{domain}/"',
        content
    )
    
    # Pattern for JSON-LD image
    content = re.sub(
        r'"image": "http://localhost:8080/([^"]*)"',
        rf'"image": "{domain}/\1"',
        content
    )
    
    f.write_text(content, encoding="utf-8")
    print(f"Updated {f.name}")

print("Done!")