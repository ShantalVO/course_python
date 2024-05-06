"""Ej. 3.36 Consider an exponential distribution with Θ = 500 and a Pareto distribution with
 a = 3 and Θ = 1,000. Determine VaR and TVaR at the 95% security level.
"""

import numpy as np

# Solicitar al usuario los valores de theta y alfa
theta_exponential = float(input("Ingrese el valor de theta para la distribución exponencial: "))
alpha_pareto = float(input("Ingrese el valor de alfa para la distribución de Pareto: "))
theta_pareto = float(input("Ingrese el valor de theta para la distribución de Pareto: "))

# Nivel de confianza (1 - alpha)
confidence_level= float(input("Ingrese el nivel de confianza: "))

# Calcular VaR y TVaR para la distribución exponencial
var_exponential = theta_exponential * np.log(1 / (1 - confidence_level))
tvar_exponential = theta_exponential * np.log(1 / (1 - confidence_level)) + theta_exponential

# Calcular VaR y TVaR para la distribución de Pareto
var_pareto = theta_pareto * ((1-confidence_level) ** (-1/alpha_pareto)-1)
tvar_pareto = var_pareto + ((theta_pareto * (1 - confidence_level) ** (-1/alpha_pareto))) / (alpha_pareto-1)

print("VaR para la distribución exponencial:", var_exponential)
print("TVaR para la distribución exponencial:", tvar_exponential)
print("VaR para la distribución de Pareto:", var_pareto)
print("TVaR para la distribución de Pareto:", tvar_pareto)
