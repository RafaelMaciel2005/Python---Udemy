class Animal:

    def fazer_som(self):
        print("O animal faz um som")

class Cachorro(Animal):
   
    def fazer_som(self):
        print("O cachorro faz woof-woof")    

    def latir(self):
        print("Woof-Woof")
        
class Gato(Animal):

    def fazer_som(self):
        print("O gato faz miaau-miaau")   

    def miar(self):
        print("Miaau-Miaau")     

animal = Animal()
animal.fazer_som()

cachorro = Cachorro()

cachorro.fazer_som()
cachorro.latir()

gato = Gato()
gato.fazer_som()
gato.miar()