import pandas as pd
from IPython.display import display

vendas_DataFrame = pd.read_excel(r"C:\Users\Rafael\Downloads\Vendas_Jan.xlsx")

#display(vendas_DataFrame)

#display(vendas_DataFrame.index)

#display(vendas_DataFrame.columns)

#display(vendas_DataFrame.head)

display(vendas_DataFrame[["Vendedor", "Total Vendas"]])