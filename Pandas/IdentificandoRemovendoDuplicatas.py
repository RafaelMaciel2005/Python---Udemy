import pandas as pd
from IPython.display import display

baseVendas_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Base_Vendas.xlsx")

resumoValoresUnicos = baseVendas_DF.nunique

#confereDuplicidades= baseVendas_DF.duplicated(subset = "Vendedor", keep="first")

#baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset = "Vendedor", keep="first")

#baseVendas_DF["Confere Duplicidade"] = baseVendas_DF.duplicated(subset = "Vendedor", keep="last")

removerDuplicidade = baseVendas_DF.drop_duplicates(subset="Vendedor", keep="first")

print(removerDuplicidade)