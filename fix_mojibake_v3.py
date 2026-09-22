#!/usr/bin/env python3
"""
Comprehensive mojibake fix using pattern replacement.
Handles both UTF-8->latin1 mojibake (Ã³, Ã©, etc.) and already-corrupted patterns (Ǹ, �?).
"""

import re
from pathlib import Path

# Comprehensive mojibake replacement map
MOJIBAKE_MAP = {
    # UTF-8 -> Latin-1 mojibake (recoverable)
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú', 'Ã±': 'ñ',
    'Ã‰': 'É', 'Ã"': 'Ó', 'Ãš': 'Ú', 'Ã': 'Á', 'Ã': 'Í', 'Ã': 'Á',
    'Ã¼': 'ü', 'Ãœ': 'Ü', 'Ã§': 'ç', 'Ã‡': 'Ç',
    'Ã ': 'à', 'Ã¨': 'è', 'Ã¬': 'ì', 'Ã²': 'ò', 'Ã¹': 'ù',
    'Ã¢': 'â', 'Ãª': 'ê', 'Ã®': 'î', 'Ã´': 'ô', 'Ã»': 'û',
    'Ã£': 'ã', 'Ãµ': 'õ', 'Ã‡': 'Ç',
    
    # Double-encoded patterns (common in JSON-LD)
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú', 'Ã±': 'ñ',
    'mÃ©dico': 'médico', 'especializaciÃ³n': 'especialización',
    'atenciÃ³n': 'atención', 'clÃ­nica': 'clínica', 'cardiologÃ­a': 'cardiología',
    'nefrologÃ­a': 'nefrología', 'neurologÃ­a': 'neurología', 'gastroenterologÃ­a': 'gastroenterología',
    'oncologÃ­a': 'oncología', 'ortopedÃ­a': 'ortopedia', 'radiologÃ­a': 'radiología',
    'dermatologÃ­a': 'dermatología', 'citopatologÃ­a': 'citopatología',
    'nutriciÃ³n': 'nutrición', 'medicina': 'medicina', 'interna': 'interna',
    'veterinaria': 'veterinaria', 'evaluaciÃ³n': 'evaluación', 'diagnÃ³stico': 'diagnóstico',
    'tratamiento': 'tratamiento', 'enfermedad': 'enfermedad', 'renal': 'renal',
    'aguda': 'aguda', 'crÃ³nica': 'crónica', 'vÃ­as': 'vías', 'urinarias': 'urinarias',
    'manejo': 'manejo', 'epilepsia': 'epilepsia', 'hernias': 'hernias', 'discales': 'discales',
    'trastornos': 'trastornos', 'neuromusculares': 'neuromusculares',
    'patologÃ­as': 'patologías', 'digestivas': 'digestivas', 'hepatologÃ­as': 'hepatologías',
    'pancreÃ¡ticas': 'pancreáticas', 'formulaciÃ³n': 'formulación', 'dietas': 'dietas',
    'mÃ©dicas': 'médicas', 'prescriptivas': 'prescriptivas', 'pacientes': 'pacientes',
    'condiciones': 'condiciones', 'especiales': 'especiales', 'evaluaciÃ³n': 'evaluación',
    'quirÃºrgica': 'quirúrgica', 'ortopÃ©dica': 'ortopédica', 'fracturas': 'fracturas',
    'ligamentos': 'ligamentos', 'alergias': 'alergias', 'atÃ³picas': 'atópicas',
    'otitis': 'otitis', 'crÃ³nica': 'crónica', 'piel': 'piel', 'ultrasonografÃ­a': 'ultrasonografía',
    'precisÃ³n': 'precisión', 'equipamiento': 'equipamiento', 'avanzado': 'avanzado',
    'profesional': 'profesional', 'dedicada': 'dedicada', 'salud': 'salud', 'paciente': 'paciente',
    'cita': 'cita', 'previa': 'previa', 'urgencias': 'urgencias', 'exclusivamente': 'exclusivamente',
    'villavicencio': 'villavicencio', 'meta': 'meta', 'colombia': 'colombia',
    'derechos': 'derechos', 'reservados': 'reservados', 'google': 'google',
    'reseÃ±a': 'reseña', 'meses': 'meses', 'aÃ±os': 'años', 'mejor': 'mejor',
    'veterinario': 'veterinario', 'profesional': 'profesional', 'confiando': 'confiando',
    'salud': 'salud', 'mascotas': 'mascotas', 'lugar': 'lugar', 'encontre': 'encontre',
    'trabajando': 'trabajando', 'feliz': 'feliz', 'varios': 'varios', 'aproximadamente': 'aproximadamente',
    'buena': 'buena', 'explica': 'explica', 'paciencia': 'paciencia', 'tiempo': 'tiempo',
    'consulta': 'consulta', 'tranquilos': 'tranquilos', 'integrante': 'integrante',
    'familia': 'familia', 'manos': 'manos', 'punto': 'punto', 'morir': 'morir',
    'gracias': 'gracias', 'ahora': 'ahora', 'goza': 'goza', 'perfecta': 'perfecta',
    'corre': 'corre', 'juega': 'juega', 'cuando': 'cuando', 'tenia': 'tenía',
    'recomendado': 'recomendado', 'doctor': 'doctor', 'convulsiones': 'convulsiones',
    'tratamiento': 'tratamiento', 'satisfactoriamente': 'satisfactoriamente', 'bueno': 'bueno',
    'llano': 'llano', 'seÃ±or': 'señor', 'dios': 'dios', 'travÃ©s': 'través',
    'sanÃ³': 'sanó', 'perrita': 'perrita', 'pasado': 'pasado', 'manos': 'manos',
    'ningÃºn': 'ningún', 'acertaba': 'acertaba', 'punto': 'punto', 'morir': 'morir',
    
    # Already-corrupted patterns (replacement chars, etc.)
    '�': 'ó',  # context-dependent, but most common
    'Ǹ': 'ó',  # mǸdico -> médico
    '�?': 'ó', '�?�': 'ó', '��': 'ó', '�': 'ó',
    '�': 'í', '�': 'á', '�': 'é', '�': 'ñ', '�': 'ú',
    
    # Specific patterns seen in output
    'Cl�?��nica': 'Clínica',
    'Cl�?�nica': 'Clínica',
    'Atenci�?��n': 'Atención',
    'Atenci�?��n': 'Atención',
    'Atenci�?�nica': 'Atención clínica',
    'M�?��dicas': 'Médicas',
    'M�?�dicas': 'Médicas',
    'M�?��dicas Cl�?��nicas': 'Médicas Clínicas',
    'Diagn�?��stico': 'Diagnóstico',
    'Diagn�?�stico': 'Diagnóstico',
    'Gastroenterolog�?�a': 'Gastroenterología',
    'Neurolog�?�a': 'Neurología',
    'Cardiolog�?�a': 'Cardiología',
    'Nefrolog�?�a': 'Nefrología',
    'Oncolog�?�a': 'Oncología',
    'Ortopedi�?�a': 'Ortopedia',
    'Radiolog�?�a': 'Radiología',
    'Dermatolog�?�a': 'Dermatología',
    'Citopatolog�?�a': 'Citopatología',
    'Nutrici�?��n': 'Nutrición',
    'Nutrici�?�nica': 'Nutrición Clínica',
    'Nutrici�?�nica Cl�?�nica': 'Nutrición Clínica',
    'Especialidades M�?��dicas': 'Especialidades Médicas',
    'Especialidades M�?�dicas': 'Especialidades Médicas',
    'Especialidad': 'Especialidad',
    'Especialista': 'Especialista',
    'Rese�?��a': 'Reseña',
    'Rese�?�a': 'Reseña',
    'aÃ±os': 'años',
    'meses': 'meses',
    'Se�?��or': 'Señor',
    'trav�?��s': 'través',
    'sanÃ³': 'sanó',
    'aÃ±os': 'años',
    'habÃ­a': 'había',
    'ningÃºn': 'ningún',
    'pasiÃ³': 'pasó',
    'gracias': 'gracias',
    'perfecta': 'perfecta',
    'aproximadamente': 'aproximadamente',
    'recomendado': 'recomendado',
    'Doctor': 'Doctor',
    'convulsiones': 'convulsiones',
    'satisfactoriamente': 'satisfactoriamente',
    'bueno': 'bueno',
    'Villavicencio': 'Villavicencio',
    'Meta': 'Meta',
    'Colombia': 'Colombia',
    'derechos': 'derechos',
    'reservados': 'reservados',
    'Google': 'Google',
    'opiniones': 'opiniones',
    'clientes': 'clientes',
    'dice': 'dice',
    'nuestros': 'nuestros',
    'cita': 'cita',
    'previa': 'previa',
    'urgencias': 'urgencias',
    'atendemos': 'atendemos',
    'exclusivamente': 'exclusivamente',
    'medicina': 'medicina',
    'interna': 'interna',
    'mascotas': 'mascotas',
    'equipamiento': 'equipamiento',
    'avanzado': 'avanzado',
    'profesional': 'profesional',
    'dedicada': 'dedicada',
    'paciente': 'paciente',
    'Centro': 'Centro',
    'médico': 'médico',
    'especializaciÃ³n': 'especialización',
    'cuidados': 'cuidados',
    'intensivos': 'intensivos',
    'Consulta': 'Consulta',
    'externa': 'externa',
    'especialidad': 'especialidad',
    'Únicamente': 'Únicamente',
    'Imagen': 'Imagen',
    'TelÃ©fono': 'Teléfono',
    'DirecciÃ³n': 'Dirección',
    'Calle': 'Calle',
    'Localidad': 'Localidad',
    'RegiÃ³n': 'Región',
    'PaÃ­s': 'País',
    'Coordenadas': 'Coordenadas',
    'Latitud': 'Latitud',
    'Longitud': 'Longitud',
    'Horario': 'Horario',
    'Apertura': 'Apertura',
    'Cierre': 'Cierre',
    'DÃ­a': 'Día',
    'Semana': 'Semana',
    'Especialidad': 'Especialidad',
    'Ã¡rea': 'Área',
    'Servida': 'Servida',
    'Nombre': 'Nombre',
}

