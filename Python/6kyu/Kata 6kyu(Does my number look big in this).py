"""Нарциссическое число (или число Армстронга) — это положительное число, которое является суммой своих собственных цифр,
   каждая из которых возведена в степень, равную количеству цифр в заданном основании.
   В этой ката мы ограничимся десятичной системой (основание 10).

Например, возьмём число 153 (три цифры), которое является самовлюблённым:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
и 1652 (4 цифры), чего нет:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938"""


def narcissistic(value):

    new_value = str(value)
    degree = len(new_value)

    j = 0
    for i in new_value:
        j += int(i) ** degree
    
    if value == j:
        print(f"{value} is narcissistic")
        return True
    else:
        print(f"{value} is not narcissistic")
        return False

print(narcissistic(7))