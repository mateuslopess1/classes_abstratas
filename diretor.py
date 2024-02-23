from gerente import Gerente
class Diretor(Gerente):
    def __init__(self,nome,cpf,s,data,senha):
        super().__init__(nome,cpf,s,data,senha)
    def get_bonifica(self):
        return self.get_salario()*0.4