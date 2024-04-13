word = ['a', 'b', 'c', 'd']


#LOOP
# for letter in word:
#     print(letter)

# k = 0
# while k < 5:
#     print(f'The value of k is {k}')
#     k += 1    #Quiero que pare hasta aquí  k = k+1
#
# print('Hello')


# x = 'spam'
#
# while x:
#     print(x, end = '   ')
#     x = x [1:]

# x = 10
# while x:
#     x -= 1
#     if x % 2 == 0:
#         continue    #regresa al test
#     print(x)


# while True:
#     name = input('Enter your name:  ')
#     if name == 'stop':
#         break
#     age = input('Hello', name, '=>', int(age) ** 2)
#
# print('out of while')

# words = ['despair', 'phone', 'computer', 'english', 'science']
# k = -len(words)   #Número de objetos en la lista
# while words:
#     print(words[k])   #Va a imprimir sin parar despair
#     del words[k]      #Va a borrar de la lista dispair
#     k +=1
#     print(words)     #Va a imprimir la lista cada que el bloque termine


# words = ['despair', 'phone', 'computer', 'english', 'science']
# print(dir(words))   #Devuelve una lista que contiene los nombres de los métodos que utiliza python en segundo plano, así como nosotros
# print(words.__getitem__(0))   #Usando puramente el método que tiene la lista


# words = ['despair', 'phone', 'computer', 'english', 'science']
#
# for index in range(0, len(words)):
#     print(words[index])
#
# print('--------------------------')
# for letter in words:    #No necesito contador, el número de elemento lo tiene la lista
#     print(letter)     #Esto es más Pythonic
#                         #letter esta apuntando a cada variable que esta en la lista


# for k in range (5):
#     print(k)

# Write a program that repeatedly asks the user to enter a number. Of the niumber es positive, add it to a running total. If the number
#is negative, stop the loop and print the final total

# SUM OF POSITIVE NUMBERS
# summ = 0
# while True:
#      num = int(input('Enter a number:  '))
#      if num < 0:
#           print(summ)
#           break
#      summ += num


