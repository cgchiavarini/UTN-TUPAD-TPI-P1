import csv
ruta_csv = 'paises.csv'
def cargar_paises(ruta_csv):
    paises = []
    try:
        with open(ruta_csv, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Error en conversión de tipos: {fila}")
    except FileNotFoundError:
        print("Archivo CSV no encontrado.")
    return paises
