"""Ваша задача — написать функцию, которая форматирует продолжительность, заданную в секундах, 
в удобном для восприятия человеком виде.

Функция должна принимать неотрицательное целое число. Если оно равно нулю, функция просто возвращает "now". 
В противном случае продолжительность выражается комбинацией years, days, hours, minutes и seconds.

Это гораздо легче понять на примере:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"""

def format_duration(seconds):
    res = ""
    s = seconds
    m = 0
    h = 0 
    d = 0
    y = 0
    
    while (s > 59):

        m += 1
        s = s - 60
        if m > 59:
            while (m > 59):
                h += 1
                


    print(res , seconds)
    return res

print(format_duration(3600))