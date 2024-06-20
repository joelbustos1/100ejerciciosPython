'''
Calcular el IMC e interpretarlo
'''
peso = int(input("Ingresa tu peso en kg"))
altura = float(input("Ingresa tu altura en metros"))

imc = peso / (altura ** 2)
if imc < 18.5:
    print("Peso inferior al normal")
elif 18.5 < imc < 24.9:
    print("Peso normal")
elif 25 < imc < 29.9:
    print("Peso superior al normal")
else:
    print("Obesidad")