'''
Solicitia al usuario ingresar un numero y contar cuantos digitos tiene
'''
numero = int(input("Ingrese un numero: "))
contador = 0
while numero != 0:
    numero = numero // 10
    contador = contador + 1
print("digitos son", contador)