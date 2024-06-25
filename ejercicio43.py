'''
Solicita al usuario ingresar un numero n e imprime el factorial de ese numero
ej: 5! = 5x4x3x2x1 = 120
'''
numero = int(input('ingrese un numero '))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i = i + 1
print("el factorial es", factorial)