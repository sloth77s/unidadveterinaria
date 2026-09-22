import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")

html_files = list(root.glob("*.html")) + list(root.glob("servicios/*.html"))

for f in html_files:
    content = f.read_text(encoding="utf-8")
    
    # Determine the relative path to img folder
    if "servicios" in str(f):
        img_prefix = "../img/"
        webp_prefix = "../img/"
    else:
        img_prefix = "img/"
        webp_prefix = "img/"
    
    # Replace logo images with picture element
    old_logo = f'{img_prefix}logo%20sin%20fondo%20uci%20.png'
    webp_logo = f'{webp_prefix}logo-sin-fondo-uci.webp'
    
    # Find all occurrences and replace
    content = re.sub(
        rf'<img src="{re.escape(old_logo)}" alt="([^"]*)" class="([^"]*)">',
        rf'<picture>\n            <source srcset="{webp_logo}" type="image/webp">\n            <img src="{old_logo}" alt="\1" class="\2" loading="lazy">\n          </picture>',
        content
    )
    
    # Also handle self-closing tags
    content = re.sub(
        rf'<img src="{re.escape(old_logo)}" alt="([^"]*)" class="([^"]*)" ?/?>',
        rf'<picture>\n            <source srcset="{webp_logo}" type="image/webp">\n            <img src="{old_logo}" alt="\1" class="\2" loading="lazy">\n          </picture>',
        content
    )
    
    f.write_text(content, encoding="utf-8")
    print(f"Updated {f.name}")

print("Done!")