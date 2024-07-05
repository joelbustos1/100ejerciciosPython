'''
Representa una cuenta bancaria con deposito y retiro
debe haber un titular y un saldo
Utiliza POO
'''
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"se desposito: {cantidad}")

    def retirar(self, cantidad):
        self.saldo -= cantidad
        print(f"se retiro: {cantidad}")

    def mostrar(self):
        print(self.__dict__)

cuenta1 = Cuenta("Joel", 500)
cuenta1.mostrar()
cuenta1.depositar(1500)
cuenta1.mostrar()
cuenta1.retirar(1300)
cuenta1.mostrar()
