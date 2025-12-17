import pandas as pd
from IPython.display import display

Loja1_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Outer_Vendas_Loja1.xlsx")

Loja2_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Outer_Vendas_Loja2.xlsx")

verificandoVendas_DF = pd.merge(Loja1_DF, Loja2_DF, on=["Id Vendedor"], how="outer", suffixes=("Loja1", "Loja2"))

display(verificandoVendas_DF)