def fix_file(filepath: Path) -> bool:
    """Fix mojibake in a single file using pattern replacement."""
    raw = filepath.read_bytes()
    
    # Try to decode as UTF-8 first
    try:
        content = raw.decode('utf-8')
    except UnicodeDecodeError:
        # If not valid UTF-8, decode as latin-1
        content = raw.decode('latin-1')
    
    original = content
    
    # Apply all replacements
    for bad, good in MOJIBAKE_MAP.items():
        if bad in content:
            content = content.replace(bad, good)
    
    # Also fix any remaining � in context
    # These are harder - we'll do a second pass for common words
    content = content.replace('m�dico', 'médico')
    content = content.replace('cl�nica', 'clínica')
    content = content.replace('atenci�n', 'atención')
    content = content.replace('cardiolog�a', 'cardiología')
    content = content.replace('nefrolog�a', 'nefrología')
    content = content.replace('neurolog�a', 'neurología')
    content = content.replace('gastroenterolog�a', 'gastroenterología')
    content = content.replace('oncolog�a', 'oncología')
    content = content.replace('ortoped�a', 'ortopedia')
    content = content.replace('radiolog�a', 'radiología')
    content = content.replace('dermatolog�a', 'dermatología')
    content = content.replace('citopatolog�a', 'citopatología')
    content = content.replace('nutrici�n', 'nutrición')
    content = content.replace('a�os', 'años')
    content = content.replace('rese�a', 'reseña')
    content = content.replace('Se�or', 'Señor')
    content = content.replace('trav�s', 'través')
    content = content.replace('san�', 'sanó')
    content = content.replace('hab�a', 'había')
    content = content.replace('ning�n', 'ningún')
    content = content.replace('pasiÃ³', 'pasó')
    content = content.replace('perfecta', 'perfecta')
    content = content.replace('aproximadamente', 'aproximadamente')
    content = content.replace('recomendado', 'recomendado')
    content = content.replace('convulsiones', 'convulsiones')
    content = content.replace('satisfactoriamente', 'satisfactoriamente')
    content = content.replace('Villavicencio', 'Villavicencio')
    content = content.replace('Colombia', 'Colombia')
    content = content.replace('derechos', 'derechos')
    content = content.replace('reservados', 'reservados')
    content = content.replace('Google', 'Google')
    content = content.replace('opiniones', 'opiniones')
    content = content.replace('clientes', 'clientes')
    content = content.replace('cita', 'cita')
    content = content.replace('previa', 'previa')
    content = content.replace('urgencias', 'urgencias')
    content = content.replace('atendemos', 'atendemos')
    content = content.replace('medicina', 'medicina')
    content = content.replace('interna', 'interna')
    content = content.replace('mascotas', 'mascotas')
    content = content.replace('equipamiento', 'equipamiento')
    content = content.replace('avanzado', 'avanzado')
    content = content.replace('profesional', 'profesional')
    content = content.replace('dedicada', 'dedicada')
    content = content.replace('paciente', 'paciente')
    content = content.replace('Centro', 'Centro')
    content = content.replace('especializaci�n', 'especialización')
    content = content.replace('cuidados', 'cuidados')
    content = content.replace('intensivos', 'intensivos')
    content = content.replace('Consulta', 'Consulta')
    content = content.replace('externa', 'externa')
    content = content.replace('especialidad', 'especialidad')
    content = content.replace('�nicamente', 'únicamente')
    
    # Fix canonicals
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
    
    files = list(base.glob("*.html")) + list(base.glob("servicios/*.html"))
    
    print(f"Processing {len(files)} HTML files...\n")
    
    fixed = 0
    for f in files:
        if fix_file(f):
            print(f"  FIXED: {f.relative_to(base)}")
            fixed += 1
        else:
            print(f"  OK:     {f.relative_to(base)}")
    
    print(f"\nTotal fixed: {fixed}/{len(files)}")

if __name__ == "__main__":
    main()