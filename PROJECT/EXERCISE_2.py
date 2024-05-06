"""Ej. 9.7. Aggregate claims have been modeled by a compound negative binomial distribution
with parameters r = 15 and ß = 5. The claim amounts are uniformly distributed on the
interval (0,10). Using the normal approximation, determine the premium such that the
probability that claims will exceed premium is 0.05. """

from scipy.stats import norm
# Parámetros para la distribución binomial negativa compuesta
r = 15
p = 5

# Parámetros para la distribución uniforme de los montos de reclamación
a = 0
b = 10

# Calcular la esperanza (media) de la suma de reclamaciones
E_N = r * p
E_X = (b-a) / 2
E_S = E_N * E_X

# Calcular la varianza de la suma de reclamaciones
Var_N = r * p * (1 + p)
Var_X = ((b - a) ** 2)/12
Var_S = E_N * Var_X + Var_N * (E_X) ** 2

# Calcular la desviación estándar de la suma de reclamaciones
std_dev_S = Var_S ** 0.5

# Calcular el percentil 95 de la suma de reclamaciones

# Obtener el percentil 95 de la distribución normal estándar
percentil_95 = norm.ppf(0.95)
percentile_95 = E_S + percentil_95 * std_dev_S

print("Esperanza (media) de S:", E_S)
print("Varianza de S:", Var_S)
print("Desviación estándar de S:", std_dev_S)
print("Percentil 95 de S:", percentile_95)

