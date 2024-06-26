'''
Escribe una funcion para saber si un numero es par o impar
'''
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

resultado = es_par(10)
print(resultado)