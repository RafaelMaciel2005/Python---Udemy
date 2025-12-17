import pandas as pd
from IPython.display import display

vendas_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendas_LEFT_JOIN.xlsx")

vendedores_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Vendedores_LEFT_JOIN.xlsx")

verificandoVendas_DF = pd.merge(vendas_DF, vendedores_DF, on=["Id Vendedor"], how="left", suffixes=("Vendas", "Checagem"))

limpandoLinhascomNAN = verificandoVendas_DF.dropna()

del limpandoLinhascomNAN["VendedorChecagem"]

display(limpandoLinhascomNAN)