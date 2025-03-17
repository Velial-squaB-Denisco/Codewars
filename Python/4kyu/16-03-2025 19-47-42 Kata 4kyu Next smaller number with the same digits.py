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

    result.sort()

    for i in range(len(result)):
        try:
            if result[i + 1] == n:
                return int(result[i])
        except:
            return -1

print(next_smaller(100))

#////////////////////////////////////////////////

def next_smaller(n):
    digits = list(str(n))
    i = len(digits) - 2
    # Ищем точку i, где digits[i] > digits[i+1]
    while i >= 0 and digits[i] <= digits[i+1]:
        i -= 1
    if i == -1:
        return -1  # Невозможно сделать меньше
    
    # Ищем j, наибольший индекс справа от i, где digits[j] < digits[i]
    j = len(digits) - 1
    while digits[j] >= digits[i]:
        j -= 1
    
    # Меняем местами i и j
    digits[i], digits[j] = digits[j], digits[i]
    
    # Переворачиваем оставшуюся часть после i
    digits[i+1:] = reversed(digits[i+1:])
    
    # Проверяем на ведущий ноль
    if digits[0] == '0':
        return -1
    
    # Преобразуем обратно в число
    next_num = int(''.join(digits))
    
    return next_num if next_num < n else -1

print(next_smaller(100))