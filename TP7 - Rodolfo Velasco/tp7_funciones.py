#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP7 - FUNCIONES

#EJERCICIO 1

def bubble_sort(numbers):   #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


#EJERCICIO 2

def selection_sort(fruits):    #Orden de selección
    n = len(fruits)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if fruits[j] < fruits[min_idx]:
                min_idx = j
        fruits[i], fruits[min_idx] = fruits[min_idx], fruits[i]


#EJERCICIO 4

def insertion_sort(list):       #Tipo de inserción
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and len(key) < len(list[j]):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


#EJERCICIO 5

def bubble_sort_desc(numbers):  #Ordenamiento de burbuja
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


#EJERCICIO 6

def counting_sort(numbers):	#Ordenamiento por conteo
    max_value = max(numbers)
    min_value = min(numbers)
    range_of_values = max_value - min_value + 1

    count = [0] * range_of_values
    output = [0] * len(numbers)

    for num in numbers:
        count[num - min_value] += 1

    for i in range(1, range_of_values):
        count[i] += count[i - 1]

    for num in reversed(numbers):
        output[count[num - min_value] - 1] = num
        count[num - min_value] -= 1

    return output


#EJERCICIO 7

def number_string_items(item):	#Ordenar lista con números enteros y Strings
    if isinstance(item, int):
        return (0, item)  # Tupla con 0 para números
    elif isinstance(item, str):
        return (1, item)  # Tupla con 1 para cadenas de texto


#EJERCICIO 8

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
