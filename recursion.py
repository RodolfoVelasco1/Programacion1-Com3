#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#EJERCICIO 1

import random

def maze_time(time):    #Función recursiva que calculará el tiempo que le toma a la rata salir de la jaula.
    maze = random.randint(1, 3)     #Elige un número al azar entre 1 y 3, el cual representa el camino que elige la rata.
    if (maze == 1):     #Si la rata toma el camino 1 o 2...
        print("La rata eligió el camino #1. En 3 minutos vuelve a la jaula.")
        time = 3        #...se imprime el camino que tomó, y la variable "time" toma el valor del tiempo que le toma regresar a la jaula.
        return time + maze_time(time) #Se suma el resultado a la variable de retorno y se llama nuevamente a la función.
    elif (maze ==2):
        print("La rata eligió el camino #2. En 5 minutos vuelve a la jaula.")
        time = 5
        return time + maze_time(time)
    else:   #Caso base: si la rata toma el camino 3, se imprime un mensaje, la variable time adquiere el valor del tiempo que le toma a la rata salir.
        print("La rata eligió el camino #3. En 7 minutos logra salir.")
        time = 7
        return time #El programa devuelve la suma de todo el tiempo que le tomó a la rata recorrer cada camino.

time = 0            #Creamos la variable de tiempo. Y llamamos a la función que calulará el tiempo que le toma a la rata salir de la jaula.
time = maze_time(time)
print("La rata tardó ", time, " minutos en salir del laberinto.")


#EJERCICIO 2

#CONSIGNA: Realice una función recursiva que reciba como parámetro un número entero y devuelva el número en orden invertido.


def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))


n = 5839
h = f(n)
print(h)