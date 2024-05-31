# ANONYMUS INLINE FUNCTION
#
# def f(x): return x*x    # print(f(2))   4
#
# g = lambda x: x*x
# print(g(2))    # 4
#
# # Or
# print((lambda x: x*x)(2))    # 4


# ___________________________________________________

# for item in map(
#                 lambda x, y: 2*x**y,
#                 [1, 2, 3],
#                 [0.1, 0.2, 0]):
#     print(item)


# ___________________________________________________
# EJEMPLO
# Quiero los nombres de éstas personas con su inicial en mayúsculas

# names = ['jake', 'esteban', 'fred', 'Tim']
#
# corrected_names = map(lambda name: name.title(), names)   # iterator
#
# print(list(corrected_names))
#
# # for item in corrected_names:    # Si losquiero por separado
# #     print(item)

# # for item in corrected_names:    # Si los quiero por separado en un renglon
# #     print(item, end=0)

#_____________________________________________________________

my_grades = [
    ('linear algebra', 8.8)
    ('differenial calculos', 2.0)
    ('actuarial calculus II', 9.4)
    ('probability theory', 1.0)
]

# test = lambda grad: grad[1] >=3
#
# # print(test(my_grades[0]))
#
# x = filter(test, my_grades)
# print(list(x))

for t in range(4):
    print(my_grades[t][1])

# _______________________________________________________
# def f(*args)
#     print(args)
#
# f(5, 7, 8, 9, 10)
#
# def my_func(*numbers, **letters):
#     return numbers, letters
#
# a = my_func( 5,7, 9, 10, 54, a=1, b=5)
# print(a[1]['b'])

