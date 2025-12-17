import pandas as pd
from IPython.display import display

baseLanchonete_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Lanchonete_Pivot_Table.xlsx")

pivotExemplo1 = baseLanchonete_DF.pivot(index="Data Venda", columns="Cliente", values="Preço")

display(pivotExemplo1)