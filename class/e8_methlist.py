import random
"""
1. From the empty list, store the elements: 3.1415, 'sin(x)', []. Inside the last element, store the first two elements,
then print out the list with all the elements. Finally remove all the elements and print out the list. The two lists
should appear
"""
list1 = []
list1.append(3.1415)
list1.append('sin(x)')
list1.append('cos(x)')
list1.append([])
print(list1)  #Imprimo los elementos añadidos
list1[-1].append(3.1415)  #[-1] para acceder al último elemento
list1[-1].append('sin(x)')
print(list1)
list1.clear()
print(list)


# 2. From the list2, print out the original list and print out a second with one element extra. DO NOT copy and paste
list2 = ['Spivak', 'Mood', 'Apostol', 'Bowers']
print(list2)
list2.append('I do not know')
print(list2)



# 3. Use extend() method as you want
fruits = ['grape', 'banana', 'apple']
fruits.extend(['grape', 'banana', 'apple'])
print(fruits)



# 4. At index 8, insert 'a new element'. Print out the before and after. Also count how many times 5 are in the list
random_list = [random.randint(1, 100) for _ in range(25)] #Lista con 25 números aleatorios del 1 al 100
print(random_list)
random_list.insert(8, 'a new element')
print(random_list)  #Cada que se ejecute el string va a dar numeros distintos, pues son aleatorios
print(random_list.count(5))   #Me va acontar cuantas veces aparece el 5 en la lista generada


''' 
5. from my_list retrieve the 15th element and store in my_list2. The same with the last element
and store it in my_list3. Then remove the first element of my_list. Print out the three lists
'''
my_list = [
    45, 78, 98, 4, 12, 'g0', 7, 'er', 'py', 456, 96, 153, 78, 4410, 3213, 'r', 'ef0'
]
my_list2 = []
my_list2.append(my_list.pop(14))  #pop retorna el elemento borrado
my_list3 = []
my_list3.append(my_list.pop())   #Cuando se deja pop en blanco es porque borra y retorna el último elemento
my_list.remove(45)   #Remueve el primer elemento
print(my_list)
print(my_list2)
print(my_list3)


# 6. Make a string with your favorite artist name, each component must be in a list. When you have the list, reverse it
artist = 'Adele'
my_list = list(artist)  #Del iterable que se especifico, se va a poner cada elemento como objeto de una lista 'Adele'
print(my_list)
my_list.reverse()      #Revertir la lista
print(my_list)


'''
7. Make a list with random numbers, sort from lowest to largest. Do not modify the list. Print out the original and the
sorted list. Finally print out the index of some random number of your list
'''
rad = [1, 0, -9, -8, 52, 4, 6]
print(rad)           #Lista original
print(sorted(rad))   #Ordena del menor al mayor, no modifica la lista, solo retorna una nueva y ordenada
print(rad)           #Lista con modificaciones
print(rad.index(0))  #Imprime el elemento que esta en el índice 0
