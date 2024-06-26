'''
Escribe una funcion para calcular el promedio de una lista de numeros
'''
def prom(lista1):
    return sum(lista1) / len(lista1)

resultado = prom([2, 4, 6, 8, 10])
print(resultado)