# FUNCTION

# # Me va a dar la palabra algebra separada por comas y con espacios
# s = 'algebra'
# for char in s:
#     print(char, end= ' ,  ')

# OTRA FORMA

# def special_printing(s):
#     for char in s:
#         print(char, end =' ,  ')
#
# special_printing('algebra')

# Hace lo mismo que el código anterior
# Tiene un key word nuevo que es el 'def' 'nombre'(argumentos):
# ARGUMENTOS: cuando estamos llamando a la función ej: 'algebra' es un argumento
# PARAMETROS: Variabes que vamos a necessitar al momento de la creacion de una función ej: s es un argumento


# EJEMPLO DE REUSO DE CÓDIGO

# print('**********')
# print('*        *')
# print('*        *')
# print('**********')

# # si lo quiero dos veces, lo copio y lo pego


# _____________________________________________________________________________________________________________________

# LO MISMO PERO UTILIZANDO FUNCIONES

# def draw_box():
#     print('**********')
#     print('*        *')
#     print('*        *')
#     print('**********')
#
# draw_box()
# draw_box()
#
# # Lo estoy imprimiendo dos veces


# _____________________________________________________________________________________________________________________

# PARA DECIRLE CUANTAS VECES QUIERO QUE SE IMPRIMA
#
# def draw_box(n):
#     for _ in range(n):
#
#         print('**********')
#         print('*        *')
#         print('*        *')
#         print('**********')
#
# draw_box(1)    # 1: quiero que se imprima 1 vez



# ____________________________________________________________________________________________________________________

# En Pythontodo es un objeto, por lo tanto, una fuención también lo será
#
# def f(x): return x*x            # A fruitful function
#
# def g(x): return 2*x + 6
#
# def h(x): return -x
#
# my_func = [f, g, h]              #Recollecting names
# for name in my_func:
#     print(name(4))              # name tomará el nombre de f, g, h


# OTRA FORMA
#
# def f(x):
#     return x*x            # A fruitful function
#
# print(f(2))               # Le digo que x vale 2, entonces 2*2 = 4


# OTRA FORMA

# def f(x): return x*x            # A fruitful function
#
# def g(x): return 2*x + 6
#
# def h(x): return -x
#
# # my_func = [f, g, h]              #Recollecting names
# # for name in my_func:
# #     print(name(4))              # name tomará el nombre de f, g, h
#
# # print(f)     # Me da la dirección de memoria, para la letra que le dé
#
# my_functions = (f, g, h)
# for function in my_functions:
#     print(function(2))

# _____________________________________________________________________________________________________________________
#
# def check(a_list):                  # Cuando se acabe la funcion la variable a_list va a desaparecer
#     if 'hello' in a_list:           # a_list is a
#         #local variable
#         return True
#
# my_list = []     # We could have an error because the var is outer the scope of the function


# OTRA FORMA
#
# a = 0
# def check(a_list):                  # Cuando se acabe la funcion la variable a_list va a desaparecer
#     if 'hello' in a_list:           # a_list is a
#         #local variable
#         return print(a)
#
# # my_list = []     # We could have an error because the var is outer the scope of the function

# ___________________________________________________________________________________________________________________
#
# x = 5
#
# def my_f(x):
#     print(x)
#
# my_f(8)      # 8 tomará el valor de x en la línea 130
# print(x)     # Lo toma del GLOBAL SCOPE, la que esta disponible en la línea 127


# OTRA FORMA
#
# x = 5
#
# def my_f(y):
#     print(y)
#
# my_f(8)      # 8 tomará el valor de x en la línea 130
# print(x)     # Lo toma del GLOBAL SCOPE, la que esta disponible en la línea 127
#
# # Aquí ya se quita el warning

# ___________________________________________________________________________________________________________________
#
# x = 45    # GLOBAL    # Puede ser accesible para toda estructura que este haciendo, es global, lo más fuera
# def outer_function(var1):
#     y = 12          # LOCAL
#     a = var1        #LOCAL
#
#     def inside_function():     # No va a tomar parámetros
#         b = 17      # LOCAL
#         print(x, y, a, b)
#     #print(b)  # ERROR!!! This is nonlocal   # Es un error porque está fuera de la función, y no se puede acceder a ella (identado)
#     inside_function()
#
# #print(y)    # ERROR !!!   # Es un error porque está fuera de la función, y no se puede acceder a ella (identado)
# outer_function(4)


# __________________________________________________________________________________________________________________

# PARA MODIFICAR X

# x = 0
#
# def increment_by_n(n):
#     global x
#     x+= n
#     return x
#
# print(x, increment_by_n(5))         # 0 5
# print(x)     # This is a 5

