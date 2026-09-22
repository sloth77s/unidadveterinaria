#!/usr/bin/env python3
"""
Fix mojibake encoding in HTML files.
Mojibake pattern: UTF-8 bytes misinterpreted as Latin-1/Windows-1252.
Fix: encode as latin-1, decode as utf-8.
"""

import os
import re
from pathlib import Path

def fix_mojibake(text: str) -> str:
    """Fix mojibake by re-encoding latin-1 -> utf-8."""
    try:
        # The corrupted text is UTF-8 bytes that were decoded as latin-1
        # So we encode back to latin-1 (recovering the original UTF-8 bytes)
        # then decode properly as UTF-8
        return text.encode('latin-1').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        # If that fails, try cp1252 (Windows-1252)
        try:
            return text.encode('cp1252').decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            return text  # Return original if can't fix

def fix_file(filepath: Path) -> bool:
    """Fix mojibake in a single file. Returns True if changed."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # If file isn't valid UTF-8, read as latin-1 first
        content = filepath.read_text(encoding='latin-1')
    
    original = content
    
    # Fix mojibake in the entire content
    fixed = fix_mojibake(content)
    
    # Also fix JSON-LD specifically (often has separate encoding issues)
    # Find and fix JSON-LD script blocks
    def fix_json_ld(match):
        json_content = match.group(1)
        try:
            fixed_json = fix_mojibake(json_content)
            return f'<script type="application/ld+json">\n  {fixed_json}\n  </script>'
        except:
            return match.group(0)
    
    fixed = re.sub(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        fix_json_ld,
        fixed,
        flags=re.DOTALL
    )
    
    if fixed != original:
        filepath.write_text(fixed, encoding='utf-8')
        return True
    return False

def main():
    base = Path(r"C:\Users\SOPORTES JPVM\Documents\web uci vet con seo\unidad-veterinaria-david-aguilar")
    
    # Files to fix
    files = []
    files.extend(base.glob("*.html"))
    files.extend(base.glob("servicios/*.html"))
    
    print(f"Found {len(files)} HTML files to check")
    
    fixed_count = 0
    for f in files:
        if fix_file(f):
            print(f"  FIXED: {f.relative_to(base)}")
            fixed_count += 1
        else:
            print(f"  OK:     {f.relative_to(base)}")
    
    print(f"\nTotal fixed: {fixed_count}/{len(files)}")
    
    # Also fix canonical URLs to unidadveterinaria.com (no .html)
    print("\n--- Updating canonical URLs ---")
    for f in files:
        content = f.read_text(encoding='utf-8')
        original = content
        
        # Fix canonical URLs
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
            f.write_text(content, encoding='utf-8')
            print(f"  Updated canonicals: {f.relative_to(base)}")

if __name__ == "__main__":
    main()