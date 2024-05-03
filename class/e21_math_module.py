# Import the math module (as you want)
import math

# Make the Poisson distribution. The user must enter the parameters. Then print out the result
lam = float(input('Dame el valor de lambda: '))
x = int(input('Dame el valor de x: '))

poisson = (math.exp(-lam) * (lam ** x)) / math.factorial(x)
print("La distribución de Poisson es:", poisson)


# Make an iterable with some numbers to calculate the product of all those numbers
numbers = [2, 3, 4, 5]

# From two iterables, calculate the sum of the product of values
product_sum = sum(a * b for a, b in zip(numbers, numbers[::-1]))
print("La suma del producto de los valores es:", product_sum)

# Calculate the GCD of two numbers that user gives
num1 = int(input("Ingrese el primer número: "))







num2 = int(input("Ingrese el segundo número: "))
gcd = math.gcd(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", gcd)


# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result
n = int(input("Ingrese el valor de n para la distribución binomial: "))
x = int(input("Ingrese el valor de x para la distribución binomial: "))
p = float(input("Ingrese el valor de p para la distribución binomial: "))
binomial = (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))
print("La distribución binomial es:", binomial)


# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "
float_number = float(input("Ingrese un número flotante: "))
ceiling = math.ceil(float_number)
print("El techo de", float_number, "es:", ceiling)

# Choose two functions from the math documentation to make exercises like the previous
logarithm_base2 = math.log2(8)  # log base 2 of 8
e_to_power = math.exp(2)  # e raised to the power of 2
print("El logaritmo base 2 de 8 es:", logarithm_base2)
print("e elevado a la potencia de 2 es:", e_to_power)