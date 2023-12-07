import numpy as np

# Matriz A proporcionada
A = np.array([
    [21.80357143, 23.57142857, 24.16071429, 25.33928571],
    [15.44419643, 15.44419643, 15.86160714, 17.53125],
    [29.85714286, 29.07142857, 29.07142857, 32.21428571],
    [35.0625, 32.55803571, 30.88839286, 30.88839286]
])

# Redondear los valores de la matriz A hacia arriba al número entero más cercano
A_redondeada = np.ceil(A)

# Mostrar la matriz redondeada
print(A_redondeada)





import numpy as np

# Matriz A proporcionada
A = np.array([
    [21.80357143, 23.57142857, 24.16071429, 25.33928571],
    [15.44419643, 15.44419643, 15.86160714, 17.53125],
    [29.85714286, 29.07142857, 29.07142857, 32.21428571],
    [35.0625, 32.55803571, 30.88839286, 30.88839286]
])

# Redondear los valores de la matriz A hacia abajo al número entero más cercano
A_redondeada_abajo = np.floor(A)

# Mostrar la matriz redondeada hacia abajo
print(A_redondeada_abajo)