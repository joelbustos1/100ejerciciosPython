'''
Obtener la cantidad de memoria RAM en mi computadora
'''
import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total / (1024 **3)
    return memoria_total

memoria = obtener_ram()
print("Total de RAM:", memoria, "GB")