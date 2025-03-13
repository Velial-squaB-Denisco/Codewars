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
    if seconds == 0:
        return "now"

    years = seconds // (365 * 24 * 60 * 60)
    seconds %= (365 * 24 * 60 * 60)
    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    parts = []
    if years > 0:
        parts.append(f"{years} year" + ("s" if years > 1 else ""))
    if days > 0:
        parts.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours > 0:
        parts.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        parts.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds > 0:
        parts.append(f"{seconds} second" + ("s" if seconds > 1 else ""))

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return " and ".join(parts)
    else:
        return ", ".join(parts[:-1]) + " and " + parts[-1]

print(format_duration(205851834))