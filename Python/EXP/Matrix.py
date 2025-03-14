# Нулевая матрица N x N

import numpy as np

def create_matrix(N):
    matrix = np.zeros((N, N))
    return matrix

print(create_matrix(2))
