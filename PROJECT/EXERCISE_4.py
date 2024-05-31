# Función para separar las letras del nombre en tuplas
def separar_en_tuplas(nombre):
    return tuple(nombre)


# Función para invertir el nombre
def invertir_nombre(nombre):
    return nombre[::-1]


# Función para obtener las vocales del nombre
def obtener_vocales(nombre):
    vocales = "aeiouAEIOU"
    return [letra for letra in nombre if letra in vocales]


# Función principal
def main():
    nombre = input("Por favor, ingresa tu nombre: ")

    # Separar letras en tuplas
    letras_en_tuplas = separar_en_tuplas(nombre)
    print("Letras en tuplas:", letras_en_tuplas)

    # Nombre de derecha a izquierda
    nombre_invertido = invertir_nombre(nombre)
    print("Nombre de derecha a izquierda:", nombre_invertido)

    # Vocales en el nombre
    vocales = obtener_vocales(nombre)
    print("Vocales en el nombre:", vocales)

    # Letra inicial y final
    letra_inicial = nombre[0]
    letra_final = nombre[-1]
    print("Letra inicial:", letra_inicial)
    print("Letra final:", letra_final)

    # Número de letras en el nombre
    numero_de_letras = len(nombre)
    print("Número de letras en el nombre:", numero_de_letras)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
