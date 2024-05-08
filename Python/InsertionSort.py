import random
import time

def insertionSort(arr):
    n = len(arr)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def llenarArreglo(n):
    arrTemp = []
    for i in range(n):
        arrTemp.append(random.randint(0, 10000))
    return arrTemp

# Generar la lista de números aleatorios
arr = llenarArreglo(1000000)

# Tomar el tiempo antes de ejecutar el algoritmo
start_time = time.time()

# Ejecutar el algoritmo de ordenamiento por inserción
insertionSort(arr)

# Tomar el tiempo después de ejecutar el algoritmo
end_time = time.time()

# Calcular el tiempo de ejecución del algoritmo
execution_time = end_time - start_time

print("Tiempo de ejecución del algoritmo de inserción:", execution_time)