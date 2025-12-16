import pandas as pd
from IPython.display import display

dataFrameDados = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\\Tratamento_Dados.xlsx")

#dataFrameDados["Total Vendas"] = dataFrameDados["Total Vendas"].fillna(dataFrameDados["Total Vendas"].mean())
#display(dataFrameDados)

#dataFrameDados["Total Vendas"] = dataFrameDados["Total Vendas"].fillna(5)
#display(dataFrameDados)

dataFrameDados["Total Vendas"] = dataFrameDados["Total Vendas"].ffill()
display(dataFrameDados)