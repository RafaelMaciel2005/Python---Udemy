class Impressora:

    def imprimir(self, dado):
        
        if isinstance(dado, str):

            print(f"Imprimindo texto {dado}")

        elif isinstance(dado, list):
            print("Imprimindo lista de textos") 

            for item in dado:
                print(f" - {item}")   

        elif isinstance (dado, dict):

            print("Imprimindo diconário de textos")

            for item in dado:

                print(f" - {item}")      

        else:
            print("Tipo de dado não suportado para impressão")

impressao = Impressora()
impressao.imprimir("Rafael")    
impressao.imprimir(["Rafael", "Maciel"])   
impressao.imprimir({"Rafael": "Maciel"})                       