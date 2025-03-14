# Нулевая матрица N x N

import numpy as np

def create_matrix(N):
    return np.zeros((N, N))

print(create_matrix(2))

# Заполнение матрицы I

import numpy as np

def create_matrix(N, value):
    return np.full((N, N), value)

print(create_matrix(2, 4))

# Заполнение матрицы II

import numpy as np

def create_matrix(N, value):
    return np.arange(value).reshape(N, N)

print(create_matrix(2, 4))

# Заполнение матрицы III

import numpy as np

def create_matrix(N, value):
    matrix = np.empty((N, N))
    return matrix

print(create_matrix(2, 4))