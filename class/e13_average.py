"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""
#
#
# def compute_average():
#     total = 0
#     count = 0
#
#     while True:
#         value = float(input("Ingrese un valor o 0 para parar: "))
#
#         if value == 0:
#             if count == 0:
#                 print("Error: No se ingresarón valores.")
#                 continue
#             else:
#                 break
#
#         if count == 0 and value == 0:
#             print("Error: El primer valor no puede ser 0.")
#             continue
#
#         total += value
#         count += 1
#
#     if count > 0:
#         average = total / count
#         print("Promedio:", average)
#
#
# compute_average()


#___________________________________________________________________________________________________________________
# OTRA FORMA

count = 0
my_sum = 0
while True:
    n = float(input('Enter a number, 0 for break: '))
    if n == 0 and count == 0:
        print('You should enter another value')
        continue
    elif n == 0:
        break
    else:
        my_sum += n
        count += 1

print(my_sum/count)