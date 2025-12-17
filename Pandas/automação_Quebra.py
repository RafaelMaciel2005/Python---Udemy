import pandas as pd
from IPython.display import display

baseDados_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Jan2.xlsx")

removendoDuplicidades = baseDados_DF.drop_duplicates(subset="Vendedor", keep="first")

display(baseDados_DF)