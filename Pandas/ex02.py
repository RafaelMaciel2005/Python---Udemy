import pandas as opcoesPandas
import numpy as opcoesNumpy

dataFrame_Meses = opcoesPandas.date_range("2025/12/31", periods=12, freq="M")
print(dataFrame_Meses)