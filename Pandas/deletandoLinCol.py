import pandas as opcoesPandas
from IPython.display import display

dataFrameDados = opcoesPandas.read_excel(r"C:\\Users\\Rafael\Documents\\Estudos\\Python-Curso-Udemy\\Arquivos fonte de estudos\\Deletar_Linhas_Colunas.xlsx")

#deletandoLinhasEmBranco = dataFrameDados.dropna()

#del deletandoLinhasEmBranco["Produto"]
#deletarDuasColunas = dataFrameDados.drop(columns=["Produto", "Data Venda"])

#display(deletandoLinhasEmBranco) 
#display(deletarDuasColunas)

excluirLinha3 = dataFrameDados.drop(2, axis=0)
display(excluirLinha3)