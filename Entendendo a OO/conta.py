

class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite = 1000.0):

        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("{}, o seu saldo é {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)