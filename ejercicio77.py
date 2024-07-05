'''
Crear una clase llamada persona
con los atributos: nombre, edad
un constructor, donde los datos pueden estar vacios
los setters y getters
para cada uno de los atributos
mostrar(): muestra los datos de la persona 
esMayorDeEdad(): devuelve un valor logico
indicando si es mayor de edad
'''
class Persona:
    def __init__(self, nombre=None, edad=None):        #=None es para decir que es opcional o vacio
        self._nombre = nombre          #modificador de acceso _ 
        self._edad = edad

    @property                          #decordador property
    def nombre(self):  
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre == nuevo_nombre

    @property                          #decordador property
    def edad(self):  
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad == nueva_edad

    def mostrar(self):
        print(self.__dict__)

    def esMayorDeEdad(self):
        if self._edad >= 18:
            return True
        else:
            return False
        
persona1 = Persona("Joel", 20)
persona1.mostrar()
print(persona1.esMayorDeEdad())