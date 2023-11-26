import pandas as pd
import os
import sys
import numpy as np

# Itera a través de las hojas del diccionario y muestra todos los registros de cada hoja
def datos_loc_ets (datos):
            
    rows = datos['Distancia Loc - ETs'].tolist()
    cols = datos.columns[1:].tolist()
    result_matrix = np.zeros((len(rows), len(cols)), dtype=int)

    for i, row_label in enumerate(rows):
        for j, col_label in enumerate(cols):
            result_matrix[i, j] = datos.at[i, col_label]
    return(result_matrix)