import random
import time
import bisect
import os

# --- CONFIGURACIÓN ---
FILE_NAME = "datos.txt"
TOTAL_DATOS = 10_000_000
RANGO = (-50_000_000, 50_000_000)

# 1. GENERAR 10 MILLONES DE NÚMEROS Y GUARDAR EN TXT
if not os.path.exists(FILE_NAME):
    print(f"Generando {TOTAL_DATOS} números... esto puede tardar unos segundos.")
    with open(FILE_NAME, "w") as f:
        for _ in range(TOTAL_DATOS):
            f.write(f"{random.randint(*RANGO)}\n")
    print("✅ Archivo generado con éxito.")
else:
    print("✅ El archivo ya existe, saltando generación.")

# 2. CARGAR DATOS Y CONSTRUIR ESTRUCTURAS
print("Cargando datos en memoria...")
with open(FILE_NAME, "r") as f:
    # Esta es la lista base
    lista_base = [int(linea.strip()) for linea in f]

print("Construyendo Tabla Hash...")
tabla_hash = set(lista_base)  # Estructura 1: Tabla Hash

print("Construyendo Arreglo Ordenado...")
lista_ordenada = sorted(lista_base)  # Estructura 2: Arreglo Ordenado

# 3. BÚSQUEDA INTERACTIVA (USUARIO)
print("\n" + "="*40)
print("🔎 BUSCADOR INTERACTIVO")
while True:
    entrada = input("Ingresa un número para buscar (o 'salir'): ")
    if entrada.lower() == 'salir': break
    try:
        num = int(entrada)
        if num in tabla_hash: print(f"✅ El número {num} SÍ está en la lista.")
        else: print(f"❌ El número {num} NO se encontró.")
    except ValueError: print("⚠️ Por favor ingresa un número válido.")

# 4. EJECUTAR 1,000 BÚSQUEDAS AUTOMÁTICAS Y MEDIR TIEMPO
print("\n" + "="*40)
print("📊 EJECUTANDO PRUEBAS DE RENDIMIENTO...")
busquedas_azar = [random.randint(*RANGO) for _ in range(1000)]

# Medir Tabla Hash
inicio = time.perf_counter()
for n in busquedas_azar:
    _ = n in tabla_hash
t_hash = (time.perf_counter() - inicio) / 1000 * 1000 # Promedio en ms

# Medir Arreglo Ordenado (Búsqueda Binaria)
inicio = time.perf_counter()
for n in busquedas_azar:
    _ = bisect.bisect_left(lista_ordenada, n)
t_array = (time.perf_counter() - inicio) / 1000 * 1000 # Promedio en ms

# 5. PRESENTAR TABLA COMPARATIVA EN CONSOLA
print("\n--- RESULTADOS PARA TU INFORME ---")
print(f"{'Estructura':<20} | {'Tiempo Promedio':<18} | {'Memoria':<10} | {'Complejidad'}")
print("-" * 70)
print(f"{'Tabla Hash':<20} | {t_hash:>15.6f} ms | {'Alta':<10} | O(1)")
print(f"{'Arreglo Ordenado':<20} | {t_array:>15.6f} ms | {'Media':<10} | O(log n)")