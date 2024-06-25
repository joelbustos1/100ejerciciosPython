'''
Hacer un menu de opciones que incluya la opcion de salir del programa
'''
while True:
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Salir")

    opcion = int(input("Escribe tu opcion "))

    if opcion == 1:
        print("usted esta sumando")
    elif opcion == 2:
        print("Usted esta restando")
    elif opcion == 3:
        break
    else:
        print("No es una opcion valida")

print("Vuelve pronto")