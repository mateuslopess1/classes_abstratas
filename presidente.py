from funcionario import Funcionario
from autenticavel import Autenticavel
class Presidente(Funcionario,Autenticavel):
    def __init__(self,nome,cpf,s,data):
        super().__init__(nome,cpf,s,data)
    def get_bonifica(self):
        return self.get_salario()*0.5+1000