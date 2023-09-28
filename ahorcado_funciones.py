#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio Ahorcado - Funciones

def encrypt(a): #Esta función encripta la palabra que el usuario debe adivinar. Por cada letra de la palabra, el programa mostrará guines bajos.
    b = ""
    for i in range(a):
        b = b + "_"
    return b

def main_game (a, b, c):    #Esta función mostrará por pantalla, las letras que el usuario ha ingresado. Y mostrará la palabra encriptada. Si el usuario ya adivinó letra, se mostrarán esas letras desencriptadas en su lugar correspondiente.
    print("Palabras usadas: " + a)
    print("Palabra: ", end ="")
    for i in range(b):
        print(c[i] + " ", end = "")
    print("\n")

def word_check(a, b, c, d): #Esta función verifica si la letra ingresada se encuentra en la palabra que se debe adivinar. Si la letra es correcta, la función devuelve "True", caso contrario, devuelve "False".
    for i in range(a):
        if (b[i] != c):
            d = False
        else:
            d = True
            return d
    return d

def right(a, b, c, d):  #Si la letra ingresada por el usuario es correcta, en la palabra encriptada, se "desencriptará" la letra que adivinó, es decir, la letra ingresada se hará visible en el lugar correspondiente.
    for i in range(a):
        if (b[i] == d):
            c = c[:i] + d + c[i+1:]
    print("¡Letra correcta! ¡Sigue así!")
    return c

def wrong(a):   #Si la letra ingresada por el usuario es incorrecta, se le avisará al usuario, se le quitará una vida y se le mostrará la cantidad de vidas restantes.
    print("¡Incorrecto! Pierdes una vida.")
    a = a - 1
    print("Cantidad de vidas: " + str(a))
    return a