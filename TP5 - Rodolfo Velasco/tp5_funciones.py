#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#EJERCICIO 1

def id_checker(a):  #Comprueba si la longitud del DNI es 7 u 8 dígitos
    if (a == 7 or a == 8):
        return True
    else:
        return False


def response(a):    #Imprime si es correcto o incorrecto
    if (a == True):
        print("Correcto.")
    else:
        print("Incorrecto. Inténtelo de nuevo.")
   

#EJERCICIO 2

def last_word(answer):      #Obtiene la longitud de la última palabra del mensaje. 
    list = answer.split()   #En una lista guarda cada palabra del mensaje
    list_length = int(len(list))    #Obtenemos la longitud de la lista
    word = list[list_length - 1]    #Vamos al último elemento de la lista
    length = str(len(word))     #Obtenemos su longitud
    return length


#EJERCICIO 3

def name_id(name_list, id_number):  #Esta función crea un identificador único formado por el primer nombre, la longitud de su apelllido y los 3 primeros números del DNI
    first_name = name_list[0]
    if (len(name_list) == 2):
        last_name = name_list[1]
    elif(len(name_list) == 3):
        last_name = name_list[2]
    length = str(len(last_name))
    id_number = str(id_number[0] + id_number[1] + id_number[2])
    new_name = first_name + length + id_number
    return new_name


#EJERCICIO 4

def multiple(number1, number2): #Comprueba si el primer número es múltiplo del segundo
    if (number1 % number2 == 0):
        return True
    else:
        return False


#EJERCICIO 5

def temperatura_media(max, min):    #Calcula la temperatura media
    media = (max + min) / 2
    return media


#EJERCICIO 6

def add_space(text):        #Agrega un espacio entre cada caracter
    space_text = text.replace(" ", "")
    space_text = " ".join(space_text)
    return space_text


#EJERCICIO 7

def max_min(number_list, list_length):      #Encuentra el mayor y el menor número en la lista
    max =  number_list[0]
    min =  number_list[0]
    for i in range(list_length):
        if ( number_list[i] > max):
            max =  number_list[i]
        elif ( number_list[i] < min):
            min =  number_list[i]
    return [max, min]


#EJERCICIO 8

def area_perimeter(radio, pi):      #Calcula el área y el perímetro de la circunferencia
    area = (radio**2) * pi
    print("El area de la circunferencia es: " + str(area))
    perimeter = (2*pi)*radio
    print("El perímetro de la circunferencia es: " + str(perimeter))
    return


#EJERCICIO 9

def login(user_name, password, attempt):    #Comprueba si el nombre de usuario y contraseña son correctos
    if (user_name == "usuario1" and password == "asdasd"):
        answer = True
    else:
        answer = False
        attempt = attempt + 1
    return answer, attempt


#EJERCICIO 10

def total_price(products, discounts):       #Calcula el total a pagar con descuentos
    total = 0
    for product, price in products.items():
        if (product in discounts):
         item_discount = discounts[product]
         item_price = price - (price * item_discount / 100)
         total = total + item_price
        else:
           total = total
    return total


#EJERCICIO 11

def result(double, numbers):    #Esta función envía la lista de números a la función "double" la cual nos duplicará los números de la lista. Luego, esta función creará una lista nueva para guardar los resultados que reciba de la función "double".
    new_list = []
    new_list = double(numbers)
    return new_list


def double(numbers):        #Esta función nos da el doble de cada número de la lista de números.
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers


#EJERCICIO 12

def string_dictionary(text):    #Crea un diccionario con las palabras y sus longitudes
    dictionary = {}
    words = text.split(" ")
    for word in words:
        dictionary[word] = dictionary.get(word, len(word))
    return dictionary


#EJERCICIO 13
import math
def module_calculation(vector): #Calcula el módulo del vector
    module = math.sqrt((vector[0]**2) + (vector[1] **2 ))
    return module


#EJERCICIO 14

def prime_number(number):       #Comprueba si el número es primo o no
    counter = 0
    i = 1
    while (i <= number + 200):
        if (number % i == 0):
            counter = counter + 1
        i = i+1
    if (counter == 2):
        return True
    else:
        return False


#EJERCICIO 15

def check_factorial(number):        #Calcula la factorial del número ingresado
    factorial = number
    while (number >= 2):
        number = number - 1
        factorial = factorial * number
    return factorial


#EJERCICIO 16

def check_digit(number, digit):     #Obtiene la cantidad de veces que aparece un dígito en un número
    amount = 0
    for i in range(len(number)):
       if (number[i] == digit):
            amount = amount + 1
    return amount


#EJERCICIO 17

def prime_number(number):       #Comprueba si el número es primo
    counter = 0
    index = 1
    while (index <= number):
        if (number % index == 0):
            counter = counter + 1
        index = index + 1
    if (counter == 2):
        return True
    else:
        return False


def digit_addition(number):     #Suma los dígitos del número
    number = str(number)
    length = len(number)
    addition = 0
    for i in range(length):
        addition = addition + int(number[i])
    return addition


def asking_digit():     #Le pide al usuario que ingrese un dígito
    while (True):
        digit = int(input("Ingrese un dígito: "))
        if (digit > 9 or digit < 0):
            print("Error: ingrese un solo dígito.")
        else:
            return digit


def frequency(number, digit):  #Cuenta la cantidad de veces que aparece el dígito en el número
    counter = 0
    for i in range(len(number)):
        if (number[i] == digit):
            counter = counter + 1
    return counter


def biggest_number(biggest, number):    #Encuentra el número más grande
    if (number > biggest):
        biggest = number
    return biggest


def biggest_factorial(biggest):     #Calcula el factorial del número más grande
    factorial = biggest
    while (biggest >= 2):
        biggest = biggest - 1
        factorial = factorial * biggest
    return factorial
