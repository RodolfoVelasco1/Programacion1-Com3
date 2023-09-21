#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio 1

phrase = input("Ingrese una palabra o una frase: ")
if (len(phrase) == 4):
    phrase = phrase + "!"
else:
    phrase = phrase + "?"
print(phrase)


#Ejercicio 2

import random
list = ["PIZZA", "HAMBURGUESA", "PASTA", "MANZANA", "NUEZ", "MILANESA", "PLATANO"]
random = random.choice(list)
word_length = len(random)
index = 0
failures = 0
complete_answer = ""
print("Bienvenido al juego de ADIVINAR LA PALABRA")
print("El día de hoy, la temática serán: comidas.")
print("Debes adivinar letra por letra la palabra.")
print("Puedes equivocarte hasta 3 veces.")
print("¡Mucha suerte!")
print(f"La palabra tiene {word_length} letras.")

while (complete_answer != random):
    print(f"Te faltan adivinar {word_length} letras.")
    print(f"Palabra: {complete_answer}")
    answer = input("Ingrese una letra: ")
    if (answer.upper() == random[index]):
        complete_answer = (complete_answer + answer).upper()
        word_length = word_length - 1
        index = index + 1
        print("CORRECTO.")
    elif (answer.upper() != random[index] and failures < 3):
        failures = failures + 1
        print(f"INCORRECTO. Error #{failures}")
        
    else:
        print("INCORRECTO.")
        break
if (failures == 3):
    print("Perdiste. Gracias por jugar.")
else:
    print(f"La palabra era {random}.")
    print("¡Ganaste! ¡Buen trabajo! Gracias por jugar.")


#Ejercicio 3

phrase = input("Ingrese una palabra o una frase: ")
counter = 0
space = " "
for i in range(len(phrase)):
    if (phrase[i] == space):
        counter = counter + 1
if (counter >= 1):
    counter = counter + 1
    print(f"Usted ha ingresado {counter} palabras.")
elif (phrase == ""):
    print("No ha ingresado palabras")
elif (counter == 0 and phrase != ""):
    print("Usted ha ingresado 1 palabra.")


#Ejercicio 4

index = 0
print("Para saber qué adicional hay que pagarle a los empleados conteste las siguientes preguntas.")
print("Por favor, responda con el número de opción que desea seleccionar.")
while (index == 0):
    print("¿El empleado asistió todo el mes?")
    print("1. Sí.     2. No.")
    month = int(input("Respuesta: "))
    if (month == 1):
        print("¿Cuántas horas trabajó los domingos?")
        print("1. Entre 3 y 5 horas.     2. Entre 6 y 10 horas.   3. Ninguna de las anteriores")
        sunday1 = int(input("Respuesta: "))
        if (sunday1 == 1):
            print("Le corresponde un adicional del 3%.")
            break
        elif (sunday1 == 2):
            print("Le corresponde un adicional del 10%.")
            break
        elif (sunday1 == 3):
            print("No le corresponde adicional.")
            break
        else:
            print("Error. Respuesta inválida")

    elif (month == 2):
        print("¿Cuántas horas trabajó los domingos?")
        print("1. Entre 3 y 10 horas.     2. Ninguna de las anteriores")
        sunday2 = int(input("Respuesta: "))
        if (sunday2 == 1):
            print("Le corresponde un adicional del 3%.")
            break
        elif (sunday2 == 2):
            print("No le corresponde adicional.")
            break
        else:
            print("Error. Respuesta inválida")
    else:
        print("Error. Respuesta inválida")


#Ejercicio 5

number_1 = int(input("Ingrese un número: "))
number_2 = int(input("Ingrese otro número: "))
if (number_1 == number_2):
    result = number_1 * number_2
    print(f"{number_1} x {number_2} = {result}")
elif (number_1 > number_2):
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")
else:
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")


#Ejercicio 6

index = 0
print("Bienvenido a ANSES.")
print("Para saber el tipo de jubilación que le corresponde, conteste las siguientes preguntas.")
print("Debe contestar con el número de la respuesta que desea seleccionar.")
while (index == 0):
    print("¿Cuántos años tiene?")
    print("1. Tengo 60 años o más.    2. Tengo menos de 60 años.")
    age = int(input("Respuesta: "))
    if (age == 1):
        print("¿Cuánta antigüedad tiene en su empleo?")
        print("1. Menos de 25 años.   2. 25 años o más.")
        job = int(input("Respuesta: "))
        if (job == 1):
            print("Le corresponde: JUBILACIÓN POR EDAD.")
            break
        elif (job == 2):
            print("Le corresponde: JUBILACIÓN POR ANTIGÜEDAD ADULTA.")
            break
        else:
            print("Error. Respuesta inválida.")
    elif (age == 2):
        print("¿Cuánta antigüedad tiene en su empleo?")
        print("1. Menos de 25 años.   2. 25 años o más.")
        job = int(input("Respuesta: "))
        if (job == 1):
            print("Lo sentimos, no le corresponde ninguna jubilación.")
            break
        elif (job == 2):
            print("Le corresponde: JUBILACIÓN POR ANTIGÜEDAD JOVEN.")
            break
        else:
            print("Error. Respuesta inválida.")
    else:
        print("Error. Respuesta inválida.")


#Ejercicio 7

index = 0
print("¿Cuánto me corresponde de utilidad?")
print("Para saberlo conteste las siguientes preguntas.")
while (index == 0):
    print("¿Cuántos años lleva en la empresa?")
    years = int(input("Respuesta: "))
    if(years == 0):
        salary = int(input("Ingrese el monto de su salario mensual: $"))
        money = salary * 0.05
        print("Su utilidad será del 5% de su salario")
        print(f"Recibirá una utilidad de ${money}")
        break
    elif (years == 1):
        salary = int(input("Ingrese el monto de su salario mensual: $"))
        money = salary * 0.07
        print("Su utilidad será del 7% de su salario")
        print(f"Recibirá una utilidad de ${money}")
        break
    elif (years >= 2 and years < 5):
        salary = int(input("Ingrese el monto de su salario mensual: $"))
        money = salary * 0.10
        print("Su utilidad será del 10% de su salario")
        print(f"Recibirá una utilidad de ${money}")
        break
    elif (years >= 5 and years < 10):
        salary = int(input("Ingrese el monto de su salario mensual: $"))
        money = salary * 0.15
        print("Su utilidad será del 15% de su salario")
        print(f"Recibirá una utilidad de ${money}")
        break
    elif (years >= 10):
        salary = int(input("Ingrese el monto de su salario mensual: $"))
        money = salary * 0.20
        print("Su utilidad será del 20% de su salario")
        print(f"Recibirá una utilidad de ${money}")
        break
    else: 
        print("ERROR. Respuesta inválida.")