import pandas as pd
from IPython.display import display

loja1_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendedores_Join_Full_Loja1.xlsx")

loja2_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendedores_Join_Full_Loja2.xlsx")

vendasLoja1e2_DF = pd.concat([loja1_DF, loja2_DF])

semClientesDuplicados = vendasLoja1e2_DF.drop_duplicates(subset = "Id Vendedor")

display(semClientesDuplicados)


