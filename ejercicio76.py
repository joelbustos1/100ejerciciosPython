'''
Crear una clase animal con los atributos:
especie y nombre
La clase debe tener de metodos
init y hablar()
el metodo hablar nos retorna una palabra
segun la interpretacion del sonido como un perro
seria "guau"
'''
class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
    def hablar(self):
        if self.especie == "perro":
            return "guau"
        elif self.especie == "gato":
            return "miau" 
        else:
            return "...."
        
animal1 = Animal("perro", "Jorge")
print(f"mi mascota es un {animal1.especie}, se llama {animal1.nombre} y hace {animal1.hablar()}")

print(animal1.__dict__)