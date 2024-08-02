'''
Duplicar cada elemento de una lista usando map y lambda
'''
lista = [1, 2, 3, 4, 5]
duplicados = list(map(lambda X: X*2, lista))
print(f"lista original: {lista} lista duplicada: {duplicados}")