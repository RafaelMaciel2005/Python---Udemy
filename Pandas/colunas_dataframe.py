import pandas as opcoesPanda
from IPython.display import display

notasAluno_DataFrame = opcoesPanda.DataFrame({

    "Nome": ["Ana", "Pedro", "João"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

notasAluno_DataFrame.loc[1, "Nota 2"] = 50

notasAluno_DataFrame["Média"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4

novaColunaFaltas = [2, 5, 3]

notasAluno_DataFrame["Faltas"] = novaColunaFaltas


display(notasAluno_DataFrame)
