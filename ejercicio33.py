'''
Determina si el año es bisiesto
regla de negocio
    -divisible por 4
    -no divisible por 100
    -divisible por 400
'''
anio = 2024
if (anio % 4 == 0 and anio % 100 != 0) or \
(anio % 400 == 0):
    print("es un anio bisiesto")
else:
    print("no es anio bisiesto")
