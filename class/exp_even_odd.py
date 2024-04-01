# Make a program that determines if a number (given by the user) is odd or even

# User's number
number = int(input('Enter a number: '))

# test if the number is odd or even
if number % 2 == 0:  #Del numero que el usuario me de me retorne el modulo si lo divido en 2
    print(f'{number} is even')
else:
    print(f'{number} is odd')


# print the result
