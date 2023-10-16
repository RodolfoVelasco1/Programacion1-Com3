#Alumno: Rodolfo Nicolás Velasco Fessler

#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

from ordenamiento_busqueda_funciones import *

print("--------------------------------------------------------")

#Ordenar en orden ascendente
print("Ordenar en orden ascendente:")

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original: ", numbers)

bubble_sort(numbers)
print("Ordenamiento de burbuja (Bubble Sort): ", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

selection_sort(numbers)
print("Orden de selección (Selection Sort):", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

insertion_sort(numbers)
print("Tipo de inserción (Insert Sort): ", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

merge_sort(numbers)
print("Combinar ordenamiento (Merge Sort): ", numbers)

print("-----------------------------------------------------------")

#Ordenar en orden descendente
print("Ordenar en orden descendente:")

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

bubble_sort_desc(numbers)
print("Ordenamiento de burbuja (Bubble Sort): ", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

selection_sort_desc(numbers)
print("Orden de selección (Selection Sort): ", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

insertion_sort_desc(numbers)
print("Tipo de inserción (Insert Sort): ", numbers)

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)

merge_sort_desc(numbers)
print("Combinar ordenamiento (Merge Sort): ", numbers)

print("--------------------------------------------------------")

#BÚSQUEDA LINEAL & BÚSQUEDA BINARIA

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
target = 7

linear_result = linear_search(numbers, target)
binary_result = binary_search(numbers, target)

if linear_result != -1:
    print(f"Búsqueda Lineal: Se encontró el objetivo en el índice {linear_result}.")
else:
    print("Búsqueda Lineal: No se encontró el objetivo.")

if binary_result != -1:
    print(f"Búsqueda Binaria: Se encontró el objetivo en el índice {binary_result}.")
else:
    print("Búsqueda Binaria: No se encontró el objetivo.")


