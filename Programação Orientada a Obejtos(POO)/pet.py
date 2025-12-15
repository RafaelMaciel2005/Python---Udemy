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

while True:
   
    print("---MENU---")
    print("1 - Definir o nome do pet")
    print("2 - Definir a idade do pet")
    print("3 - Definir o peso do pet")
    print("4 - Exibir informações do pet")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:

        nome = str(input("Digite o nome:"))
        meu_pet.set_nome(nome)

    elif opcao == 2:

        idade = int(input("Digite da idade:"))
        meu_pet.set_idade(idade)

    elif opcao == 3:

        peso = float(input("Digite o peso do pet:"))
        meu_pet.set_peso(peso)

    elif opcao == 4:

        print("Exibindo informações...")
        meu_pet.exibir_info()

    elif opcao == 5: 
        
        print("Saindo...")

        break  
    else:
        print("Opção inválida...") 