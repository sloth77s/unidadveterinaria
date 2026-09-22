import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")

html_files = list(root.glob("*.html")) + list(root.glob("servicios/*.html"))

for f in html_files:
    content = f.read_text(encoding="utf-8")
    
    # Determine the relative path
    if "servicios" in str(f):
        prefix = "../"
    else:
        prefix = "./"
    
    # Add manifest link before </head>
    manifest_link = f'  <link rel="manifest" href="{prefix}manifest.json">\n'
    content = content.replace('</head>', manifest_link + '</head>')
    
    # Add theme-color meta tag
    theme_color = '  <meta name="theme-color" content="#0D3880">\n'
    content = content.replace('<meta name="viewport"', theme_color + '<meta name="viewport"')
    
    # Add service worker registration before closing body (after ui-components.js)
    sw_script = f'''
  <script>
    if ('serviceWorker' in navigator) {{
      window.addEventListener('load', () => {{
        navigator.serviceWorker.register('{prefix}sw.js')
          .then(reg => console.log('SW registered:', reg.scope))
          .catch(err => console.log('SW registration failed:', err));
      }});
    }}
  </script>
'''
    # Insert after ui-components.js script
    content = content.replace(
        f'<script src="{prefix}js/ui-components.js"></script>',
        f'<script src="{prefix}js/ui-components.js"></script>{sw_script}'
    )
    
    f.write_text(content, encoding="utf-8")
    print(f"Updated {f.name}")

print("Done!")