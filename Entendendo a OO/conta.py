

class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite = 1000.0):

        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("{}, o seu saldo é {}".format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor