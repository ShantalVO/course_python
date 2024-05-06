# Generate and print the first 10 numbers in the Fibonacci sequence
#
# def func_fibonacci(n):
#     fib_seq = [0, 1]
#     for i in range(2, n):
#         fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
#     return fib_seq
# print(func_fibonacci(10))


#_________________________________________________________________________________________________________________
# SIN RECUERSION DE FUNCIONES

a, b = 0, 1
for _ in range(10):
    print(a, end = ' ')
    a, b = b, a + b
