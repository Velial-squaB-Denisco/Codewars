"""Создайте две функции для кодирования и декодирования строки с помощью шифра «Рельсы». 
Этот шифр используется для кодирования строки путём последовательного размещения 
каждого символа по диагонали вдоль набора «рельсов». Сначала начните двигаться по диагонали вниз. 
Когда вы дойдёте до конца, измените направление и двигайтесь по диагонали вверх, 
пока не достигнете верхнего «рельса». Продолжайте, пока не дойдёте до конца строки. 
Затем каждая «рельса» считывается слева направо для получения закодированной строки.

Например, строка "WEAREDISCOVEREDFLEEATONCE" может быть представлена в трёхпроводной системе 
следующим образом:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
Закодированная строка будет иметь вид:

WECRLTEERDSOEEFEAOCAIVDEN
Напишите функцию/метод, который принимает 2 аргумента: строку и количество рельсов и возвращает 
ЗАКОДИРОВАННУЮ строку.

Напишите вторую функцию/метод, которая принимает два аргумента: 
закодированную строку и количество рельсов и возвращает раскодированную строку.

При кодировании и декодировании предполагается, что количество рельсов >= 2 
и что при передаче пустой строки возвращается пустая строка.

Обратите внимание, что в приведенном выше примере для простоты опущены знаки препинания и пробелы. 
Однако существуют тесты, в которых знаки препинания учитываются. Не отфильтровывайте знаки препинания, 
так как они являются частью строки.
"""
import numpy as np

def encode_rail_fence_cipher(string, n):

    string = list(string)
    matrix = np.empty((n, len(string)), dtype=str)

    for i in range(len(matrix)):
        for j in range(n):
            matrix[i][j] = string[i]
    print(matrix)
    
def decode_rail_fence_cipher(string, n):
    pass

print(encode_rail_fence_cipher("hello", 3))

for i
    j++