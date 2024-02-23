from abc import ABC,abstractmethod
class Funcionario(ABC):
    def __init__(self,nome,cpf,s,data):
        self._nome = nome
        self._cpf = cpf
        self._salario = s
        self._data_nasc = data
    def get_salario(self):
        return self._salario
    @abstractmethod
    def get_bonifica(self):
        pass