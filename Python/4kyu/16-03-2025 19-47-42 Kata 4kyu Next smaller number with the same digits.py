"""Напишите функцию, которая принимает положительное целое число и возвращает следующее 
меньшее положительное целое число, состоящее из тех же цифр.

Например:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Верните -1 (для Haskell: верните Nothing, для Rust: верните None), 
если не существует меньшего числа, состоящего из тех же цифр. Также верните -1, 
если следующее меньшее число с теми же цифрами требует, чтобы первая цифра была равна нулю.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
некоторые тесты будут включать очень большие числа.
в тестовых данных используются только положительные целые числа."""
from itertools import permutations

def next_smaller(n):
    n = str(n)
    m = list(n)
    result = []

    res = list(permutations(m))
    
    for i in range(len(res)):
        if int(res[i][0]) == 0:
            continue
        result.append("".join(res[i]))

    print("\n","END", result)

print(next_smaller(2071))