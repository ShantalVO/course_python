#OPERADORES PARA USAR CON LAS LISTAS

#OPERADOR ASIGNACIÓN PARA PODER MODIFICAR ALGÚN ELEMENTO DE LA LISTA
my_list =['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0] = 'sin(x)'  #Modifica la posicion 0 con el elemento sen(x)
print(my_list)
my_list [1] = 'cos(x)'
print(my_list)
my_list [2] = 'tan(x)'
print(my_list)

#REEMPLAZAR POR EL CONTENIDO DE UN ITERABLE EN PASOS DE UNO
my_list =['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0:3] = ['sin(x)', 'cos(x)', 'tan(x)']  #El 3 no se incluye, reemplazar del 0 al 3 por los elementos de este renglon
                                               # El iterable es una lista, lo que hice en el anterior ejemplo, pero ahora en 1 línea
print(my_list)


#REEMPLAZAR POR EL CONTENIDO DE UN ITERABLE EN PASOS DE DOS
my_list =['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0:5:2] = ['sin(x)', 'cos(x)', 'tan(x)']
print(my_list)

#ELIMNINA ELEMENTOS EN ESPECÍFICO
my_list =['sin', 'cos', 'tan', 'f(x)', 'g(x)']
del my_list[0]  #El del elimina lo que esta en la posición 0  ---del es un key word---
print(my_list)
del my_list[0:3] #Elimina del índice 0 hasta el índice 3
print(my_list)
del my_list[0:5:2]
print(my_list) #Considerando lo que este en la posición del 0 al 5, borrará en pasos de 2,
               # como ya solo me sobraba un elemento en el paso anteriorior, entonces arrojará 0


# += EXTIENDE LA SECUENCIA CON LOS CONTENIDOS DEL ITERABLE, s+=t donde t es un iterable
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list += ['python', 'C', 'R']
print(my_list)

# *= ACTUALIZA LA SECUENCIA CON LOS CONTENIDOS REPETIDOS N-VECES s*= n donde n es un int
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list *= 2   #Quiero repetir dos veces los elementos de esta lista
print(my_list)



#LIST.METHOD()

#AGREGAR OPERADORES AL FINAL DE LA LISTA
fruits = []
print(fruits)
fruits.append('apple')
fruits.append('grape')
print(fruits)


#ELIMINA LOS ELEMENTOS DE LA LISTA
fruits.clear()
print(fruits)


#CREA UNA COPIA DE LA LISTA, pero no transfiere todos los elementos, solo una copia
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors.copy()
print(at_copy)
#Ahora, aparentemente es lo mismo, pero veamos que no son en sí el mismo objeto
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors.copy()
print(id(at_copy))
print(id(authors))
#Comprovar si es la misma identidad
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors.copy()
print(authors is at_copy)

#OTRA FORMA CON OPERADOR SLICING
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors [:]    #Hazme una copia de todos los elementos de la lista authors
print(at_copy)  #Funciona igual que el método copy


#EXTENDER LA LISTA CON CONTENIDOS DE ITEABLES +=
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_variable = my_list.extend(['python', 'C', 'R'])
print(my_variable)    #None: algo vacio, por lo tanto no se puede a abordar en variables

my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list.extend(['python', 'C', 'R'])
print(my_list)        #Aquí sí agrega los elementos a la lista


#AGREGA UN OBJETO x EN EL INDICE i (i,x)
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
my_list.insert(1, 'arctan')  # Lo va a agregar en el índice 1 --- 0,1,2...
print(my_list)


#IDINTIFICA EL OBJETO DEL INDICE Y DEPUÉS LO REMUEVE
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
popped = my_list.pop()   #Si lo uso sin nada me va a retornar y a eliminar el objeto g(x)
print(popped, my_list)  #Imprimo el objeto eliminado y retornato y después la lista ya modificada
popped = my_list.pop(0)  #Si quiero algo más específico, quiero que me elimine y retorne lo que esta en el índice 0, estoy considerando el codigo anterior por eso me quita sin
print(popped, my_list)


#ELIMINA EL PRIMER OBJETO x DE LA LISTA
words = ['red', 'read', 'red']  #Teng 2 veces el mismo objeto
words.remove('red')  #Elimina la primera ocurrencia
print(words)
#Considerando lo anterior
words.remove('red')  #Elimina la primera ocurrencia
print(words)


#REVERTIR LOS ELEMENTOS DE LA LISTA
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
my_list.reverse()    #El método modifica la lista, si quiero regresar a la original tengo que aplicar de nuevo un reverse
print(my_list)

#RETORNA UNA NUEVA LISTA Y NO MDFIFICA LA SECUENCIA
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
my_list.reverse()    #El método modifica la lista, si quiero regresar a la original tengo que aplicar de nuevo un reverse
print(my_list)
print(sorted(my_list)) #Me va a dar una lista  con un orden ascendente, los strings tienen un código que los identifica y con eso los odena


#CONTEMPLANDO UN ORDEN ENTRE ITEMS
my_list = [45, -8, 52.14, 3.14, 0]
my_list.sort()  #Va de menor a mayor y modifica la lista
print(my_list)
#Si quiero que no modifique el orden
my_list = [45, -8, 52.14, 3.14, 0]
print(sorted(my_list))  #No modifica el ordeb
print(my_list)



#MÉTODOS DE LOS STRINGS QUE SE PUEDEN USAR CON LISTAS

#RETORNAR NÚMERO DE OCURRENCIAS DEL VALOR QUE LE ESTOY DANDO
my_list = [45, -8, 52.14, 3.14, 0, 0, 0]
print(my_list.count(0))  #Imprime cuantas veces esta el 0

#otro ejemplo
print('jaja'.count('j'))


#RETORNA EN QUE ÍNDICE ESTA EL OBJETO QUE YO ESTOY INDICANDO, ME ARROJA UN ERROR SI EL ÍNDICE NO ESTA PRESENTE
my_list = [45, -8, 52.14, 3.14, 0, 0, 0]
print(my_list.index(0))  #Me va a retornar el de la primera ocurrencia: index = 4   0,2,3,4,...
#Si pongo un número que no esta me va a arrojar un error
#otro ejemplo
print('jaja'.index('j')) #No tengo ninguna j sola
