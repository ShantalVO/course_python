"""
Use Nilakantha's series to approximate pi.
Show 15 approximations of pi.The first approx should be the first term of the series, the second approx the second term
and so on
pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...

https://i1.wp.com/www.glc.us.es/~jalonso/exercitium/wp-content/uploads/2017/02/Calculo_de_pi_mediante_la_serie_de_Nilakantha.png?resize=571%2C83
"""

def nilakantha_series(num_approx):
    pi_approx = 3.0
    sign = 1.0
    denominator = 2.0
    for i in range(num_approx):
        pi_approx += sign * 4 / ((denominator) * (denominator + 1) * (denominator + 2))
        sign *= -1
        denominator += 2
        print("Aproximación {}: {:.15f}".format(i+1, pi_approx))

num_approximations = int(input("Ingrese el número de aproximciones de pi que desee calcular: "))
nilakantha_series(num_approximations)