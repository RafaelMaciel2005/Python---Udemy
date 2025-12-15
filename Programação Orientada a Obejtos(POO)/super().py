class Veiculo:
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):

    def __init__(self, marca, modelo, cor):

        super().__init__(marca, modelo)
        self.cor = cor

    def exibir_info(self):

        super().exibir_info()
        print(f"Cor do carro: {self.cor}")

veiculo = Veiculo("Toyota", "Corolla")
veiculo.exibir_info()

carro = Carro("Honda", "Civic","Cinza")
carro.exibir_info()