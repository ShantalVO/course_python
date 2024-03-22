full_name = 'satoshi nakamoto'  # capitalize(), title()
print(full_name.capitalize())
print(full_name.title())

state = 'mississippi'  # count('ss'), count('pp'), count('ppp')
print(state.count('ss'))
print(state.count('pp'))
print(state.count('ppp'))

url = 'www.python.orgw'  # startswith('ww'), endswith('g'), endswith('.py'), strip('w'), rstrip('w'), lstrip('w')
print(url.startswith('ww'))
print(url.endswith('g'))
print(url.endswith('.py'))
print(url.strip('w'))
print(url.rstrip('w'))
print(url.lstrip('w'))

sentence = 'I saw a saw saw'  # find('saw'), rfind('saw'), find('jeje'), index('saw'), rindex('saw'), index('jeje')
print(sentence.find('saw'))
print(sentence.rfind('saw'))
print(sentence.find('jeje'))
print(sentence.index('saw'))
print(sentence.rindex('saw'))
# print(sentence.index('jeje')) no esta en a cadena y generará un error
try:
    noindex = sentence.index('jeje')
except ValueError:
    noindex = 0
print(noindex)


func = '5tAn(x)'  # upper(), lower(),
print(func.upper())
print(func.lower())

swap = 'AAAhhHaAhh'  # swapcase()
print(swap.swapcase())

song = 'LUMBERJACK'  # isupper(), islower()
print(song.isupper())
print(song.islower())

string = "I'm bad in Python"  # replace('bad', 'good')
print(string.replace('bad' , 'good'))

e = '2.71828'  # isalnum(), isalpha(), isdecimal(), isdigit(), isnumeric()
print(e.isalnum())
print(e.isalpha())
print(e.isdecimal())
print(e.isdigit())
print(e.isnumeric())

num = 18055  # isalnum(), isalpha(), isdecimal(), isdigit(), isnumeric()
numstr = str(num)
print(numstr.isalnum())
print(numstr.isalpha())
print(numstr.isdecimal())
print(numstr.isdigit())
print(numstr.isnumeric())

# Create a string where the istitle() method returns True
# Cadena con cada palabra inicial en mayúscula
a = 'La Universidad Es Formativa'
print(a.istitle())


# Create a string where the isspace() method returns True
# Cadena que solo tiene espacios en blanco
b = "    "
print(b.isspace())


# Create a string where you can use removeprefix() and removesuffix(). Hint: use a URL
# Cadena de URL
c = "http://www.calculo.com.mx.//"
prefix = "http://"
sufix = "//"
print(c.removeprefix(prefix).removesuffix(sufix))


# Create a valid object where you can use split() method
# Lista de palabras separadas por comas y espacios, en corchete
d = "llevar las llaves de la camioneta"
print(d.split())