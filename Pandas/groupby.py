import pandas as pd
from IPython.display import display

vendas_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Groupby.xlsx")

#mediaVendedor = vendas_DF.groupby(["Vendedor"]).mean(numeric_only=True)
#display(mediaVendedor)

#somaVendedor = vendas_DF.groupby(["Vendedor"]).sum(numeric_only=True)
#display(somaVendedor)

agrupaDuasColunas = vendas_DF.groupby(["Produto", "Vendedor"]).sum(numeric_only=True)
display(agrupaDuasColunas)

