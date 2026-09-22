import os
import re

def fix_file(filepath):
    """Fix mojibake encoding in a single HTML file"""
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    # Check if file starts with BOM
    has_bom = raw.startswith(b'\xef\xbb\xbf')
    
    # Decode as latin-1 to get the raw characters, then re-encode as UTF-8
    try:
        decoded = raw.decode('latin-1')
    except UnicodeDecodeError:
        print(f"  Warning: Could not decode {filepath} as latin-1")
        return False
    
    # Fix common mojibake patterns
    replacements = {
        # Spanish characters
        'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú', 'Ã±': 'ñ',
        'Ã‰': 'É', 'Ã"': 'Ó', 'Ãš': 'Ú', 'Ã': 'Á', 'Ã': 'Í',
        'Ã¼': 'ü', 'Ãœ': 'Ü', 'Ã§': 'ç', 'Ã‡': 'Ç',
        'Ã ': 'à', 'Ã¨': 'è', 'Ã¬': 'ì', 'Ã²': 'ò', 'Ã¹': 'ù',
        'Ã¢': 'â', 'Ãª': 'ê', 'Ã®': 'î', 'Ã´': 'ô', 'Ã»': 'û',
        'Ã£': 'ã', 'Ãµ': 'õ', 'Ã‡': 'Ç',
        
        # Common words
        'mÃ©dico': 'médico',
        'especializaciÃ³n': 'especialización',
        'atenciÃ³n': 'atención',
        'clÃ­nica': 'clínica',
        'cardiologÃ­a': 'cardiología',
        'nefrologÃ­a': 'nefrología',
        'neurologÃ­a': 'neurología',
        'gastroenterologÃ­a': 'gastroenterología',
        'oncologÃ­a': 'oncología',
        'ortopedÃ­a': 'ortopedia',
        'radiologÃ­a': 'radiología',
        'dermatologÃ­a': 'dermatología',
        'citopatologÃ­a': 'citopatología',
        'nutriciÃ³n': 'nutrición',
        'aÃ±os': 'años',
        'reseÃ±a': 'reseña',
        'SeÃ±or': 'Señor',
        'travÃ©s': 'través',
        'sanÃ³': 'sanó',
        'habÃ­a': 'había',
        'ningÃºn': 'ningún',
        'pasiÃ³': 'pasó',
        'perfecta': 'perfecta',
        'aproximadamente': 'aproximadamente',
        'recomendado': 'recomendado',
        'convulsiones': 'convulsiones',
        'satisfactoriamente': 'satisfactoriamente',
        'Villavicencio': 'Villavicencio',
        'Colombia': 'Colombia',
        'derechos': 'derechos',
        'reservados': 'reservados',
        'Google': 'Google',
        'opiniones': 'opiniones',
        'clientes': 'clientes',
        'cita': 'cita',
        'previa': 'previa',
        'urgencias': 'urgencias',
        'atendemos': 'atendemos',
        'medicina': 'medicina',
        'interna': 'interna',
        'mascotas': 'mascotas',
        'equipamiento': 'equipamiento',
        'avanzado': 'avanzado',
        'profesional': 'profesional',
        'dedicada': 'dedicada',
        'paciente': 'paciente',
        'Centro': 'Centro',
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
        'Ã¡rea': 'Área',
        'Servida': 'Servida',
        'Nombre': 'Nombre',
    }
    
    fixed = decoded
    for bad, good in replacements.items():
        fixed = fixed.replace(bad, good)
    
    # Also fix any remaining standalone 'Ã' patterns by removing them
    # (these are corrupted characters that couldn't be mapped)
    fixed = re.sub(r'Ã.', '', fixed)
    
    # Fix question marks
    fixed = fixed.replace('Â¿', '¿')
    
    # Fix ellipsis
    fixed = fixed.replace('â€¦', '…')
    
    # Clean up any remaining mojibake artifacts
    fixed = re.sub(r'[ðÿ][\x9f-\xaf]', '', fixed)
    
    # Remove BOM if present
    if fixed.startswith('\ufeff'):
        fixed = fixed[1:]
    
    # Write back as UTF-8 without BOM
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        original = f.read()
    
    if fixed != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    return False

def main():
    all_files = [
        'index.html',
        'aviso-legal.html',
        'politica-de-privacidad.html',
        'politica-de-cookies.html',
        'contacto-y-ubicacion.html',
        'preguntas-frecuentes.html',
    ]
    
    for fname in os.listdir('servicios'):
        if fname.endswith('.html'):
            all_files.append('servicios/' + fname)
    
    print('Fixing mojibake encoding issues...')
    fixed_count = 0
    for fname in all_files:
        if fix_file(fname):
            print(f'Fixed: {fname}')
            fixed_count += 1
        else:
            print(f'OK: {fname}')
    
    print(f'\nFixed {fixed_count} files')

if __name__ == '__main__':
    main()