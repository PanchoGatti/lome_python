# Función para crear una matriz de ceros con las mismas dimensiones que la matriz A
def crear_matriz_ceros(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_ceros = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz_ceros

# Ejemplo de matriz A
matriz_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Crear una matriz B de ceros con las mismas dimensiones que la matriz A
matriz_B = crear_matriz_ceros(matriz_A)

print("Matriz A:")
for fila in matriz_A:
    print(fila)

print("\nMatriz B (con todos los elementos en 0):")
for fila in matriz_B:
    print(matriz_B)