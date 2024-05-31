ra = range(1, 10, 2)    # Estoy usando esta función solo como un posicional, porque digo que 1 es el inicio,
                        # 2 el final y 2 es el paso

# Defining a function with positional - only
def func1(value1, value2, value3, /):
    print(value1/value3 + value2)

# func1(value1=1, value2=5, value3=10)

# positional - or - keyword with a built-in

com = complex(imag=8, real=1)
com2 = complex(real=1, imag=5)
com2 = complex(5,4)
com4 = complex(imag=10)  # Con un solo número porque tengo los parámetros con '...' valores vacios
print(com4)

# defining a function with positional- or- keyword

def func2(r, i=0):
    print(f'{r}+{i}j')

func2(i=4, r=8)  #argumentos posicionales

# keyword only

def func3(pos1, *, live, student = ' '):
    print(live + student + str(pos1))
func3(5, live='true', student = 'jake')    # Estoy cambiando el valor ue ya tenía student

def some(obs, k_or_guess, my_iter='20', /, thresh='1e-0.5', check_finite='True', *, seed= 'None'):
    print(obs+k_or_guess+my_iter+thresh+check_finite+seed)

some('hola', 'adios', seed='example')
