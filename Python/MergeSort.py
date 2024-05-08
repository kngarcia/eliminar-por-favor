import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

# Generar una lista de números aleatorios
n = 10000000
random_list = [random.randint(1, 100) for _ in range(n)]

# Tomar el tiempo antes de ejecutar el algoritmo
start_time = time.time()

# Ordenar la lista utilizando merge sort
sorted_list = merge_sort(random_list)

# Tomar el tiempo después de ejecutar el algoritmo
end_time = time.time()

# Calcular el tiempo de ejecución
execution_time = end_time - start_time
print("Tiempo de ejecución del algoritmo de merge sort:", execution_time, "segundos")