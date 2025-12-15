class SensorVelocidade:

    def __init__(self, velocidade):

        self._velocidade = 0
        self.velocidade = velocidade

    @property
    def velocidade(self):

        return self._velocidade
    
    @velocidade.setter
    def velocidade (self, valor):
        if valor >= 0.0:
            self._velocidade = valor
        else:
            print("Velocidade inválida.")    

    def exibir(self):
        print("A velocidade é: {} Km/Hr".format(self._velocidade))

vel = SensorVelocidade(60)
vel.exibir()

vel.velocidade = -10   # inválido
vel.exibir()
            