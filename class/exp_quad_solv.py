"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""
#
# def lambda_func(a, b, c):
#     x1 = (-b + pow(1/2, b^2 -4ac))/2a
#


import math

quadratic_roots = lambda a, b, c: (
    (-b + pow((pow(b,2)- 4*a*c), 1/2))/ (2*a),
    (-b - pow((pow(b,2) - 4*a*c), 1/2)) / (2*a)
)

a, b, c = 2, 2, 0
roots = quadratic_roots(a, b, c)
print(roots)  # Output: (2.0, 1.0)

# OTRA FORMA

quad = lambda a, b, c: ((-b + pow(pow(b,2)-4*a*c, 1/2))/(2*a), (-b - pow(pow(b,2)-4*a*c, 1/2))/(2*a))
print(quad(2,2,0))

# OTRA FORMA
def lamda_func(a,b,c):
    x1 = (-b + pow((pow(b,2)- 4*a*c), 1/2))/ (2*a)
    x2 = (-b - pow((pow(b,2) - 4*a*c), 1/2)) / (2*a)
    print(f'Las raice de a ecuacion cuadrática son: raiz 1 = {x1} y raíz 2 = {x2}')

lamda_func(1,-3,2)