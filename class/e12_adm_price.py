"""
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00.
Admission for all other guests is $23.00. Create a program that begins by reading the ages of all the guests in a
group from the user,with one age entered on each line.
The user will enter a blank line to indicate that there are no more guests in the group.
Then your program should display the admission cost for the group with an appropriate message.
"""


def calculate_admission(age):
    if age <= 2:
        return 0
    elif 3 <= age <= 12:
        return 14.00
    elif age >= 65:
        return 18.00
    else:
        return 23.00


def main():
    total_cost = 0
    while True:
        age_input = input("Ingrese la edad del huesped o deje en blanco para terminar: ")
        if age_input == "":
            break
        age = int(age_input)
        cost = calculate_admission(age)
        total_cost += cost

    print("El costo total de admisión para el grupo es: ${:.2f}".format(total_cost))   #.2 dos decimales, f = número decimal


if __name__ == "__main__":
    main()

# _________________________________________________________________________________________________________________
# OTRA FORMA

# cost = 0
#
# while True:
#     age = input('Enter the age: ')
#     if age == '':
#         break
#     age = int(age)
#     if age <= 2:
#         continue
#     elif 3 <= age <= 12:
#         cost +=14
#     elif age >= 65:
#         cost += 18
#     else:
#         cost += 23
#
# print(cost)
