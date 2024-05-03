"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""
# Cualquier número entero realizando operaciones particulares llegamos a 1

n = int(input('Enter a number: '))  # Al trabajar con número lo vamos a convertir en enteros    # typecasting

while True:      # No se cuántas operaciones debo realizar para llegar a 1   True: valor boleano, hace que el While se detenga
    # if number
    # 1
    if n == 1:
        break

    # if number 2
    if n % 2 == 0:
        n = n/2        # shared references
        print(n)
    else:
        n = 3*n + 1
        print(n)

# Como se tarata de un While mientras se cumpla el primero o segundo if se cumple el while, entra al if numero 1, y se para