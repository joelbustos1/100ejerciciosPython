'''
contar el numero de vocales en una lista de palabras utilizando map
'''
def contar(palabra):
    return sum(1 for letra in palabra if letra.lower() in "aeiou") #me va a retornar un 1 siempre que encuentre una vocal

palabras = ["hola", "mundo"]
conteos = list(map(contar, palabras))
print(palabras)
print(conteos)