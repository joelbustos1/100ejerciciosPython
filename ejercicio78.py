'''
Crear una clase persona y otra clase estudiante
la clase persona tiene el atributo nombre y el metodo mostrar_nombre()
la clase estudiante debe heredar de la clase persona y utilizar el metodo mostrar_nombre()
de la clase persona
'''
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostar_nombre(self):
        print(self.nombre)

class Estudiante(Persona):
    pass

estudiante1 = Estudiante("Joel")
estudiante1.mostar_nombre()