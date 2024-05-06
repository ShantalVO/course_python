"""A word is palindrome if it is identical forward and backward.
Write a program that treads a word from the user to determine whether it is a palindrome.
Display the result, including a meaningful output message"""
#
# def palindrome(word):
#     word = word.lower()
#     return word == word[::-1]    # Valor boleano
#
# def main():
#     palabra = input("Ingresa una palabra: ")
#     if palindrome(palabra):
#         print(f"{palabra} es una palindrome :) ")
#     else:
#         print(f"{palabra} no es una palindrome :( ")
#
# if __name__ == "__main__":
#     main()

# OTRA FORMA
#
# def palindrome(word):
#     tam = len(word)   # lend: me dice cuántos caracteres tiene
#     ad = 0     # adelante
#     at = -1     # atrás
#     while ad <= tam-1 and at >= -tam:
#         if word[ad] == word[at]:
#             ad += 1
#             at -= 1
#         else:
#             print('Está palabra no es un palindromo ')
#             break
#     if ad > tam-1 or at < -tam:
#         print('Ésta palabara es un palindromo ')
#
# palindrome(input('Inserta una palabra: '))

# OTRA FORMA

# word = input('Enter a word: ')
# espal = True
# long = len(word)
#
# for i in range(long):
#     if word[i] != word[-i-1]:
#         espal = False
#         break
# if espal:
#     print(f'{word} is a palindrome')
#
# else:
#     print(f'{word} is not a palindrome')

# OTRA FORMA

word = input('Enter a word to verify if it is a palindrome: ')
word2 = ''
word_list = list(word)
word_list.reverse()

for _ in word_list:
    word2 = word2 + _

if word == word2:
    print('palindrome')
else:
    print('not palindrome')