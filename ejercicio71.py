'''
Crear una clase rectangulo con los siguientes atributos:
base: base del rectangulo
altura: altura del rectangulo
La clase debe tener los siguientes dos metodos:
** __init__(self, base, altura): inicializa los atributos aqui
** calcular_area(self): calcula y devuelve el area del rectangulo
** calcular_perimetro(self): calcula y devuelve el perimetro del rectangulo
'''
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base + self.altura) * 2
    
rec1 = Rectangulo(5, 3)
print(f"Area: {rec1.calcular_area()} Perimetro: {rec1.calcular_perimetro()}")