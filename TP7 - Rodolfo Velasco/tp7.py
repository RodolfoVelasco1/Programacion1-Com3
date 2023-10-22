#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP7

from tp7_funciones import *


#EJERCICIO 1

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original: ", numbers)
bubble_sort(numbers)
print("Ordenamiento de burbuja (Bubble Sort): ", numbers)


#EJERCICIO 2

fruits = ["ananá", "zanahoria", "manzana", "banana", "frutilla"]
print("Lista Original:", fruits)
selection_sort(fruits)
print("Orden de selección (Selection Sort):", fruits)


#EJERCICIO 3

ordered_list = []
book_list = [{"title":"El principito", "author":"Antoine de Saint-Exupéry", "year":1943}, {"title":"El mago de oz", "author":"L. Frank Baum", "year":1900}, {"title":"El Eternauta", "author":"Héctor Germán Oesterheld", "year":1957}, {"title":"Tokio Blues", "author":"Haruki Murakami", "year":1987}, {"title":"El sabueso de los Baskerville", "author":"Arthur Conan Doyle", "year":1902}]
ordered_list = sorted(book_list, key=lambda x: x['year'])
print(ordered_list)


#EJERCICIO 4

string_list = ["Hola a todos", "Cómo están el día de hoy", "Bien", "Mal", "Mas o menos"]
insertion_sort(string_list)
print(string_list)


#EJERCICIO 5

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)
bubble_sort_desc(numbers)
print("Ordenamiento de burbuja (Bubble Sort) ORDEN DESCENDENTE: ", numbers)


#EJERCICIO 6

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original: ", numbers)
ordered_list = counting_sort(numbers)
print("Ordenamiento por Conteo (Counting Sort):", ordered_list)


#EJERCICIO 7

list = [5, "manzana", 3, "banana", 1, "ananá", 2, "zanahoria", 4, "naranja"]
print("Lista desordenada: ", list)
sorted_list = sorted(list, key=number_string_items)
print("Lista ordenada:", sorted_list)


#EJERCICIO 8

numbers = [5, 3, 8, 1, 2, 7, 4, 10, 6, 9]
print("Lista Original:", numbers)
merge_sort(numbers)
print("Combinar ordenamiento (Merge Sort): ", numbers)