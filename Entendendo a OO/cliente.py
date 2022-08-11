
class Cliente:

    def __init__(self, nome):
        self.nome = nome

    @property #executa sem precisar do ()
    def get_nome(self):
        return self.nome.title()

