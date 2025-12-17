import pandas as pd
from IPython.display import display

#https://docs.google.com/spreadsheets/d/1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD/edit?usp=sharing&ouid=103286032416998039927&rtpof=true&sd=true

planilha_id = '1uxYa8NKhoPQVAO_LNqNWxyn30qn5S_qD'

dados_DF = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{planilha_id}/export?format=csv")

"""
1 - Após carregar os dados, deixe somente as colunas de Vendedor e Total de Vendas
"""
deletarDuasCOL = dados_DF.drop(columns = ["Produto", "Data Venda"])

"""
2 - Com o groupby, use a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas
"""

deletarDuasCOL["Total Vendas"] = deletarDuasCOL["Total Vendas"].str.replace(",", ".")

deletarDuasCOL["Total Vendas"] = deletarDuasCOL["Total Vendas"].astype(float)

agrupaCol_Resumo = deletarDuasCOL.groupby(["Vendedor"]).sum(numeric_only = True)

#display(agrupaCol_Resumo)

"""
3 - Salve o dataFrame como um arquivo de Excel
"""
agrupaCol_Resumo.to_csv("Resposta Desafio.csv")

agrupaCol_Resumo = pd.ExcelWriter("Resposta Desafio.xlsx", engine = "xlsxwriter")
