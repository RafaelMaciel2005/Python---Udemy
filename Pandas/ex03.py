import pandas as opcoesPandas
import numpy as opcoesNumpy

numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(15,10)*100)
print(numerosAleatorios)