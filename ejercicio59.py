'''
Pedir a un usuario un numero e imprimir la tabla de multiplicacion de dicho numero
'''
numero = int(input("Ingresa un numero "))
for i  in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i}:", resultado)