from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self,nome,cpf,s,data,senha):
        super.__init__(nome,cpf,s,data)
        self._senha = senha
    def get_bonifica(self):
        return self.get_salario()*0.3
    def autenticar(self, senha):
        return senha == self._senha