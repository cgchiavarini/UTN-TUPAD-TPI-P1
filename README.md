# 💻 Programación 1

Noviembre 2025

**Tecnicatura Universitaria en Programación**
📍 _Universidad Tecnológica Nacional_

## ✨ Estudiantes

- **Nombre:** Chiavarini Carlos
- **Comisión:** A2025-3
- **Nombre:** Zerpa Alexis Cristian Boris
- **Comisión:** A2025-10

## 👨‍🏫 Docentes

- **Coordinador:** Alberto Cortez
- **Profesores:** Cinthia Rigoni y Ariel Enferrel
- **Tutores:** Brian Lara y Martina Zabala

# 🧾 Trabajo Práctico Integrador – Gestión de Datos de Países en Python

## 📘 Descripción del Proyecto

Este proyecto forma parte del **Trabajo Práctico Integrador (TPI)** de la asignatura **Programación I** de la **Tecnicatura Universitaria en Programación**.
El objetivo principal es desarrollar un sistema en **Python** que permita **gestionar, analizar y persistir información sobre distintos países**.

El programa implementa un menú interactivo en consola, mediante el cual el usuario puede:

- Registrar nuevos países.
- Modificar o actualizar datos existentes.
- Buscar, filtrar y ordenar registros.
- Calcular estadísticas como promedios, máximos y mínimos.
- Guardar y recuperar los datos desde un archivo CSV.

El desarrollo aplica los principios de la **programación estructurada**, el uso de **funciones modulares**, **validaciones de entrada**, y la **persistencia de datos** mediante archivos.

## 🧩 Estructura del Proyecto

📦 **GestionPaises**
📜 Trabajo_Practico_Integrador.py # Código principal en Python
📜 paises.csv # Archivo con los datos de ejemplo
📜 README.md # Documentación del proyecto

**Bloques principales del programa:**

- **Main:** flujo general y menú interactivo.
- **Datos:** manejo del archivo CSV (lectura/escritura).
- **Búsquedas:** localización de países según criterios.
- **Filtros:** selección por continente o población.
- **Ordenamiento:** orden alfabético o por valores numéricos.
- **Estadísticas:** cálculo de promedios y extremos.
- **Validaciones:** control de entradas y consistencia de datos.

## ⚙️ Instrucciones de Ejecución

1. **Requisitos previos:**

   - Python 3.10 o superior (recomendado Python 3.12)
   - Sistema operativo Windows, Linux o macOS
   - Archivo `paises.csv` en la misma carpeta que el script principal

2. **Ejecutar el programa:**

   ```bash
   python Trabajo_Practico_Integrador.py

   ```

3. **Interacción:**

   - Seleccioná una opción del menú escribiendo su número.
   - Seguí las instrucciones en pantalla para cargar, buscar o modificar datos.
   - Al cerrar el programa, los cambios se guardan automáticamente en el archivo CSV.

## 🔗 Enlaces

🎥 Video explicativo: Ver presentación
💻 Repositorio GitHub: https://github.com/cgchiavarini/UTN-TUPAD-TPI-P1

## 🧠 Ejemplo de Entrada y Salida

📥 **Entrada de datos:**
Ingrese el nombre del país: Argentina
Ingrese la población: 45376763
Ingrese la superficie: 2780400
Ingrese el continente: América

📤 **Salida esperada:**
País agregado correctamente.

Listado de países:

1. Argentina – América – Población: 45376763 – Superficie: 2780400 km²
2. Brasil – América – Población: 213993437 – Superficie: 8515767 km²

Promedio de población: 129185600
País con mayor población: Brasil

## 📚 Créditos

Este proyecto fue desarrollado como parte de la evaluación final integradora de la asignatura Programación I, aplicando los conocimientos sobre estructuras de datos, funciones, control de flujo, modularización y manejo de archivos.
El código y la documentación fueron elaborados por los estudiantes del grupo con fines educativos y académicos.
