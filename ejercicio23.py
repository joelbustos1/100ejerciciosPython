'''
Verifica si una palabra es un palindromo
'''
palabra = "oso"
es_pa = palabra == palabra[::-1]
print("la palabra es palindromo:", es_pa)