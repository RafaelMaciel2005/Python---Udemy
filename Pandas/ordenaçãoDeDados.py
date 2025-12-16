import pandas as pd
from IPython.display import display

baseVendas_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Ordenação.xlsx")

ordenarVendedor = baseVendas_DF.sort_values(by="Vendedor")

display(ordenarVendedor)

ordenarProduto = baseVendas_DF.sort_values(by="Produto")
display(ordenarProduto) 

ordenarDuasColunas = baseVendas_DF.sort_values(by = ["Vendedor", "Produto"])
display(ordenarDuasColunas)

ordenarZaA = baseVendas_DF.sort_values(by="Vendedor", ascending=False)
display(ordenarZaA)