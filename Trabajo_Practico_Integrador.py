import csv
import os
from statistics import mean


# ============================================================
# =============== BLOQUE VALIDACIONES ========================
# ============================================================

# VALIDACIONES: leer texto no vacío desde consola
def leer_texto_no_vacio(mensaje: str) -> str:
    texto = input(mensaje).strip()
    while not texto:
        print("El campo no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto

# VALIDACIONES: leer entero no negativo desde consola
def leer_entero_no_negativo(mensaje: str) -> int:
    texto = input(mensaje).strip().replace(".", "").replace(",", "")
    while not texto.isdigit():
        print("Debe ingresar un número entero no negativo.")
        texto = input(mensaje).strip().replace(".", "").replace(",", "")
    return int(texto)

# VALIDACIONES: normalizar cadenas generales
def normalizar_cadena(cadena: str) -> str:
    if cadena is None:
        return ""
    return cadena.strip()


# ============================================================
# ================== BLOQUE DATOS (CSV, VISTA) ===============
# ============================================================

ARCHIVO_CSV = "paises.csv"

# DATOS: crear archivo CSV (con encabezado) si no existe
def asegurar_csv_con_encabezado(ruta: str) -> None:
    if not os.path.exists(ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

# DATOS: cargar datos desde CSV
def cargar_desde_csv(ruta: str) -> list:
    asegurar_csv_con_encabezado(ruta)
    lista_paises = []
    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = normalizar_cadena(fila.get("nombre"))
            continente = normalizar_cadena(fila.get("continente"))
            pob_txt = normalizar_cadena(fila.get("poblacion"))
            sup_txt = normalizar_cadena(fila.get("superficie"))

            es_entero_pob = pob_txt.isdigit()
            es_entero_sup = sup_txt.isdigit()
            if not nombre or not continente or not es_entero_pob or not es_entero_sup:
                continue

            poblacion = int(pob_txt)
            superficie = int(sup_txt)
            if poblacion < 0 or superficie < 0:
                continue

            lista_paises.append({
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            })
    return lista_paises


# DATOS: guardar datos a CSV
def guardar_a_csv(lista_paises: list, ruta: str) -> None:
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        for pais in lista_paises:
            escritor.writerow(pais)

# DATOS: utilitario visual de línea separadora
def imprimir_linea(caracter: str = "─", ancho: int = 80) -> None:
    print(caracter * ancho)

# DATOS: utilitario visual de título
def imprimir_titulo(texto: str) -> None:
    imprimir_linea("=")
    print(texto)
    imprimir_linea("=")

# DATOS: tabla simple en consola
def imprimir_tabla(lista_paises: list) -> None:
    if not lista_paises:
        print("No hay registros para mostrar.")
        return
    columnas = ["nombre", "poblacion", "superficie", "continente"]
    anchos = {}
    for c in columnas:
        max_col = len(c)
        for p in lista_paises:
            largo = len(str(p[c]))
            if largo > max_col:
                max_col = largo
        anchos[c] = max_col

    encabezado_partes = []
    for c in columnas:
        encabezado_partes.append(c.upper().ljust(anchos[c]))
    encabezado = " | ".join(encabezado_partes)

    imprimir_linea()
    print(encabezado)
    imprimir_linea()

    for pais in lista_paises:
        fila_partes = []
        for c in columnas:
            fila_partes.append(str(pais[c]).ljust(anchos[c]))
        print(" | ".join(fila_partes))

    imprimir_linea()


# ============================================================
# ===================== BLOQUE BÚSQUEDAS =====================
# ============================================================

# BÚSQUEDAS: buscar país por nombre (parcial/insensible a mayúsculas)
def buscar_por_nombre(lista_paises: list) -> None:
    imprimir_titulo("Buscar país por nombre")
    patron = leer_texto_no_vacio("Texto a buscar: ").lower()
    resultados = []
    for p in lista_paises:
        if patron in p["nombre"].lower():
            resultados.append(p)
    imprimir_tabla(resultados)


# ============================================================
# ===================== BLOQUE ORDENAMIENTO ==================
# ============================================================

# ORDENAMIENTO: clave de orden por nombre en minúsculas
def clave_nombre(pais: dict):
    return pais["nombre"].lower()

# ORDENAMIENTO: clave de orden por población
def clave_poblacion(pais: dict):
    return pais["poblacion"]

# ORDENAMIENTO: clave de orden por superficie
def clave_superficie(pais: dict):
    return pais["superficie"]

# ORDENAMIENTO: ordenar por nombre/población/superficie (asc/desc)
def ordenar_paises(lista_paises: list) -> None:
    imprimir_titulo("Ordenar países")
    print("1) Nombre (A→Z)")
    print("2) Población (asc/desc)")
    print("3) Superficie (asc/desc)")
    opcion = leer_texto_no_vacio("Opción: ")

    if opcion == "1":
        ordenados = sorted(lista_paises, key=clave_nombre)
        imprimir_tabla(ordenados)
        return

    if opcion == "2":
        sentido = leer_texto_no_vacio("Ascendente (A) / Descendente (D): ").strip().upper()
        descendente = (sentido == "D")
        ordenados = sorted(lista_paises, key=clave_poblacion, reverse=descendente)
        imprimir_tabla(ordenados)
        return

    if opcion == "3":
        sentido = leer_texto_no_vacio("Ascendente (A) / Descendente (D): ").strip().upper()
        descendente = (sentido == "D")
        ordenados = sorted(lista_paises, key=clave_superficie, reverse=descendente)
        imprimir_tabla(ordenados)
        return

    print("Opción inválida.")


# ============================================================
# ======================= BLOQUE ABM (Altas, Bajas y Modificaciones) =================
# ============================================================

# ABM: agregar un país (evita duplicados por nombre)
def agregar_pais(lista_paises: list) -> None:
    imprimir_titulo("Agregar país")
    nombre = normalizar_cadena(leer_texto_no_vacio("Nombre: "))

    # Revisar duplicado por nombre (insensible a mayúsculas)
    existe = False
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            existe = True
            break

    if existe:
        print("Ya existe un país con ese nombre.")
        return

    poblacion = leer_entero_no_negativo("Población (entero): ")
    superficie = leer_entero_no_negativo("Superficie en km² (entero): ")
    continente = normalizar_cadena(leer_texto_no_vacio("Continente: "))

    pais_nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(pais_nuevo)
    print("País agregado correctamente.")

# ABM: actualizar población y superficie de un país existente
def actualizar_pais(lista_paises: list) -> None:
    imprimir_titulo("Actualizar país")
    nombre = leer_texto_no_vacio("Nombre (coincidencia exacta): ")

    indice_encontrado = -1
    for i in range(len(lista_paises)):
        if lista_paises[i]["nombre"].lower() == nombre.lower():
            indice_encontrado = i
            break

    if indice_encontrado == -1:
        print("No se encontró el país.")
        return

    pais = lista_paises[indice_encontrado]
    print("Actualizando '{}': población actual {}, superficie actual {}"
          .format(pais["nombre"], pais["poblacion"], pais["superficie"]))

    nueva_poblacion = leer_entero_no_negativo("Nueva población: ")
    nueva_superficie = leer_entero_no_negativo("Nueva superficie: ")

    lista_paises[indice_encontrado]["poblacion"] = nueva_poblacion
    lista_paises[indice_encontrado]["superficie"] = nueva_superficie
    print("Datos actualizados.")

# ABM: mostrar todos los países en tabla
def ver_todos(lista_paises: list) -> None:
    imprimir_titulo("Listado de países")
    imprimir_tabla(lista_paises)


# ============================================================
# ====================== BLOQUE FILTROS ======================
# ============================================================

# FILTROS: por continente (igualdad estricta, insensible a mayúsculas)
def filtrar_por_continente(lista_paises: list) -> None:
    imprimir_titulo("Filtrar por continente")
    cont = leer_texto_no_vacio("Continente: ").lower()
    resultados = []
    for p in lista_paises:
        if p["continente"].lower() == cont:
            resultados.append(p)
    imprimir_tabla(resultados)

# FILTROS: por rango numérico (población/superficie)
def filtrar_por_rango(lista_paises: list, campo: str) -> None:
    imprimir_titulo("Filtrar por rango de " + campo)
    minimo = leer_entero_no_negativo("Mínimo: ")
    maximo = leer_entero_no_negativo("Máximo: ")
    if maximo < minimo:
        print("El máximo no puede ser menor que el mínimo.")
        return
    resultados = []
    for p in lista_paises:
        valor = p[campo]
        if minimo <= valor <= maximo:
            resultados.append(p)
    imprimir_tabla(resultados)


# ============================================================
# =================== BLOQUE ESTADÍSTICAS ====================
# ============================================================

# ESTADÍSTICAS: mayor/menor población, promedios y conteo por continente
def mostrar_estadisticas(lista_paises: list) -> None:
    imprimir_titulo("Estadísticas")
    if not lista_paises:
        print("No hay datos.")
        return

    # Mayor y menor población
    pais_mayor = lista_paises[0]
    for p in lista_paises:
        if p["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = p

    pais_menor = lista_paises[0]
    for p in lista_paises:
        if p["poblacion"] < pais_menor["poblacion"]:
            pais_menor = p

    # Promedios
    acumulado_poblacion = 0
    acumulado_superficie = 0
    for p in lista_paises:
        acumulado_poblacion += p["poblacion"]
        acumulado_superficie += p["superficie"]

    promedio_poblacion = int(acumulado_poblacion / len(lista_paises))
    promedio_superficie = int(acumulado_superficie / len(lista_paises))

    # Conteo por continente
    conteo = {}
    for p in lista_paises:
        cont = p["continente"]
        if cont in conteo:
            conteo[cont] += 1
        else:
            conteo[cont] = 1

    print("País con mayor población: {} ({})".format(pais_mayor['nombre'], pais_mayor['poblacion']))
    print("País con menor población: {} ({})".format(pais_menor['nombre'], pais_menor['poblacion']))
    print("Promedio de población: {}".format(promedio_poblacion))
    print("Promedio de superficie: {} km²".format(promedio_superficie))
    print("\nCantidad de países por continente:")
    # ordenar por nombre de continente
    continentes_ordenados = list(conteo.items())
    for i in range(len(continentes_ordenados)):
        for j in range(0, len(continentes_ordenados) - i - 1):
            if continentes_ordenados[j][0].lower() > continentes_ordenados[j + 1][0].lower():
                aux = continentes_ordenados[j]
                continentes_ordenados[j] = continentes_ordenados[j + 1]
                continentes_ordenados[j + 1] = aux
    for par in continentes_ordenados:
        print("  - {}: {}".format(par[0], par[1]))


# ============================================================
# ======================== BLOQUE MAIN =======================
# ============================================================

def menu_principal() -> None:
    lista_paises = cargar_desde_csv(ARCHIVO_CSV)

    salir = False
    while not salir:
        imprimir_titulo("Gestión de Países - Menú Principal")
        print("1) Agregar país")
        print("2) Actualizar población y superficie de un país")
        print("3) Buscar país por nombre")
        print("4) Filtrar países por continente")
        print("5) Filtrar países por rango de población")
        print("6) Filtrar países por rango de superficie")
        print("7) Ordenar países")
        print("8) Mostrar estadísticas")
        print("9) Ver todos")
        print("S) Guardar y salir")
        opcion = leer_texto_no_vacio("Opción: ").strip().upper()

        match opcion:
            case "1":
                agregar_pais(lista_paises)
            case "2":
                actualizar_pais(lista_paises)
            case "3":
                buscar_por_nombre(lista_paises)
            case "4":
                filtrar_por_continente(lista_paises)
            case "5":
                filtrar_por_rango(lista_paises, "poblacion")
            case "6":
                filtrar_por_rango(lista_paises, "superficie")
            case "7":
                ordenar_paises(lista_paises)
            case "8":
                mostrar_estadisticas(lista_paises)
            case "9":
                ver_todos(lista_paises)
            case "S":
                guardar_a_csv(lista_paises, ARCHIVO_CSV)
                print("Datos guardados. Hasta luego.")
                salir = True
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    menu_principal()
