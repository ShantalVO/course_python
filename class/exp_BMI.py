"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Equal to or over 25 but below 30 they are slightly overweight
    Equal to or over 30 but below 35 they are obese
    Equal to or over 35 they are clinically obese.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
"""
# Peso y altura del usuario
weight = float(input('What is your weight in kg: '))
height = float(input('What is your height in m: '))

# operacion BMI
bmi = weight/(height**2)

# condicionales
if bmi < 18.5:
    print('You are underweight')
elif bmi > 18.5 and bmi < 25:   # Tambien se puede poner en forma de intervalo
    print('You are normal weight')
elif bmi >= 25 and bmi < 30:
    print('You are slightly overweight')
elif bmi >=30 and bmi < 35:
    print('You are obese')
elif bmi >= 35:
    print('You are clinacally obese')