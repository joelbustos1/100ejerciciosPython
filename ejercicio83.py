'''
calcular la longitud de una lista de palabras utilizando map
'''
def longitud(palabra):
    return len(palabra)

palabras = ["gato", "perro", "jirafa"]
long_palabras = list(map(longitud, palabras))
print(palabras)
print(long_palabras)