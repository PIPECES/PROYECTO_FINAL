# Sistema OptoGestión

Proyecto Final de **Programación I** – Universidad CES.

## Descripción
Programa de consola en Python para un centro universitario de atención optométrica.
Permite registrar, almacenar, consultar y procesar los datos de pacientes atendidos
en jornadas visuales. La información se guarda de forma permanente en `pacientes.json`.

## Funcionalidades
1. **Registrar paciente**: pide nombre, edad (1–120), sexo (F/M) y uso de corrección visual (solo `True`/`False`). El id (P001, P002…) se genera automáticamente y es único.
2. **Consultar paciente**: busca por id y muestra todos sus datos, o avisa si no existe.
3. **Mostrar pacientes registrados**: recorre la lista con `for` e imprime los nombres.
4. **Buscar pacientes con corrección visual**: muestra los nombres o informa si ninguno cumple.
5. **Generar estadísticas**: total de pacientes, edad promedio y cantidad con corrección visual (evita la división entre cero).
6. **Salir**: guarda y termina. El menú se repite hasta elegir esta opción.

## Estructura del proyecto
```
OptoGestion/
├── main.py          # Código fuente
├── pacientes.json   # Registros ficticios (6 pacientes)
└── README.md        # Este archivo
```

## Requisitos técnicos cumplidos
Consola, funciones, listas y diccionarios, condicionales y ciclos, archivos JSON,
ejecución continua hasta elegir la opción de salida y archivo con al menos 5 pacientes.

## Instrucciones de ejecución
1. Instalar Python 3.8 o superior.
2. Descargar la carpeta y mantener `main.py` y `pacientes.json` juntos.
3. Abrir una terminal en esa carpeta y ejecutar:
   ```
   python main.py
   ```
   (en algunos sistemas: `python3 main.py`)

## Estructura de un paciente
```python
{"id": "P001", "nombre": "Laura Gómez", "edad": 24, "sexo": "F", "usa_correccion": True}
```
