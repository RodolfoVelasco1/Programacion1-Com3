#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#DEFINICIÓN DE FUNCIONES

def most(a, b):
    if (a > b):
        return a
    else:
        return b

def least(a, b):
    if (a < b):
        return a
    else:
        return b

#PROGRAMA PRINCIPAL

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

print(most(x - 3, least(x + 2, y - 5)))
