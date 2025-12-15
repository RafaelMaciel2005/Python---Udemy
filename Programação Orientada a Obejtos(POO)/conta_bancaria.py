class conta_bancaria:
    def __init__(self, saldo):
        
        self._saldo = 0.0
    
    @property
    def saldo(self):

        return self._saldo    

    @saldo.setter 
    def saldo(self, valor):

        if valor >= 0.0:           
            self._saldo = valor
        else:
            print("Valor Inválido")       

    def mostrar_saldo(self):
        print(self.saldo)    

conta = conta_bancaria(100)         
conta.mostrar_saldo()        

conta.saldo = 250
conta.mostrar_saldo()

conta.saldo = -50   # inválido
conta.mostrar_saldo()