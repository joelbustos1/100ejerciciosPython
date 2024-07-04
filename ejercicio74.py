'''
Crear una clase persona con los atributos :
*** nombre, edad, dni
Con  los metodos:
init()
es_mayor_de_edad() este retorna True si es mayor de edad
'''
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        
persona1 = Persona("Joel", 21, 44960377)
print(f"el nombre es: {persona1.nombre}")
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("Es menor de edad")