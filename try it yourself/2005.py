# def my_ func(*, c1, c2):
#     pass
#
# my_func(c1 = 'h', c2='d')

print(range(7))

print(*range(7))    #unpacking

print(*[1,2,3])
#args
#kargs

my_range = range (7)
print(my_range)
print(*my_range)
my_list = [1, 2, 3, 4]
print(*my_list)


days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']    #Packing

# rest, school, free = days        #Error
rest, *school, free = days

print(rest)   #monday
print(school)  #tuesday, wednesday, thursday
print(free)    #friday

# COMPREHENSION

from random import gauss
my_numbers = []
for num in range(10):
    my_numbers.append(gauss())

print(my_numbers)

# __________________________________________________________
from random import gauss

my_numbers = [gauss() for num in range(10)]
print(my_numbers)