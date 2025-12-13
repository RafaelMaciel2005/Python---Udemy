class fruta:

    def __init__(self, nome, preco_por_kg, quantidade_estoque):

        self.nome = nome
        self.preco_por_kg = preco_por_kg
        self.quantidade_estoque = quantidade_estoque

banana = fruta("Banana", "R$6,80", 7.5)        
lichia = fruta("Lichia", "R$21,90", 3.5) 

print("Nome da Fruta: {}".format(banana.nome))
print("O preço por kilograma da banana é: {}".format(banana.preco_por_kg))
print("A quantidade em estoque da banana é: {}".format(banana.quantidade_estoque))

print("_________________________________________________________")

print("Nome da Fruta: {}".format(lichia.nome))
print("O preço por kilograma da lichia é: {}".format(lichia.preco_por_kg))
print("A quantidade em estoque da lichia é: {}".format(lichia.quantidade_estoque))
