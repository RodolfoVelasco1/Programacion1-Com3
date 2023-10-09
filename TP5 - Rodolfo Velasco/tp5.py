#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#EJERCICIO 1

from tp5_funciones import *

answer = False
while(answer == False):
    id_number = input("Ingrese su número de DNI: ") #El usuario ingresa su DNI
    length = len(id_number)
    answer = id_checker(length) #Comprueba si la longitud del DNI es 7 u 8 dígitos
    response(answer)    #Imprime si es correcto o incorrecto
print("Su número de DNI es: " + id_number)


#EJERCICIO 2

answer = input("Ingrese un mensaje: ")  #El usuario ingresa un mensaje
length = last_word(answer)  #Obtiene la longitud de la última palabra del mensaje
print("La última palabra ingresada en el string tiene " + length + " letras.")


#EJERCICIO 3

while (True):       #El usuario debe ingresar 1 o 2 nombres y un solo apellido
    name = input("Ingrese su nombre y su primer apellido: ")
    name_list = name.split()
    if (len(name_list) != 2 and len(name_list) != 3):
        print("Error. Ingrese 1 o 2 nombres y 1 solo apellido.")
    else:
        break
while (True):       #El usuario ingresa su DNI
    id_number = input("Ingrese su número de DNI: ")
    if (len(id_number) != 7 and len(id_number) != 8):
        print("Error. El número de DNI debe tener 7 u 8 números.")
    else:
        break
new_name = name_id(name_list, id_number)    #Esta función crea un identificador único formado por el primer nombre, la longitud de su apelllido y los 3 primeros números del DNI
print("Su identificador único es: " + new_name)


#EJERCICIO 4

number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese otro número: "))
answer = multiple(number1, number2)     #Comprueba si el primer número es múltiplo del segundo
if (answer == True):
    print("El número " + str(number1) + " es múltiplo de " + str(number2))
else:
    print("El número " + str(number1) + " NO es múltiplo de " + str(number2))


#EJERCICIO 5

days = int(input("Ingrese la cantidad de días: "))
for i in range(days):
    max = int(input("Ingrese la temperatura máxima del día #" + str(i+1) + ": "))
    min = int(input("Ingrese la temperatura mínima del día #" + str(i+1) + ": "))
    media = temperatura_media(max, min)     #Calcula la temperatura media
    print("La temperatura media del día #" + str(i+1) + " es de " + str(media) + "°.")


#EJERCICIO 6

text = input("Ingrese un mensaje: ")
space_text = add_space(text)
print(space_text)   #Agrega un espacio entre cada letra


#EJERCICIO 7

list_length = int(input("Ingrese el tamaño de la lista: "))
number_list = []
answer_list = []
for i in range(list_length):
    number = int(input("Ingrese un número: "))
    number_list.append(number)
answer_list = max_min(number_list, list_length) #Encuentra el mayor y el menor número en la lista
print("El mayor número de la lista es " + str(answer_list[0]))
print("El menor número de la lista es " + str(answer_list[1]))


#EJERCICIO 8

import math
radio = int(input("Ingrese el radio de la circunferencia: "))
pi = math.pi
area_perimeter = area_perimeter(radio, pi)  #Calcula el área y el perímetro de la circunferencia


#EJERCICIO 9

attempt = 0
while (True):
    user_name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    answer, attempt = login(user_name, password, attempt)   #Comprueba si el nombre de usuario y contraseña son correctos
    if (answer == True):
        print("Nombre de usuario y contraseña correcta.")
        print("Bienvenido, " + user_name)
        break
    else:
        print("Ha ingresado datos erroneos.")
        print("Intento # " + str(attempt) + ". Inténtelo de nuevo.")


#EJERCICIO 10

products = {"product1": 500, "product2": 1500, "product3": 700, "product4": 2380, "product5": 5400}
discounts = {"product1": 10, "product2": 50, "product3": 20, "product4": 25, "product5": 70}
total = total_price(products, discounts)        #Calcula el total a pagar con descuentos
print("El total a pagar es de: $" + str(total)) 


#EJERCICIO 11

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original: ")
print(numbers)
numbers = result(double, numbers)   #Esta función recibe otra función y una lista. La otra función nos da el doble de cada número en la lista. Esta función guarda cada resultado en una lista.
print("Nueva lista:")
print(numbers)


#EJERCICIO 12

dictionary = {}
text = input("Ingrese un mensaje: ")
dictionary = string_dictionary(text) #Crea un diccionario con las palabras y sus longitudes
print(dictionary)


#EJERCICIO 13

import math
vector = [3,-4]
print("El vector es igual a: " + str(vector))   #Calcula el módulo del vector
module = module_calculation(vector)
print("El módulo de dicho vector es igual a: " + str(module))


#EJERCICIO 14

number = int(input("Ingrese un número: "))
answer = prime_number(number)   #Comprueba si el número es primo o no
if (answer == True):
    print("El número " + str(number) + " es primo.")
else:
    print("El número " + str(number) + " no es primo.")


#EJERCICIO 15

attempts = 0
answer = 0
while (True):
    print("1. Jugar | 2. Salir")
    answer = (int(input("Respuesta: ")))
    if (answer == 1):
        number = int(input("Ingrese un número: "))
        factorial = check_factorial(number)     #Calcula la factorial del número ingresado
        print("La factorial de " + str(number) + " es igual a " + str(factorial))
        attempts = attempts + 1
    elif (answer == 2):
        print("Gracias por jugar. Vuelve pronto.")
        break
    else:
        print("Ingresó un valor incorrecto. Intente de nuevo.")
print("La cantidad de veces que jugó fueron: " + str(attempts))


#EJERCICIO 16

number = input("Ingrese un número: ")
while (True):
    digit = input("Ingrese un dígito: ")
    if (len(digit) == 1):
        break
    else:
        print("Error, ingrese un solo dígito.")
amount = check_digit(number, digit)     #Obtiene la cantidad de veces que aparece un dígito en un número
print("¿Cuántas veces aparece el dígito " + digit + " en el número " + number + "?")
print("Cantidad de veces que aparece: " + str(amount))


#EJERCICIO 17

biggest = 0
while(True):
    number = int(input("Ingrese un número primo: "))
    prime = prime_number(number)    #Comprueba si el número es primo
    if (prime == True):
        print("El número es primo.")
    else:
        print("El número no es primo.")
        print("Programa finalizado.")
        break
    addition = digit_addition(number)       #Suma los dígitos del número
    print("La suma de sus dígitos da " + str(addition))
    digit = asking_digit()      #Le pide al usuario que ingrese un dígito
    counter = frequency(str(number), str(digit))        #Cuenta la cantidad de veces que aparece el dígito en el número
    print("En el número " + str(number) + " el dígito " + str(digit) + " se encuentra " + str(counter) + " veces.")
    biggest = biggest_number(biggest, number)       #Encuentra el número más grande


print("El número más grande es " + str(biggest))
factorial = biggest_factorial(biggest)      #Calcula el factorial del número más grande
print("La factorial de " + str(biggest) + " es igual a " + str(factorial))
 