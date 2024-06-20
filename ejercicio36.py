'''
Pide un caracter y determina si es una vocal
'''
caracter = input("introduce un caracter")
vocales = ["a", "e", "i", "o", "u"]
if caracter.lower() in vocales:
    print("es una vocal")
else:
    print("no es una vocal")