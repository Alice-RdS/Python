

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

    def __pode_sacar(self, valor_saque):
        valor_saque = self.__saldo + self.__limite
        return valor_saque

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Você não possui limite para este saque.")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property #executa get sem precisar do ()
    def saldo(self):
        return self.__saldo

    @property
    def titutar(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter #executa set sem precisar do ()
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def banco():
        return "001"

    @staticmethod
    def cods_banco():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}