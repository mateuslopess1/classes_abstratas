from autenticavel import Autenticavel
class Cliente(Autenticavel):
    def __init__(self,nome,senha):
        self._nome = nome
        self._senha = senha
    def autenticar(self, senha):
        return senha == self._senha