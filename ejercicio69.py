'''
Escribe una funcion para calcular la tasa de desempleo
td = no_desempleados / fuerza_laboralx100
'''
def tasa_desemp(nodes, fuerlab):
    return (nodes / fuerlab) * 100

resultado = tasa_desemp(100, 400)
print(resultado)