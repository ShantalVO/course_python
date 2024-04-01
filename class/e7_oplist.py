# 1. From the given list, replace the number by its name, then print out the list
numbers = [11, 4, 9, 100, 1000]

numbers_name = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7: 'seven', 8:'eight', 9:'nine', 10:'ten',
                11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 20:'twenty', 30:'thirty',
                40:'forty', 100:'one hundred',1000:'one thousand' }

name_list =[numbers_name[num] if num in numbers_name else num for num in numbers]
print(name_list)

#OTRA FORMA
numbers[0] = 'eleven'
numbers[1] = 'four'
numbers[2] = 'nine'
numbers[3] = 'one hundred'
numbers[4] = 'one thousand'
print(numbers) #Imprimirá la lista modificada

# 2. replace all numbers with the numbers 9.6 and 6 with 6 and 9.6 respectively
scores = [9.6, 6, 10, 4.5, 5, 8.2]
scores[0:2] = [6,9.6]
print(scores)

# 3. from the given list, there are two items that do not correspond to the list (notice the contex), delete it
items = ['red', 'purple', 'green', 'yellow', 'phone', 'magenta', 'math', 'white']
my_pop1 = items.pop(4)  #Lo quita y lo guarda en la variable
my_pop2 = items.pop(6)  #Lo quita y lo guarda en la variable
print(items)  #Puede imprimir las variables de pop para que me mestren los que quité pero no es ncesario

#Otra forma
items = ['red', 'purple', 'green', 'yellow', 'phone', 'magenta', 'math', 'white']
items.remove('phone')
items.remove('math')
print(items)

#Otra forma
items = ['red', 'purple', 'green', 'yellow', 'phone', 'magenta', 'math', 'white']
del items[4]
del items[6]
print(items)

# 4. delete the numbers from the list, then print out the final list
my_list = ['r', 'e', 5, 8, 'c', 'q', 9]
del my_list[2]  #del --de que lista -- de que índice
del my_list[2]  #tengo que volver a poner ora vez el 2, porque se crea una lista nueva con lo que ya borré así el 8 seráborrado,
                # poqrue ocupará la posicion 2, cuando quito el primer elemento modificaré los indices de todos los que esten delante
del my_list[-1]  #Me quita el último
print(my_list)

# 5. insert the elements that the variables have. ANSWER: What do you observe?
a = [5, 5, 5]
b = {'key': 1}
c = ('a', 'b')
d = 'jeje'
lst = []

lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
print(lst)

#Otra manera
a = [5, 5, 5]
b = {'key': 1}
c = ('a', 'b')
d = 'jeje'
lst = []
count = [a, b, c, d]    #Los estoy guardando en un iterable
lst += count            # += solo se usan conn un iterable
print(lst)


# 6. Use *= as you want
my_list = [1, 2, 3]
my_list *= 2    #No significa que se van a multiplocar, solo se repetiran ese numero de veces, despues del último objeto
print(my_list)


# 7. Print the 1 that are in the lists
nested_list = [[[[1]]]]  #Listas dentro de otras listas
print(nested_list[0][0][0][0])
#accedo a la lista al elemeneto del primer corchete, con el siguiente cero accedo al segundo corchete, y así hasta llegar al 4 corchete

# 8. Print the word
nested_list2 = [[1], [['hello']]]  #tengo dos elementos
print(nested_list2[1][0][0])
#[1] accedo al índice 1     0,1