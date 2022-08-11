
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #executa sem precisar do ()
    def nome(self):
        return self.__nome.title()

    @nome.setter #executa sem precisar do ()
    def nome(self, nome):
        self.__nome = none
