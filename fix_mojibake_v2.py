#!/usr/bin/env python3
"""
Fix mojibake by reading files as raw bytes -> latin-1 -> utf-8.
This recovers patterns like: Ã³ -> ó, Ã© -> é, Ã± -> ñ, Ãº -> ú, Ã­ -> í, etc.
"""

import re
from pathlib import Path

def fix_mojibake_bytes(filepath: Path) -> bool:
    """Read as bytes, decode latin-1, write as UTF-8."""
    # Read raw bytes
    raw = filepath.read_bytes()
    
    try:
        # Decode as latin-1 (recovers the original UTF-8 byte sequences)
        decoded = raw.decode('latin-1')
        # Now encode as UTF-8
        fixed = decoded.encode('utf-8')
    except UnicodeDecodeError:
        # If latin-1 fails, file might already be UTF-8
        return False
    
    if fixed != raw:
        filepath.write_bytes(fixed)
        return True
    return False

def fix_canonicals(filepath: Path) -> bool:
    """Fix canonical URLs to unidadveterinaria.com (no .html)."""
    content = filepath.read_text(encoding='utf-8')
    original = content
    
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
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    base = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")
    
    files = []
    files.extend(base.glob("*.html"))
    files.extend(base.glob("servicios/*.html"))
    
    print(f"Processing {len(files)} HTML files...\n")
    
    fixed_mojibake = 0
    fixed_canonical = 0
    
    for f in files:
        if fix_mojibake_bytes(f):
            print(f"  FIXED MOJIBAKE: {f.relative_to(base)}")
            fixed_mojibake += 1
        else:
            print(f"  OK bytes:       {f.relative_to(base)}")
        
        if fix_canonicals(f):
            print(f"  FIXED CANONICAL: {f.relative_to(base)}")
            fixed_canonical += 1
    
    print(f"\nTotal mojibake fixed: {fixed_mojibake}/{len(files)}")
    print(f"Total canonicals fixed: {fixed_canonical}/{len(files)}")

if __name__ == "__main__":
    main()