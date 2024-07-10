'''
Convertir una lista de cadenas que sean numeros a enteros utilizando map
'''
def convertir_numeros(cadena):
    return int(cadena)

cadenas = ["1", "2", "3", "4", "5"]
enteros = list(map(convertir_numeros, cadenas))
print(cadenas)
print(enteros)
