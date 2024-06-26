'''
Escribe una funcion para clasificar si una sustancia es acida, basica o neutra segun su ph
'''
def clasif(ph):
    if ph < 7:
        return "es acida"
    elif ph > 7:
        return "es basica"
    else:
        return "es neutra"
    
resultado = clasif(7)
print(resultado)