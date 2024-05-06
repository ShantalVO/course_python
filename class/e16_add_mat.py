"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).

"""
#
# def add(matrix1, matrix2):
#     result = []
#     for i in range(len(matrix1)):
#         row = []
#         for j in range(len(matrix1[0])):
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result.append(row)
#     return result
#
# # Example
# matrix1 = [[1, -2], [-3, 4]]
# matrix2 = [[2, -1], [0, -1]]
# print(add(matrix1, matrix2))
#
# matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
# print(add(matrix1, matrix2))

# # OTRA FORMA
# def add(matrix1, matrix2):
#     result = [[] for _ in range(len(matrix1))]   # Se crea una lista para la longitud de la matriz
#     k, j = 0, 0
#     while k < len(matrix1):
#         while j < len(matrix1[k]):
#             result[k].append(matrix1[k][j] +matrix2[k][j])
#             j += 1
#         j = 0
#         k += 1
#     return result
#
# s = add(((1, 1, 1), (1, 1, 1)), ((1, 1, 1), (1, 1, 1)))
# print(s)

# OTRA FORMA

my_matrix1 = [[1, 1], [2,3], [2, 3]]
my_matrix2 = [[4, 4], [5,5], [2, 3]]

def add(matrix1, matrix2):

    result = [[] for _ in range(len(matrix1))]

    my_matrix_one_one = zip(matrix1, matrix2)
    r = -1
    for i, k in my_matrix_one_one:
        r += 1
        for m, n in zip(i, k):
            result[r].append(m + n)
    print(result)

add(my_matrix1, my_matrix2)