import pandas as pd
from IPython.display import display

loja1_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendas_+INNER_JOIN_Loja1.xlsx")

loja2_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendas_+INNER_JOIN_Loja2.xlsx")

vendedoresAmbasLojas_DF = pd.merge(loja1_DF, loja2_DF, on = ["Vendedor"], how = "Inner")

display(loja1_DF)