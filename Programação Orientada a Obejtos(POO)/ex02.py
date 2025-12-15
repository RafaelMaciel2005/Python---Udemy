class pet:

    def __init__(self, _nome, _idade, _peso):
        
        self._nome = ""
        self._idade = 0
        self._peso = 0.0

    def get_nome(self):

        return self._nome
    
    def set_nome(self, novo_nome):

        if isinstance(novo_nome, str) and novo_nome != "":
            self._nome = novo_nome
        else:
            print("Nome inválido.")            