#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#TP8

from tp8_funciones import *

#EJERCICIO 1

print("EJERCICIO 1")
number = 12345
digits = counting_digits(number) 
print("El número ", number, " tiene ", digits, " dígitos.")


#EJERCICIO 2

print("EJERCICIO 2")
while (True):
    print("Verificaremos si n es potencia de b.")
    print("Ingrese 0 si se quiere salir.")
    n=int(input("Ingrese n: "))
    b=int(input("Ingrese b: "))        
    if(n!=0 and b!=0):
        option=power(n,b)
        if option==True:
            print(n,"es potencia de",b)
        else:
            print(n,"no es potencia de",b)    
    else:
        break


#EJERCICIO 3

print("EJERCICIO 3")
array_temp = []
print("Buscaremos la posición de \"es\" en \"Tres tristes tigres\"")
print(find_in("Tres tristes tigres","es",0,array_temp))


#EJERCICIO 4

print("EJERCICIO 4")
number = int(input("Ingrese un número: "))
print("El numero", number, "es",even(number))


#EJERCICIO 5

print("EJERCICIO 5")
array = [25, 500, 250, 835, 425]
print("Lista:", array)
max_list(array)


#EJERCICIO 6

print("EJERCICIO 6")
list = [3, 5, 8, 9]
print("Lista:", list)
repetitions = int(input("¿Cuántas veces desea repetirlo?: "))
repeat(list, repetitions)


#EJERCICIO 7

print("EJERCICIO 7")
number = int(input("Ingrese un numero: "))
number_count = int(input("Ingrese cantidad: "))

print(sumatory(number, number_count))


#EJERCICIO 8

print("EJERCICIO 8")
print("Triángulo Pascal")
print("El valor de columna 3 fila 5= ",pascal(3,5)) 


#EJERCICIO 9

print("EJERCICIO 9")
characters = ['a', 'b', 'c']
length = 6
combinations(characters, length)


#EJERCICIO 10

print("EJERCICIO 10")
fold = int(input("¿Cuántas veces desea doblar la hoja de papel?: "))     
print("Las dimensiones de la hoja al doblarla", fold, "veces son:", sheet_measurements(fold))











 