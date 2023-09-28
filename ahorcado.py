#Alumno: Rodolfo Nicolás Velasco Fessler
#Mi repositorio en GitHub: https://github.com/RodolfoVelasco1/Programacion1-Com3

#Ejercicio Ahorcado

from ahorcado_funciones import *    #Importamos las funciones
import random
word_list = ["GORILA", "TIGRE", "ELEFANTE", "RINOCERONTE", "SERPIENTE", "PERRO", "GATO", "VACA", "GALLINA"]	#Se crea una lista con palabras para usar en el juego del ahorcado.
random_word = random.choice(word_list)	#El programa elige una palabra al azar de la lista.  
word_length = len(random_word) #Se verifica la cantidad de cifras de la palabra.
game_word = encrypt(word_length)	#Se llama a una función que encriptará la palabra. Es decir, en otra variable, por cada letra que tenga la palabra a adivinar, en otra variable se creará un guión bajo.
lives = 5	#Ingresamos la cantidad de vidas que tendrá el usuario.
used_letters = ""
correct = False
print("Bienvenido al juego del Ahorcado.")
print("La temática de hoy es: \"Animales\"")
print("Tienes 5 vidas en este juego.")
print("¡Mucha suerte! ¡A jugar!")	#Le explicamos al usuario el juego.
print("Tu palabra tiene " + str(word_length) + " letras")
while (lives > 0):      #El ciclo se repite hasta que al jugador se le terminen las vidas.
    main_game(used_letters, word_length, game_word) #Se llama a una función que muestra por pantalla las letras que el usuario ha dicho y la palabra encriptada que el usuario debe adivinar.
    answer = input("Ingresa una letra: ").upper()   #Se le pide al usuario que ingrese una letra.
    used_letters = used_letters + answer + ", " #Las letras que ingresa el usuario se guardan en esta variable. Así luego el programa puede mostrar todas las letras que ya ha ingresado.
    correct = word_check(word_length, random_word, answer, correct)  #Se llama a una función que verifica si la letra ingresada está en la palabra que debe adivinar. Si la letra está en la palabra, devolverá un valor "True", sino devolverá "False".
    if (correct == True):
        game_word = right(word_length, random_word, game_word, answer) #Si la letra está en la palabra a adivinar, el programa llama a una función que le avisa al usuario que la letra era correcta y además busca en la palabra encriptada, la ubicación donde debería estar la letra que ingresó el usuario y reemplaza la letra encriptada por la letra ingresada. De este modo, el usuario podrá ver la ubicación de la letra que adivinó.
        if (game_word == random_word):
            print("¡Felicidades! ¡Ganaste!")
            print("La palabra era: " + random_word)
            break   #Si el usuario adivinó todas las letras, el programa le avisará al usuario que ganó, le mostrará la palabra completa y utilizará un break para terminar el ciclo.
    else:
        lives = wrong(lives)    #Si la letra que ingresó el usuario no era correcta, el programa llamará a una función que le avisará al usuario que su respuesta es incorrecta, le quitará una vida, y le mostrará sus vidas restantes.
        if (lives == 0):
            print("¡Incorrecto!")
            print("¡Perdiste! ¡Te quedaste sin vidas!")
            print("La palabra era: " + random_word)
            break   #Si el usuario se queda sin vidas, se le avisa al usuario que perdió, se le muestra la palabra completa y el programa se termina.

    

