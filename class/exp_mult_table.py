# Generate and print the multiplication table (up to 10) for a given number

number = int(input('Introduce un número: '))   # typecasting: proceso de conversión entre datos

for a in range(1, 11):
    mult = a*number
    print(f'{number} x {a} = {mult}')

