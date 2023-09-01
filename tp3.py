#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio 1

word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

#Ejercicio 2

age = int(input("Ingrese su edad: "))
count_age = 1
while count_age <= age:
    print(count_age)
    count_age = count_age + 1

#Ejercicio 3

number = int(input("Ingrese un número entero positivo: "))
counter = 1
if (number < 0):
    print("El número ingresado es negativo.")
elif (number == 0):
    print("El número ingresado es 0, no hay números impares para mostrar.")
else:
    print(f"Los números impares que hay desde 1 al número {number} son:")
while counter <= number:
    if (counter % 2 != 0):
        print(counter, end =", ")
        counter = counter + 1
    else:
        counter = counter + 1
print(" \n ")

#Ejercicio 4

number = int(input("Ingrese un número entero positivo: "))
counter = 0
if (number < 0):
    print("El número ingresado es negativo.")
elif (number == 0):
    print("El número ingresado es 0, no habrá cuenta atrás.")
else:
    print(f"Cuenta atrás desde {number} hasta 0:")
while number >= counter:
    print(number, end =", ")
    number = number - 1

print(" \n ")

#Ejercicio 5

capital = int(input("¿Cuánto desea invertir?: $"))
interest = int(input("Ingrese el porcentaje de interés anual (sin el símbolo %): "))
years = int(input("¿Por cuántos años?: "))
for i in range(years):
    annual_interest = interest * capital / 100
    capital = capital + annual_interest
    if (i + 1 == 1):
        print(f"Luego de {i + 1} año, el capital obtenido de la inversión será de ${capital}")
    else:
        print(f"Luego de {i + 1} años, el capital obtenido de la inversión será de ${capital}")

#Ejercicio 6

number = int(input("Ingrese un número entero positivo: "))
counter = 1
if (number < 0):
    print("El número ingresado es negativo.")
elif (number == 0):
    print("El número ingresado es 0, no habrá triángulo.")
else:
    print("Aquí tiene un Triángulo Rectángulo:")

while counter <= number:
    for i in range(counter):
        print("*", end ="")
    print("\n")
    counter = counter + 1

#Ejercicio 7

table = 1
counter = 1
print("TABLAS DE MULTIPLICAR")
for i in range(10):
    print(" ")
    print(f"TABLA DEL {table}:")
    print(" ")
    while counter <= 10:
        print(f"{table}x{counter} = {table*counter}")
        counter = counter + 1
    counter = 1
    table = table + 1

#Ejercicio 8

number = int(input("Ingrese un número entero positivo: "))
counter = 1
odd = 0

if (number < 0):
    print("El número ingresado es negativo.")
elif (number == 0):
    print("El número ingresado es 0, no habrá triángulo.")
else:
    print("Aquí tiene un Triángulo Rectángulo:")

while counter <= number:
    if (counter % 2 != 0):
        odd = odd + 1
        counter = counter + 1
    else:
        counter = counter + 1

line = 1

for i in range(odd):
    counter = line
    while counter >= 1:
        if (counter % 2 != 0 and counter != 1):
            print(counter, end =" ")
            counter = counter - 2
        elif (counter % 2 != 0 and counter == 1):
            print(counter, "\n")
            break
    line = line + 2

#Ejercicio 9

password = "contraseña"
answer = input("Ingrese la contraseña: ")
while password != answer:
        print("Contraseña Incorrecta.")
        answer = input("Ingrese la contraseña: ")
print("Contraseña Correcta.")

# Ejercicio 10

number1 = int(input("Ingrese un número entero positivo: "))
counter = 1
divider = 0
if (number1 == 0 or number1 < 0):
    print("Debe ingresar un número mayor a 0.")
else:
    while counter <= number1:
        if (number1 % counter == 0):  
            divider = divider + 1
            counter = counter + 1
        else:
            counter = counter + 1
    if (divider == 2):
        print(f"El número {number1} es primo")
    else:
        print(f"El número {number1} no es un número primo")

#Ejercicio 11

word = input("Ingrese una palabra: ")
large1 = len(word)
large2 = large1
backwards = ""

for i in range(large1):
    large2 = large2 - 1
    letter = word[large2]
    backwards = backwards + letter
print(backwards)

#Ejercicio 12

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
large = len(phrase)
repetitions = 0

for i in range(large):
    if (letter == phrase[i]):
        repetitions = repetitions + 1
    else:
        repetitions = repetitions
print(f"La letra \"{letter}\" aparece {repetitions} veces en su frase")

#Ejercicio 13

print("A continuación escribirá una palabra y producirá eco.")
print("Para terminar el programa sólo deberá escribir \"salir\"")
out = "iniciar"

while (out == "iniciar"):
  phrase = input("Escribe una palabra: ")
  if (phrase == "salir"):
    out = "salir"
  else:
    print(phrase, " ", phrase, " ", phrase)
print("Programa Finalizado.")

#Ejercicio 14

number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))

if (number1 > number2):
    big = number1
    small = number2
else:
    big = number2
    small = number1

