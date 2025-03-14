# Нулевая матрица N x N

import numpy as np

def create_matrix(N):
    return np.zeros((N, N))

print(create_matrix(2))

# Заполнение матрицы 

import numpy as np

def create_matrix(N, value):
    return np.full((N, N), value)

print(create_matrix(2))