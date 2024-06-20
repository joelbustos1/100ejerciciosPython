'''
Solicita al usuario que ingrese un numero N y luego imprime una suma de todos los numeros desde 1  hasta N
'''
n = int(input("Ingresa un numero"))
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
print("la suma es:", suma)