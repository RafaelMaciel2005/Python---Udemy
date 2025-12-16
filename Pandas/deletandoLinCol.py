import pandas as opcoesPandas
from IPython.display import display

dataFrameDados = opcoesPandas.read_excel(r"C:\\Users\\Rafael\Documents\\Estudos\\Python-Curso-Udemy\\Arquivos fonte de estudos\\Deletar_Linhas_Colunas.xlsx")

deletandoLinhasEmBranco = dataFrameDados.dropna()

display(deletandoLinhasEmBranco) 