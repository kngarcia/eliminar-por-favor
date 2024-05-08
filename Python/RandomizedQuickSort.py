import time
import random

# Implementación de Randomized Quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Función para generar un nuevo arreglo aleatorio
def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Función para medir el tiempo promedio de Randomized Quicksort
def measure_average_time_randomized_quicksort(n, num_iterations):
    total_time = 0
    for _ in range(num_iterations):
        arr = generate_random_array(n)
        start_time = time.time()
        randomized_quicksort(arr, 0, len(arr) - 1)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / num_iterations

# Definir el tamaño del arreglo y el número de iteraciones
n = 1000000  # Tamaño del arreglo
num_iterations = 10  # Número de iteraciones

# Medir el tiempo promedio de Randomized Quicksort
average_time = measure_average_time_randomized_quicksort(n, num_iterations)
print(f"Tiempo promedio de Randomized Quicksort para un arreglo de tamaño {n}: {average_time} segundos")
print("hola")
print("como vas?")