"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""


def compute_average():
    total = 0
    count = 0

    while True:
        value = float(input("Ingrese un valor o 0 para parar: "))

        if value == 0:
            if count == 0:
                print("Error: No se ingresarón valores.")
                continue
            else:
                break

        if count == 0 and value == 0:
            print("Error: El primer valor no puede ser 0.")
            continue

        total += value
        count += 1

    if count > 0:
        average = total / count
        print("Promedio:", average)


compute_average()