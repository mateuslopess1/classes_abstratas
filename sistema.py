class Sistema:
    def login(self,objeto):
        try:
            if objeto.autenticar('senha'):
                print('Logado')
            else:
                print('Não logado')
        except AttributeError:
            print('Não autenticavel')