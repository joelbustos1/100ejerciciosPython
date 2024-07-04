'''
Crear una clase coche con los atributos:
marca, modelo, matricula, km
Con los metodos:
init como constructor
avanzar(km) este aumenta
el valor de km en la cantidad
'''
class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km
    def avanzar(self, km):
        self.km = self.km + km
    
coche1 = Coche("Ford", "Fiesta", "ABC DEF", 5000)
print(coche1.__dict__)
coche1.avanzar(3000)
print(coche1.__dict__)

