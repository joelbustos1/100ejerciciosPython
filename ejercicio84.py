'''
Obtener el cuadrado de la suma de dos listas de numeros utilizando map
'''
def custom_suma(a, b):
    return (a+b) ** 2

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
suma_de_listas = list(map(custom_suma, lista1, lista2))
print(lista1)
print(lista2)
print(suma_de_listas)