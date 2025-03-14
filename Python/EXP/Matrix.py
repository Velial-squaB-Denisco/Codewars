# Нулевая матрица N x N

import numpy as np

def create_matrix(N):
    return np.zeros((N, N))

print("Нулевая матрица N x N","\n",create_matrix(2))

# Заполнение матрицы I

import numpy as np

def create_matrix(N, value):
    return np.full((N, N), value)

print("Заполнение матрицы I","\n",create_matrix(2, 4))

# Заполнение матрицы II

import numpy as np

def create_matrix(N, value):
    return np.arange(value).reshape(N, N)

print("Заполнение матрицы II","\n",create_matrix(2, 4))

# Заполнение матрицы III

import numpy as np

def create_matrix(N, value):
    matrix = np.empty((N, N))
    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(value)

    return matrix

print("Заполнение матрицы III","\n", create_matrix(2, 4))