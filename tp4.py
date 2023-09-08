#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio 1.1

x = 0

while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x.")
        continue
    elif x == 15:
        print(f"Se rompió la ejecución del bucle cuando x valía {x}.")
        break
    print(f"El valor del bucle es: {x}.")
    
#Ejercicio 1.2

line = None
words = ""
while line != "":
    line = input("Ingrese una linea o deje una línea en blanco para indicar que ha finalizado la entrada de líneas: ")
    words = words + line + " "

words = words.upper()

print(words)

#Ejercicio 2

answer = "respuesta"
bank = 0
movement = ""
while (answer != ""):
    print("Ingrese la letra operación que desea realizar, seguido de un espacio y el monto")
    answer = input("D para depositar o R para retirar o una linea en blanco para finalizar: ").upper()
    if (answer == ""):
        break
    else:
        movement = answer[0]
        money = int(answer[2:len(answer)])
        if (movement == "D"):
            bank = bank + money
        elif(movement == "R"):
            bank = bank - money
        else:
            print("Operación Incorrecta. Intente de nuevo.")
print(bank)


#Ejercicio 3 

aux = 0
prime = 0
while(aux==0):
    number=int(input("Ingrese un número mayor a 1: "))
    if (number < 1 and number != 0):
        print("No se puede usar un número menor a 1.")
    elif(number == 0):
        print("Saliste del bucle.")
        break
    else:
        index = 1
        divisor = 0
        while (index <= number):
            if (number % index == 0):
                divisor = divisor + 1
            index = index + 1
        if (divisor == 2):
            prime = prime + 1
print(f"La cantidad de números primos que ingresó fue de: {prime}")  


#Ejercicio 4

year_1 = int(input("Ingrese un año: "))
year_2 = int(input("Ingrese otro año: "))

if year_2 > year_1:
    aux = year_1
    year_1 = year_2
    year_2 = aux

while year_2 < year_1:
    if year_2 % 10 == 0 and year_2 % 4 == 0 and (year_2 % 100 != 0 or year_2 % 400 == 0):
        print(f"Año Bisiesto y Multiplo de 10: {year_2}")
    elif year_2 % 4 == 0 and (year_2 % 100 != 0 or year_2 % 400 == 0):
        print(f"Año Bisiesto: {year_2}")
    elif year_2 % 10 == 0:
        print(f"Año Multiplo de 10: {year_2}")
    year_2 += 1
    

#Ejercicio 5 

for i in range(1,21):
    if i%2 != 0:
        continue
    print(i)


#Ejercicio 6: 

numbers_list = [i for i in range(50)]
search_number = int(input("Ingrese numero a buscar: "))
val = False
for i in range(len(numbers_list)):
    if numbers_list[i] == search_number:
        val = True
        break

if (val == True): 
    print(f"Numero encontrado: {search_number}")
else: 
    print(f"El numero a buscar no se encuentra")  


#Ejercicio 7 

aux = "True"
while(aux == "True"):
    print("Menú:")
    print("Opcion 1 - ingrese \"1\"")
    print("Opcion 2 - ingrese \"2\"")
    print("Opcion 3 - ingrese \"3\"")
    print("Opcion 4 - ingrese \"4\"")
    print("Para salir ingrese \"0\"")
    option = input()
    if option == "0":
        print("¡Adiós, vuelva pronto!")
        break
    elif(option == "1"):
        print("hola soy la opcion 1")
    elif(option == "2"):
        print("hola soy la opcion 2")      
    elif(option == "3"):
        print("hola soy la opcion 3")
    elif(option == "4"):
        print("hola soy la opcion 4")    

