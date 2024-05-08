import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Selecciona el primer elemento como pivote
    left = [x for x in arr[1:] if x < pivot]  # Ignora el pivote
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x > pivot]  # Ignora el pivote
    return quicksort(left) + middle + quicksort(right)

# Función para medir el tiempo de ejecución de quicksort
def measure_time_quicksort(arr):
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    return end_time - start_time

# Función para generar un nuevo arreglo aleatorio
def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Ejecutar quicksort 2 veces con nuevos arreglos aleatorios y medir el tiempo promedio
total_time = 0
n = 10000000  # Cambia este valor según el tamaño del arreglo que desees probar
for _ in range(5):
    arr = generate_random_array(n)
    total_time += measure_time_quicksort(arr)
average_time = total_time / 5

print(f"Tiempo promedio de Quicksort para un arreglo de tamaño {n}: {average_time} segundos")
