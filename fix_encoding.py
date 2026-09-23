import os
import glob

# ============================================================
#  fix_encoding.py — Unidad Veterinaria
#  Ejecutar UNA VEZ dentro de la carpeta del proyecto
#  python fix_encoding.py
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files = (
    glob.glob(os.path.join(BASE_DIR, "*.html")) +
    glob.glob(os.path.join(BASE_DIR, "servicios", "*.html"))
)

# Reemplazos a nivel de bytes (orden importa: más largos primero)
BYTE_FIXES = [
    # BOM doble-codificado
    (b'\xc3\xaf\xc2\xbb\xc2\xbf', b''),
    # ¿ (signo de interrogación)
    (b'\xc3\x81\xc2\x82\xc2\xbf', '¿'.encode()),
    # ¡ (signo de exclamación)
    (b'\xc3\x81\xc2\x82\xc2\xa1', '¡'.encode()),
    # á (aviso-legal: ámbito)
    (b'\xc3\x81\xc2\x81\xc3\x82\xc2\x81', 'á'.encode()),
    # … (puntos suspensivos)
    (b'\xc3\x81\xc2\xa2\xc3\xa2\xc2\x82\xc2\xac\xc3\x82\xc2\xa6', '…'.encode()),
    # → (flecha derecha, contacto "Google Maps")
    (b'\xc3\x81\xc2\xa2\xc3\xa2\xc2\x82\xc2\xac\xc3\xa2\xc2\x80\xc2\x9d', '→'.encode()),
    # ✕ (cruz JS preguntas-frecuentes)
    (b'\xc3\x81\xc2\xa2\xc3\x8b\xc2\x86\xc3\xa2\xc2\x80\xc2\x99', '✕'.encode()),
    # ✔ (checkmark, dos variantes)
    (b'\xc3\x81\xc2\xa2\xc3\x82\xc2\x82\xc3\x82\xc2\xb0', '✔'.encode()),
    (b'\xc3\x81\xc2\xa2\xc3\x82\xc2\x8f\xc3\x82\xc2\xb0', '✔'.encode()),
    # Ñ (RESEÑAS)
    (b'\xc3\x81\xc2\x81\xc3\xa2\xc2\x80\xc2\x98', 'Ñ'.encode()),
    # Ó (CONVERSIÓN, BOTÓN)
    (b'\xc3\x81\xc2\x81\xc3\xa2\xc2\x80\xc2\x9c', 'Ó'.encode()),
    # Á (RÁPIDA)
    (b'\xc3\x81\xc2\x81\xc3\x82\xc2\x81', 'Á'.encode()),
    # 📍 (dirección, contacto)
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80\xc2\x9c\xc3\x82\xc2\x8d', '📍'.encode()),
    # 📞 (teléfono, contacto)
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80\xc2\x9c\xc3\x85\xc2\xbe', '📞'.encode()),
    # 📸 (instagram, contacto)
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80\xc2\x9c\xc3\x82\xc2\xb8', '📸'.encode()),
    # 🐾 (pata, reseñas — variante larga)
    (b'\xc3\x85\xc2\xb8\xc3\x82\xc2\x90\xc3\x82\xc2\xb6', '🐾'.encode()),
    # 🐕 (perro, reseñas)
    (b'\xc3\x85\xc2\xb8\xc3\x82\xc2\x90\xc3\x8b\xc2\x86', '🐕'.encode()),
    # 🏆 (trofeo, reseña "Excelente Doctor")
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80\xc2\x98\xc3\x85\xc2\x92', '🏆'.encode()),
    # ❤️ (reseña "Mi niña")
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80\xc2\x98\xc3\x82\xc2\x8d', '❤️'.encode()),
    # Å¸âÂ remanentes genéricos (fallback)
    (b'\xc3\x85\xc2\xb8\xc3\xa2\xc2\x80', b''),
]

fixed = 0
for filepath in files:
    with open(filepath, 'rb') as f:
        original = f.read()

    content = original
    for bad, good in BYTE_FIXES:
        content = content.replace(bad, good)

    if content != original:
        with open(filepath, 'wb') as f:
            f.write(content)
        print(f"  CORREGIDO: {os.path.relpath(filepath, BASE_DIR)}")
        fixed += 1
    else:
        print(f"  OK:        {os.path.relpath(filepath, BASE_DIR)}")

print(f"\n✅ Listo. {fixed} archivo(s) corregido(s).")
print("   Ahora haz commit y push a GitHub, luego despliega.")
