# FUNCIÓN GENERADORA DE MOMENTOS DE LA DISTRIBUCIÓN GAMMA

from scipy.special import gamma

def gamma_moment(alpha, beta, k):
    return beta ** k * gamma(alpha + k) / gamma(alpha)

def generar_momento_gamma():
    alpha = float(input("Ingrese el valor del parámetro alpha (forma): "))
    beta = float(input("Ingrese el valor del parámetro beta (escala): "))
    k = int(input("Ingrese el orden del momento que desea calcular: "))

    momento = gamma_moment(alpha, beta, k)
    print(f"El momento de orden {k} de la distribución gamma con alpha={alpha} y beta={beta} es: {momento}")

generar_momento_gamma()