'''
Comprobar si una palabra es palindromo utilizando lambda
'''
palindromo = lambda palabra : palabra == palabra[::-1]
print(palindromo("anana"))