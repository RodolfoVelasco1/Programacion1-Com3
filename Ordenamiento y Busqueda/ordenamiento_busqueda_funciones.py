#Alumno: Rodolfo Nicolás Velasco Fessler

#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#FUNCIONES

#ORDENAMIENTO

#ORDEN ASCENDENTE

def bubble_sort(numbers):   #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def selection_sort(numbers):    #Orden de selección
    n = len(numbers)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

def insertion_sort(numbers):       #Tipo de inserción
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

def merge_sort(numbers):    #Combinar ordenamiento
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

#ORDEN DESCENDENTE

def bubble_sort_desc(numbers):  #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def selection_sort_desc(numbers):   #Orden de selección
    n = len(numbers)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

def insertion_sort_desc(numbers):   #Tipo de inserción
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key > numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

def merge_sort_desc(numbers):   #Combinar ordenamiento
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left_half = numbers[:mid]
        right_half = numbers[mid:]

        merge_sort_desc(left_half)
        merge_sort_desc(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                numbers[k] = left_half[i]
                i += 1
            else:
                numbers[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            numbers[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            numbers[k] = right_half[j]
            j += 1
            k += 1

#BÚSQUEDA 

#BÚSQUEDA LINEAL

def linear_search(numbers, target):	#Busqueda Lineal
    for i, element in enumerate(numbers):
        if element == target:
            return i  #Devuelve el índice donde se encuentra el objetivo en la lista.
    return -1  #Devuelve -1 si no encuentra el objetivo.

#BÚSQUEDA BINARIA

def binary_search(numbers, target):	#Busqueda Binaria
    left, right = 0, len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = numbers[middle]

        if middle_value == target:
            return middle  #Devuelve el índice donde se encuentra el objetivo en la lista.
        elif middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1  #Devuelve -1 si no encuentra el objetivo.
