"""
One of the first known examples of encryption was used by Julius Caesar.
Read more about here: https://en.wikipedia.org/wiki/Caesar_cipher
Create a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and then display the shifted message.
Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift
values so that it can be used both to encode messages and decode messages.

# When you have done the code, try to decrypt the following:
ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                index = (ord(char) - ord('a') + shift) % 26
                encrypted_char = chr(ord('a') + index)
            else:
                index = (ord(char) - ord('A') + shift) % 26
                encrypted_char = chr(ord('A') + index)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

message = input("Ingresa un mensaje para codificar o decodificar: ")
shift = int(input("Ingrese la cantidad delturno (positiva para codificar, negativa para decodificar): "))

encrypted_message = caesar_cipher(message, shift)
print("Mensaje codificado o decodificado", encrypted_message)