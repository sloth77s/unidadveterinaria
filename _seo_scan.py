import json
import re
from pathlib import Path

root = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo")
files = [
    p
    for p in root.rglob("*.html")
    if "runs" not in p.parts and "unidad-veterinaria-david-aguilar" not in p.parts
]


def grab(html, pat):
    m = re.search(pat, html, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


rows = []
for p in sorted(files):
    html = p.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    words = re.findall(r"[\wáéíóúüñÁÉÍÓÚÜÑ]+", text, flags=re.U)
    title = grab(html, r"<title>(.*?)</title>")
    desc = grab(html, r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']')
    if not desc:
        desc = grab(html, r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']')
    canon = grab(html, r'rel=["\']canonical["\']\s+href=["\'](.*?)["\']')
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    h1s = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h)).strip() for h in h1s]
    h2s = len(re.findall(r"<h2\b", html, re.I))
    imgs = re.findall(r"<img\b[^>]*>", html, re.I)
    missing_alt = sum(1 for img in imgs if not re.search(r"\balt=", img, re.I))
    empty_alt = sum(1 for img in imgs if re.search(r'\balt=["\']\s*["\']', img, re.I))
    schema = re.findall(r'"@type"\s*:\s*"([^"]+)"', html)
    robots = grab(html, r'name=["\']robots["\']\s+content=["\'](.*?)["\']')
    internal = len(re.findall(r'href=["\'](?!https?://|mailto:|tel:|#|javascript:)[^"\']+["\']', html, re.I))
    rows.append(
        {
            "file": str(p.relative_to(root)).replace("\\", "/"),
            "title": title,
            "title_len": len(title),
            "desc_len": len(desc),
            "canon": canon,
            "h1_count": len(h1s),
            "h1": h1s[:2],
            "h2": h2s,
            "words": len(words),
            "imgs": len(imgs),
            "missing_alt": missing_alt,
            "empty_alt": empty_alt,
            "schema": schema,
            "robots": robots,
            "viewport": "viewport" in html.lower(),
            "old_domain": html.count("pages.dev"),
            "new_domain": html.count("unidadveterinaria.com.co"),
            "internal_hrefs": internal,
        }
    )

print(json.dumps(rows, ensure_ascii=False, indent=2))
