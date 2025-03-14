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
    matrix = np.empty((N, N), dtype=int) # Стандартно dtupe = float
    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(value)

    return matrix

print("Заполнение матрицы III","\n", create_matrix(2, 4))

# Заполнение матрицы IV

import random
import numpy as np

def create_matrix(N):

    # Генерация случайного целого числа в диапазоне от 1 до 10
    value = random.randint(1, 10)
    matrix = np.empty((N, N), dtype=int) # Стандартно dtupe = float
    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(value)

    return matrix

print("Заполнение матрицы IV","\n", create_matrix(2))

# Генерация случайного числа с плавающей запятой в диапазоне от 0 до 1
random_float = random.random()
print(random_float)