'''
Imprime la tabla de multiplicar de un numero ingresado por el usuario
'''
numero = int(input("Ingrese un numero "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i = i + 1