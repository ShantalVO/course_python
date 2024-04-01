# For each point, use the print() function

# 1. Use 'in' operator to obtain a True value
# a = 'Hay que tener cuidado al usar Python '
# suba = 'Python'
# print(suba in a)  # Verifica si la subcadena (suba) esta en la cadena (a)
print('5' in '512')



# 2. Use not in operator to obtain a True value
# sube = "dominio"
# print(sube not in a)
print('5' not in '12')



# 3. Use * operator with a string (as you want) (* es el operador de repetición)
# subi = a * 2
# print(subi)
print('.py' * 2)  # El objeto tiene que ser int no es válido con float



# 4. Use + operator with a string and with a list(as you want) (+ es el operador de concatenación)
# a = 'Programando '
# b = 'en '
# c = 'Python '
# print(a + b + c)
print('hello' + ' ' + 'word')


# ------------------- Slicing for strings-----------------------
# We can use s[i:j:k] to make a slicing in python, solve each point [inicio: final: paso o step]



# 5. From the sentence, print out "is a logical consequence of the axioms and previously proved theorems"
sentence = """In mathematics, a theorem is a statement that has been proved, or can be proved. The proof of a theorem 
is a logical argument that uses the inference rules of a deductive system to establish that the theorem 
is a logical consequence of the axioms and previously proved theorems."""

#index = sentence.index('is') # Lee de izquirda a derecha hasta encontrar el subíndice
index = sentence.rindex('is') #Leyendolo de derecha a izquierda retorna el indice más grande
print(index)
print(sentence[index:])   #Slicing del índice hasta el final del string

#OTRA FORMA MÁS PYTHONIC
print(sentence[sentence.rindex('is'):])  #[sentence.rindex('is    retorna el número
                                         # :   indica que es del principio al final de la oración
                                         # print(sentence   me dice lo que estoy buscado

# 6.From the user's input, print the name, but beginning with the last names. Make sure each first letter is capitalized
# sheldon axler -> Axler Sheldon

#name = input('What is your full name? ') #UNCOMMENT WHEN YOU USE THIS
#print(name.title())

#OTRA FORMA
name = input('What is your full name? ') #UNCOMMENT WHEN YOU USE THIS
my_split = name.split()  #split pone los elementos del String en una lista para poder modificar el orden del string
print(my_split)
# print(my_split[-1], my_split[0]) #Accedo a la lista al elemento último [-1] y al primero elemento [0], solo me lo da en minusculas
print(my_split[-1].capitalize(), my_split[0].capitalize())

#OTRA FORMA
#name = input('What is your full name? ').title() #UNCOMMENT WHEN YOU USE THIS #Poner el método en el input,
                                                     # porque el método siempre va retornar un string
#my_split = name.split()
#print(my_split)
#print(my_split[-1], my_split[0])


# 7. 'tcerroc eht tuo tnirp dna ti esrever tsuJ .od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT'
print('tcerroc eht tuo tnirp dna ti esrever tsuJ .od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT' [::-1])
# La intención es hacer un slicing

# 8. The frog jump two letters in the mot string. What is the final string?
mot = 'you are doing well. Do not doubt on you!'
print(mot[::2])   #Un sí uno no

# 9. From the sentence variable, how many characters are in there?
print(len(sentence))