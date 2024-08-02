'''
filtrar cadenas de longitud mayor que 3 de una lista, usando filter
'''
cadenas = ['python','php','java', 'javascript', 'ruby','go']
cadenasFiltradas = list(filter(lambda x: len(x) > 3, cadenas ))
print(cadenasFiltradas)
