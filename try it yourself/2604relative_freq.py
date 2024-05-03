# This is a simulation of rolled a six - dice a number of times to calculate the frequency
import random   # Modulo de Python

"""
THE LOGIC:

1. WE NEED A DICE
2. WE ROLL THAT DICE A NUMBER OF TIMES AND RECORD THE FACE OF INTEREST
3. WE COMPUTE THE FREQUENCY (NUMBER OF TIMES OUR FACE OF INTEREST RESULTED/TOTAL ROLL DICE)

"""
# PARADIGMA DE FUNCIONES

# paradigms

# # PROCEDURAL APPROACH
#
# # generating the faces of a die
# faces = []    # Lista para guardar números del 1 al 6, también se podría con una tupla
# for f in range(1, 7):    # El dado tiene 6 caras
#     faces.append(f)
#
# # REPEATEDLY CHOICE a face from the list until reach some n
# # count the number of occurences the face selected
# n = 100000           # Veces que quiero tirar el dado
# face_selected = 5    # Cara a registrar
# occurrence = 0       # Registra de cuantas veces sale el 5 en las 100000 tiradas
# for _ in range(n):   # Éste for correrá 100000 veces
#     random_face = random.choice(faces)    # choice: aleatoreamente va a escoger de una lista, una cara aleatoria, ya importe random arriba, el . hace una búsqueda
#     if face_selected == random_face:      # Verifica si la cara que salio corresponde a mi interés
#         occurrence += 1                   # Suma 1 ocurrencia
#
# # print the ratio of occurrence (frequency)
# print(f'The frequency of face number {face_selected} in {n} trails is {occurrence/n}')   # Frecuencia


# _______________________________________________________________________________________________________________

# OTRO MÉTODO
# functional approach      se va a empaquetar cada tarea en una función

faces = [f for f in range(1, 7)]   # Estoy creando las 6 caras del dado

def roll_dice():            # Seleccionar alguna cara del dado

    return random.choice(faces)     # return: key word, me va a retornar un elemento aleatorio de la lista faces, yo puedo guardar lo que retorna en una variable

# my_random = roll_dice()             # Lo que me arroje, lo guardo en my_random
#
# print(my_random)                    # Cada que ejecute mi script me arrojará algo nuevo
# print(roll_dice())                    # Cada que ejecute mi script me arrojará algo nuevo

def rolling(r, face):           # r: cuantas veces va a hacer esas tiradas,  face: que cara es de intrés a registrar
    time = 0
    for _ in range(r):
        if roll_dice() == face:         # Hace la comparación de un número con un número
            time += 1
    return time

# print(rolling(5, 1))          # Me dice cuántas veces me va a dar la cara 1 en 5 tiradas


def frequency(r, face):
    print(f' The frequency is: {rolling(r, face)/r}')  # La función rollinf me va a dar las observaciones de interés

n = int(input('How many trials do you want?: '))
user_face = int(input('What face?: '))

# frequency(n, user_face)   # Posicional: poner los argumentos n toma a r, user_face a face, por sus posiciones
frequency(r = n, face = user_face)   # Otra forma de llamar a la función por sus parametros