while (small <= big):
    if (small % 2 == 0):
        print(f"{small} es par.")
        small = small + 1
    else:
        print(f"{small} es impar.")
        small = small + 1

#Ejercicio 15

number1 = int(input("Ingrese un número entero positivo: "))
counter = 1
if (number1 == 0 or number1 < 0):
    print("Debe ingresar un número mayor a 0.")
else:
    print(f"Los siguientes números son divisores de {number1}:")
    while counter <= number1:
        if (number1 % counter == 0):  
            print(counter)
            counter = counter + 1
        else:
            counter = counter + 1

#Ejercicio 16
 
repetitions = int(input("¿Cuántos números desea ingresar?: "))
negative = 0
for i in range(repetitions):
    number = int(input("Ingrese un número: "))
    if (number < 0):
        negative = negative + 1
if (negative == 0):
    print(f"Entre los números que escribió, no hubieron números negativos")
elif(negative == 1):
    print(f"Entre los números que escribió, hubo 1 número negativo")
else:
    print(f"Entre los números que escribió, hubieron {negative} números negativos")

#Ejercicio 17

phrase = input("Ingrese una frase: ")
used1 = 0
used2 = 0
used3 = 0
used4 = 0
used5 = 0
vowels = ""
large = len(phrase)
print("Las siguientes vocales están en su frase: ")
for i in range(large):
    if (phrase[i] == "a" and used1 == 0):
        vowels = vowels + phrase[i] + ", "
        used1 = used1 + 1
    elif (phrase[i] == "e" and used2 == 0):
        vowels = vowels + phrase[i] + ", "
        used2 = used2 + 1
    elif (phrase[i] == "i" and used3 == 0):
        vowels = vowels + phrase[i] + ", "
        used3 = used3 + 1
    elif (phrase[i] == "o" and used4 == 0):
        vowels = vowels + phrase[i] + ", "
        used4 = used4 + 1
    elif (phrase[i] == "u" and used5 == 0):
        vowels = vowels + phrase[i] + ", "
        used5 = used5 + 1
print(vowels)

#Ejercicio 18

number1 = 0
number2 = 1
counter = 1
print("Los diez primeros números de la sucesión de Fibonacci son:")
while (counter <= 10):
    if (counter == 1):
        print(number1, end = ", ")
        counter = counter + 1
        print(number2, end = ", ")
        counter = counter + 1
    else:
        result = number1 + number2
        print (result, end = ", ")
        number1 = number2
        number2 = result
        counter = counter + 1
print("\n")

#Ejercicio 19

piggy_bank = int(input("¿Cuánto dinero quieres ahorrar?: $"))
money2 = 0
while money2 < piggy_bank:
    money1 = int(input("¿Cuánto dinero guardarás?: $"))
    if (money1 < 0):
        money2 = money2 + 0
        print("No se admiten números negativos.")
    else:
        money2 = money2 + money1
print(f"¡Lograste tu objetivo! Ahorraste ${money2}")

#Ejercicio 20

number = 1
result = 0
while (number != 0):
    number = int(input("Ingrese un número: "))
    result = result + number
print(f"La suma de todos los números ingresados es igual a {result}.")

#Ejercicio 21

number = 1
result = 0
while (number != 0):
    number = int(input("Ingrese un número: "))
    if (number > result):
        result = number
print(f"El mayor número ingresado fue: {result}.")

#Ejercicio 22

number = 0
large = 0
result = 0
even = 0
while (number != -1):
    number = input("Ingrese un número entero positivo: ")
    large = len(number)

    if (int(number) >= 0):
        for i in range(large):
            result = result + int(number[i])
        print(f"La suma de los dígitos de {number} es igual a: {result}.")
        result = 0
        number = int(number)
        if (number % 2 == 0):
            even = even + 1

    elif (int(number) == -1):
        print("Programa finalizado.")
        number = int(number)
    else: 
        print("ERROR: Ingresó un valor negativo.")
        number = int(number)

if (even == 0):
    print("No ingresó ningún número par.")
elif (even == 1):
    print("Ha ingresado 1 número par.")
else:
    print(f"Ha ingresado {even} números pares.")

#Ejercicio 23 & 24

shopping = 1
result = 0
while (shopping != 0):
    shopping = int(input("Ingrese el monto de la compra del cliente: "))
    if (shopping < 0):
        shopping = int(input("Error: monto negativo. Ingrese un nuevo monto: "))
        result = result + shopping
    else:
        result = result + shopping
if (result <= 1000):
    print(f"El monto total de la compra del cliente es de ${result}")
else:
    discount = result *0.1
    print("Usted recibirá un 10% de descuento.")
    print(f"El monto a pagar es de ${result - discount}")

#Ejercicio 25

result = 0
number = int(input("Ingrese un número entero positivo: "))
if (number < 0):
    print("Error: su número es negativo.")
elif (number == 0):
    print("La factorial de 0 = 1.")
else:
    result = number
    copy = number
    while (number > 1):
        number = number - 1
        result = result * number
    print(f"La factorial de {copy} = {result}.")
        