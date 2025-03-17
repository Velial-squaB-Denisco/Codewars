"""Создайте функцию, которая принимает положительное целое число и возвращает следующее большее число, 
которое можно получить, переставив его цифры. Например:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
Если цифры нельзя переставить так, чтобы получилось большее число, 
верните -1 (или nil в Swift, None в Rust):

  9 ==> -1
111 ==> -1
531 ==> -1"""

def next_bigger(n):
    digits = list(str(n))
    i = len(digits) - 2
    # Ищем точку i, где digits[i] < digits[i+1]
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    if i == -1:
        return -1  # Невозможно сделать больше

    # Ищем j, наибольший индекс справа от i, где digits[j] > digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Меняем местами i и j
    digits[i], digits[j] = digits[j], digits[i]

    # Переворачиваем оставшуюся часть после i
    digits[i+1:] = reversed(digits[i+1:])

    # Преобразуем обратно в число
    next_num = int(''.join(digits))

    return next_num

print(next_bigger(12))