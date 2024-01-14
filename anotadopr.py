import numpy as np

# Matriz de ejemplo
matriz = np.array([
    [12, 0, 1, 0],
    [4, 0, 0, 0],
    [7, 1, 0, 1],
    [0, 0, 0, 0]
])

# Suma de cada columna
sumas_columnas = np.sum(matriz, axis=0)

# Calcular el promedio de las sumas excluyendo los valores iguales a cero
valores_no_cero = sumas_columnas[sumas_columnas != 0]
promedio_no_cero = np.mean(valores_no_cero)

print("Sumas por columna:", sumas_columnas)
print("Promedio de sumas excluyendo ceros:", promedio_no_cero)