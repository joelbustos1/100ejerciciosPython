'''
filtrar numeros pares de una lista utilizando filter
'''
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numerosPares = list(filter(lambda x: x % 2 == 0, listaNumeros))
print(f"Lista de numeros original: {listaNumeros} y lista de numeros pares: {numerosPares}")