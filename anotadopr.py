Xij = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]
matrices_iteradas = matriz_iterada(Xij)
matriz_transpuesta = list(map(list, zip(*Aij)))

A = np.array(Xij)
B = np.array(matriz_transpuesta)
C = np.array(TSj)
primer_termino_menor=9999999999999999999999999999999999999999999999999999999
caso_optimo=A

for matrix in matrices_iteradas:
    A = np.array(matrix)
    productos = productoEscalar2Matrices(A,B)
    resultado_final = sum(productos)
    vector_resultante = np.array(productos)
    resultado_multiplicacion = np.dot(vector_resultante, C)
    multiplicacion = resultado_multiplicacion*INVTSj
    primer_termino_actual = multiplicacion[0]
    if (primer_termino_actual < primer_termino_menor):
        primer_termino_menor = primer_termino_actual
        caso_optimo = A
print('Caso optimo array: ', caso_optimo)