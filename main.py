"""
SISTEMA OPTOGESTION
Proyecto Final - Programación I - Universidad CES

Programa de consola para registrar, consultar y procesar los datos de
pacientes atendidos en jornadas visuales. Los datos se guardan en pacientes.json
"""

import json
import os

ARCHIVO = "pacientes.json"


# ---------------------------------------------------------------
# ALMACENAMIENTO (JSON)
# ---------------------------------------------------------------
def cargar_pacientes():
    """Inicia con una lista vacía y la llena con lo que haya en el JSON."""
    pacientes = []
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as archivo:
                pacientes = json.load(archivo)
        except json.JSONDecodeError:
            print("Aviso: el archivo JSON está dañado. Se inicia con lista vacía.")
            pacientes = []
    return pacientes


def guardar_pacientes(pacientes):
    """Guarda la lista de diccionarios en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(pacientes, archivo, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# ---------------------------------------------------------------
def pedir_nombre():
    """Pide un nombre que no esté vacío."""
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre != "":
            return nombre
        print("El nombre no puede estar vacío.")


def pedir_edad():
    """Pide una edad entera entre 1 y 120."""
    while True:
        try:
            edad = int(input("Edad (1-120): "))
            if 1 <= edad <= 120:
                return edad
            print("La edad debe estar entre 1 y 120.")
        except ValueError:
            print("Ingrese un número entero válido.")


def pedir_sexo():
    """Pide el sexo: F o M."""
    while True:
        sexo = input("Sexo (F/M): ").strip().upper()
        if sexo in ("F", "M"):
            return sexo
        print("Ingrese F o M.")


def pedir_booleano(mensaje):
    """Pide una respuesta que solo admite True o False."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "true":
            return True
        if respuesta == "false":
            return False
        print("Respuesta inválida. Escriba solo True o False.")


def generar_id(pacientes):
    """Genera un id único con formato P001, P002, ..."""
    mayor = 0
    for paciente in pacientes:
        numero = int(paciente["id"][1:])
        if numero > mayor:
            mayor = numero
    return "P" + str(mayor + 1).zfill(3)


# ---------------------------------------------------------------
# MÓDULOS DEL MENÚ
# ---------------------------------------------------------------
def registrar_paciente(pacientes):
    """Módulo 1: registra un paciente y lo guarda en el JSON."""
    print("\n--- REGISTRAR PACIENTE ---")
    nuevo = {
        "id": generar_id(pacientes),
        "nombre": pedir_nombre(),
        "edad": pedir_edad(),
        "sexo": pedir_sexo(),
        "usa_correccion": pedir_booleano("¿Usa corrección visual? (True/False): "),
    }
    pacientes.append(nuevo)
    guardar_pacientes(pacientes)
    print("Paciente registrado con el id", nuevo["id"])


def consultar_paciente(pacientes):
    """Módulo 2: busca un paciente por su id y muestra todos sus datos."""
    print("\n--- CONSULTAR PACIENTE ---")
    id_buscado = input("Ingrese el id del paciente (ej. P001): ").strip().upper()
    for paciente in pacientes:
        if paciente["id"] == id_buscado:
            print("\nID:", paciente["id"])
            print("Nombre:", paciente["nombre"])
            print("Edad:", paciente["edad"])
            print("Sexo:", paciente["sexo"])
            print("Usa corrección visual:", paciente["usa_correccion"])
            return
    print("No existe un paciente con ese id.")


def mostrar_pacientes(pacientes):
    """Módulo 3: muestra los nombres de todos los pacientes."""
    print("\n--- PACIENTES REGISTRADOS ---")
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    for paciente in pacientes:
        print("-", paciente["nombre"])


def buscar_con_correccion(pacientes):
    """Módulo 4: muestra los nombres de quienes usan corrección visual."""
    print("\n--- PACIENTES CON CORRECCIÓN VISUAL ---")
    encontrados = 0
    for paciente in pacientes:
        if paciente["usa_correccion"] == True:
            print("-", paciente["nombre"])
            encontrados += 1
    if encontrados == 0:
        print("Ningún paciente usa corrección visual.")


def generar_estadisticas(pacientes):
    """Módulo 5: total, edad promedio y cantidad con corrección visual."""
    print("\n--- ESTADÍSTICAS DE LA JORNADA ---")
    total = len(pacientes)
    if total == 0:
        print("No hay pacientes registrados; no se pueden calcular estadísticas.")
        return

    suma_edades = 0
    con_correccion = 0
    for paciente in pacientes:
        suma_edades += paciente["edad"]
        if paciente["usa_correccion"]:
            con_correccion += 1

    promedio = suma_edades / total
    print("Total de pacientes:", total)
    print("Edad promedio:", round(promedio, 1))
    print("Pacientes con corrección visual:", con_correccion)




# ==========================
# MENU PRINCIPAL
# ==========================

def menu():

    pacientes = cargar_pacientes()

    while True:

        print("\n====================================")
        print("       SISTEMA OPTOGESTION")
        print("====================================")
        print("1. Registrar paciente")
        print("2. Consultar paciente")
        print("3. Mostrar pacientes registrados")
        print("4. Buscar pacientes con correccion visual")
        print("5. Generar estadisticas")
        print("6. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            registrar_paciente(pacientes)

        elif opcion == "2":

            consultar_paciente(pacientes)

        elif opcion == "3":

            mostrar_pacientes(pacientes)

        elif opcion == "4":

            buscar_correccion_visual(pacientes)

        elif opcion == "5":

            generar_estadisticas(pacientes)

        elif opcion == "6":

            guardar_pacientes(pacientes)
            print("Datos guardados. ¡Hasta pronto!")
            break

        else:

            print("Opcion invalida. Elija un numero del 1 al 6.")


# ==========================
# EJECUCION DEL PROGRAMA
# ==========================

if __name__ == "__main__":
    menu()