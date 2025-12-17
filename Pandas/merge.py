import pandas as pd
from IPython.display import display

vendas_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendas_Merge.xlsx")

produtos_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Produtos_Merge.xlsx")

vendedores_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendedores_Merge.xlsx")

vendas_DF = vendas_DF.merge(vendedores_DF)

display(vendas_DF)