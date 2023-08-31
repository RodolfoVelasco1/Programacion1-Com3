#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio 1

mover = int(input("Ingrese la cantidad de lugares que se correrán las letras: "))
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
mensaje_encriptado = ""

for i in range(5):
    mensaje = input("Ingrese un mensaje: ").upper()
    largo = len(mensaje)
    for a in range(largo):
        letra1 = mensaje[a]
        indice = abc.find(letra1)
        indice = (indice + mover)%27
        letra2 = abc[indice]
        mensaje_encriptado = mensaje_encriptado + letra2
    print(mensaje_encriptado)
    mensaje_encriptado = ""

#Ejercicio 2

num1 = 1
impar_total = 0
par_total = 0

while num1 != 0:
    impar = 0
    par = 0
    num1 = int(input("Ingrese números enteros positivos: "))
    digitos = len(str(num1))
    if num1 < 0:
        print("El número ingresado es negativo.")
    else:
        while digitos-1 >= 0:
            num2 = str(num1)
            num2 = int(num2[digitos-1])
            if num2 % 2 == 0:
                par = par + 1
                par_total = par_total + 1
            else:
                impar = impar + 1
                impar_total = impar_total + 1
            digitos = digitos - 1
        print(f"Su número tiene {par} dígitos pares y {impar} dígitos impares.")
            
print(f"En total hubieron {par_total} dígitos pares y {impar_total} dígitos impares.")