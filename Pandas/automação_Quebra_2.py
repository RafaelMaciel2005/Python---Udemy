import pandas as pd
from IPython.display import display

baseDados_DF = pd.read_excel(
    r"C:\Users\Rafael\Documents\Estudos\Python-Curso-Udemy\Arquivos fonte de estudos\Vendas_Jan2.xlsx"
)

removendoDuplicidades = baseDados_DF.drop_duplicates(
    subset="Vendedor", keep="first"
)

for vendedor in removendoDuplicidades["Vendedor"]:

    vendas_funcionario = baseDados_DF.loc[
        baseDados_DF["Vendedor"] == vendedor
    ]

    nome_arquivo = f"Relatorio_Vendas_{vendedor}.xlsx"

    with pd.ExcelWriter(nome_arquivo, engine="xlsxwriter") as writer:
        vendas_funcionario.to_excel(
            writer,
            sheet_name="Dados",
            index=False
        )

print("Relatório separado com sucesso")