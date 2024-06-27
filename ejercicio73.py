'''
Crear una clase Libro
atributos:
titulo, autor, editorial, anio de publicacion 
Metodos:
constructor para inicializar los atributos
'''
class Libro:
    def __init__(self, titulo, autor, editorial, anio):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
    
mi_libro = Libro("Pequenio hombre", "Joel", "elsa pato", "2024")
print(mi_libro.__dict__)
