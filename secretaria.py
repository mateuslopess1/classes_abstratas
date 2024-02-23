from funcionario import Funcionario
from autenticavel import Autenticavel
class Secretaria(Funcionario,Autenticavel):
    pass

class SecAdministrativa(Secretaria):
    def __init__(self,nome,cpf,s,data,senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = s
        self._data_nasc = data
        self._senha = senha
    def get_bonifica(self):
        return 100
    def autenticar(self, senha):
        return senha == self._senha
class SecExecutiva(Secretaria):
    def __init__(self,nome,cpf,s,data,senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = s
        self._data_nasc = data
        self._senha = senha
    def get_bonifica(self):
        return self.get_salario()*0.1+100
    def autenticar(self, senha):
        return senha == self._senha