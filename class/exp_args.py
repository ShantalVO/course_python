"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""
def sum_args(*numbers):    #con el asteriscotodo lo que pongamos se va a guardar en una tupla
   return sum(numbers)

print(sum_args(1, 1 ,1 ,1))


"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""
def concat_strings(*words):
    print(''.join(words))


"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""

def calculate_expenses(name, monthly_income, *expenses, **fixed_expenses):    #número, tupla, diccionario
    print(monthly_income - sum(expenses) - sum(fixed_expenses.values()))

    pass   # sirve para definir una función que no se sabe por completo que va a ser.

calculate_expenses('Shantal',
                   50000,
                   100, 200, 300, 400,
                   Rossy=3000, Yahir=2000, Andrea=1000)

def my_func(*v1, **v2):
    return v1, v2

my_func(1,2,3,4,5, c1='a', c2='b')

#________________________________________________________________________________

#OTRA FORMA

# def calculate_expenses(name, monthly_income, *variable_expenses, **fixed_expenses):
#     total_variable_expenses = sum(variable_expenses)
#
#     total_fixed_expenses = sum(fixed_expenses.values())
#
#     remaining_balance = monthly_income - (total_variable_expenses + total_fixed_expenses)
#
#     print(f"{name}'s remaining balance after deducting all expenses is: ${remaining_balance:.2f}")
#
#
# calculate_expenses(
#     "Shantal",
#     50000,
#     200, 300, 150,
#     escuela=1200,
#     ropa=300,
#     comida=2000
# )