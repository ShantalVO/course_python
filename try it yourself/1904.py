# a = range(2,10, 2) #empezar en 2, terminar en 10 en pasos de 2
# for num in a:
#     print(num)

# a = range(2,10)
#
# a[4] = 7

# iteration: el proceso de ir a traves de los elementos de una coleccion
# iterable: es un objeto  con un mètodo __iter__, podemos usar el [] para tener los elementos del objeto
# iterator: objeto con un __next__method

# print(zip('aaa', (1, 2, 3)))  #hay 2 iterables
# print(dir(zip('aaa', (1, 2, 3))))  # es un iterable y un iterator aparece cuando lo imprimo

names = ['Hamilton', 'Checo', 'Leclerc']
teams = ['Mercedes', 'Red Bull', 'Ferrari']
# hamilton mercedes
# checo red bull

# for name in names:
#     for team in teams:
#         print(name, team)  #Me da todas a combinaciones

# for name in zip(names, teams):
#     print(name)   #Me va a dar tuplas

# for name in zip(names, teams):
#     print(name[0])   #Me va a dar tuplas
#     print(name[1])

# for t in zip(names, teams):
#     print(t)  #Elemnetos de zip
#     print(t[0])
#     print(t[1])


# for n, t in zip(names, teams):
#     # print(n, t)   #desempaquetados los elementos de zip
#     print(n.upper())   #para los names
#     print(t.count('a'))  #para los teams


#ENUMERATE

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(dir(enumerate(seasons)))  #se puede convertir en un iterator

# for _ in enumerate(seasons):
#     print(_[0])  #acceder solo a los indices
#     print(_[1])  # acceder a los valores

#Para no comenzar en 0
# for _ in enumerate(seasons, start=2):
#     print(_[0])  #acceder solo a los indices
#     print(_[1])  # acceder a los valores

s = 'cat'
print(s[0]) # here we use the dunder method __getitem__
# Here we are using dunder method
for let in s:
    print(let)
# print(dir(s))

# Next method acceder a los elemento cuando los necesitemos

# s_iterator = iter(s)
# print(s_iterator)
# print(dir(s_iterator))

s_iterator = iter(s)
print(next(s_iterator))
print(next(s_iterator))
print(next(s_iterator))
