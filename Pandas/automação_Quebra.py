import pandas as pd
from IPython.display import display

baseDados_DF = pd.read_excel(r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Jan2.xlsx")

removendoDuplicidades = baseDados_DF.drop_duplicates(subset="Vendedor", keep="first")

for linha in removendoDuplicidades["Vendedor"]:

    vendas_funcionario = baseDados_DF.loc[baseDados_DF["Vendedor"]== linha]

    vendas_funcionario.to_csv("Relatório Vendas" + linha + ".csv")

print("Relatório separado com sucesso")    