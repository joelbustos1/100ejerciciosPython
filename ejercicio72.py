'''
Crear una clase circulo con los siguientes atributos:
* radio: radio del circulo
La clase debe tener los siguientes metodos:
* __init__(self, radio): inicializa los atributos de la clase 
* calcular_area(self): calcula y devuelve el area del circulo
* calcular_perimetro(self): calcula y devuelve el perimetro del circulo
'''
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    def calcular_perimetro(self):
        diametro = self.radio * 2
        return math.pi * diametro

circulo1 = Circulo(5)
print(f"Area: {circulo1.calcular_area()} Perimetro: {circulo1.calcular_perimetro()}")