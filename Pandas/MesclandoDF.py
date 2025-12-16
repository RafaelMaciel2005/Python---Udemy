import pandas as pd
from IPython.display import display

baseVendas_Jan = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Jan.xlsx")

baseVendas_Fev = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Fev.xlsx")

baseVendas_Mar = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Mar.xlsx")

#display(baseVendas_Jan)
#display(baseVendas_Fev)
#display(baseVendas_Mar)

vendasJanFev = pd.concat([baseVendas_Jan, baseVendas_Fev], ignore_index = True)

display(vendasJanFev)