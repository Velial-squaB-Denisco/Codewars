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
    s = int(seconds)
    m = 0
    h = 0 
    d = 0
    y = 0
    ss = ""
    ms = ""
    hs = ""
    ds = ""
    ys = ""

    print(s, s, s)
    
    while (s > 59):
        m += 1
        s -= 60
        if m > 59:
            while (m > 59):
                h += 1
                m -= 60 
                if h > 59:
                    while (h > 59):
                        d += 1
                        h -= 60
                        if d > 59:
                            while (d > 59):
                                y += 1
                                d -= 60 

    if s == 0:
        res = "now"

    if s == 1:
        ss = f"{s} second"
    
    if 1 > s > 59:
        ss = f"{s} seconds"
    
    if m == 1:
        ms = f"{m} minute"
    
    if 1 > m > 59:
        ms = f"{m} minutes"
    
    if h == 1:
        hs = f"{h} hours"
    
    if 1 > h > 59:
        hs = f"{h} hours"

    if d == 1:
        ds = f"{d} day"
    
    if 1 > h > 59:
        hs = f"{h} days"

    if y == 1:
        ys = f"{y} year"
    
    if 1 > y > 59:
        ys = f"{y} years"

    print(res, s, m, h, d, y)
    return res

print(format_duration(3600))