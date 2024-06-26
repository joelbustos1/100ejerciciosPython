'''
Escribe una funcion que pida por teclado la distancia y la velocidad para poder calcular el tiempo de viaje
'''
def tiemp_viaje():
    distancia = int(input("Ingresa la distancia "))
    velocidad = int(input("Ingresa la velocidad "))
    return distancia / velocidad

resultado = tiemp_viaje()
print("el viaje va a durar", resultado, "horas")