import re


def number(num):
    return re.findall(r'^\+?7\s?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{2}[ -]?\d{2}$', num)


print(number('+7 499 456-45-78'))
print(number('+74994564578'))
print(number('7 (499) 456 45 78'))
print(number('7 (499) 456-45-78'))