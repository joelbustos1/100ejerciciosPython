'''
Escribe una funcion para calcular el volumen de un cilindro
V = pi r2 h
'''
import math
def volumen_cil(radio, altura):
    return math.pi * radio**2 * altura

resultado = volumen_cil(2, 5)
print(resultado)