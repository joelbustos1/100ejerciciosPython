'''
Genere un numero entre 1 y 10.
Luego pide al usuario adivinar el numero hasta que  lo haga correctamente
'''
import random
numero_secreto = random.randint(1, 10)
intentos = 0

while True: #bucle infinito
    intento = int(input("Adivina el numero entre 1 y 10 "))
    intentos = intentos + 1
    if intento == numero_secreto:
        print(f"exito! tomo {intentos} intentos")
    else:
        print("vuelve a intentarlo")