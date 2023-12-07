import numpy as np

# Definir la matriz A
A = np.array([[120, 0, 0, 0],
              [0, 85, 0, 0],
              [160, 0, 0, 0],
              [0, 170, 0, 0]])

# Obtener el número de columnas en la matriz A
num_columnas = A.shape[1]

# Calcular las sumas de cada columna
sumas_columnas = np.sum(A, axis=0)

print("Las sumas de cada columna son:")
print(sumas_columnas)

# Crear una nueva matriz con las sumas de las columnas
nueva_matriz = np.array(sumas_columnas)

print("\nLa nueva matriz creada con las sumas de las columnas es:")
print(nueva_matriz)