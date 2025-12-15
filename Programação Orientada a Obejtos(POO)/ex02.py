class pet:

    def __init__(self):
        
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

    def get_idade(self):

        return self._idade
    
    def set_idade(self, nova_idade):

        if isinstance(nova_idade, int) and nova_idade >= 0:           
            self._idade = nova_idade

        else:
            print("Idade inválida.")

    def set_peso(self, novo_peso):

        if isinstance(novo_peso, float) and novo_peso > 0: 

            self._peso = novo_peso   
        else:
            print("Peso inválido.")     

    def exibir_info(self):
        print("NOME: {}".format(self._nome))         
        print("IDADE: {}".format(self._idade))
        print("PESO: {}kg".format(self._peso))

meu_pet = pet()
meu_pet.set_nome("Bob")
meu_pet.set_idade(8)    
meu_pet.set_peso(39.6)
meu_pet.exibir_info()    