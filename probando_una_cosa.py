import numpy as np

# Definir la matriz A (cambiar estos valores según tus datos)
A = np.array([[5, 10, 15],
              [20, 25, 30],
              [35, 40, 45]])

# Definir la matriz C con las dimensiones deseadas (nueva fila y columna)
C = np.array([(1, 1), (0, 0), (1, 1), (2, 2)])

# Calcular la cantidad de filas y columnas de la matriz C
nueva_fila = len(C)
nueva_columna = len(C[0])

# Sumar cada columna de la matriz A
sumas_columnas = np.sum(A, axis=0)

# Crear la matriz B con las dimensiones de la matriz C
filas, columnas = nueva_fila, nueva_columna
B = np.zeros((filas, columnas))  # Crear una matriz B con las dimensiones obtenidas de C

for i in range(filas):
    B[i, :] = sumas_columnas[i % len(sumas_columnas)]  # Repetir el valor de la suma de la columna i en la fila i de la matriz B

print("Matriz A:")
print(A)

print("\nMatriz C:")
print(C)

print("\nSumas de cada columna en A:")
print(sumas_columnas)

print("\nMatriz B generada:")
print(B)