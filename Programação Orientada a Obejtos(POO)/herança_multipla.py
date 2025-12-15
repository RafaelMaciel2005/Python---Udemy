class Musico:

    def tocar_instrumento(self):

        print("Tocando instrumento")

class Atleta:

    def correr(self):

        print("Correndo na pista")

class MusicoAtleta(Musico, Atleta):

    def exibir_habilidades(self): 
        print("Tocando instrumento e correndo na pista") 

musico = Musico()
musico.tocar_instrumento()              

atleta = Atleta()
atleta.correr()    

m_atleta = MusicoAtleta()
m_atleta.exibir_habilidades()
    