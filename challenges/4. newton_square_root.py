"""
Create a program that calculates the square root of a number with the Newton's method.
You should read the following: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
"""


def square_root_newton(number, tolerance=1e-6):
    if number < 0:
        return None  # No se puede calcular la raíz cuadrada de números negativos

    x = number / 2  # Una estimación inicial razonable

    while True:
        root = 0.5 * (x + number / x)
        if abs(root - x) < tolerance:
            break
        x = root

    return root


# Ejemplo de uso
number = float(input("Ingrese un número para calcular su raíz cuadrada: "))
result = square_root_newton(number)
if result is not None:
    print("La raíz cuadrada de {} es aproximadamente: {:.6f}".format(number, result))
else:
    print("No se puede calcular la raíz cuadrada de un número negativo.")