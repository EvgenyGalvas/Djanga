# Задача 1

# from math import pi
# print("Площадь окружности радиуса 2:", (lambda r: pi * r ** 2)(2))
# print("Площадь прямоугольника размером 10*13:", (lambda a, b: a * b)(10, 13))
# print("Площадь трапеции для а=7, b=5, h=3:", (lambda a, b, h: (a + b) * h * 0.5)(7, 5, 3))

# Задача 2

# print((lambda a, b, c: a * b * c)(2, 5, 5))

# Задача 3

# students = [
#     {'name': 'Jannifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# res = sorted(students, key=lambda i: i['name'])
# print(res)
# res2 = sorted(students, key=lambda i: i['final'], reverse=True)
# print(res2)

# Задача 4

# students = [
#     {'name': 'Jannifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# print(sorted(students, key=lambda i: i['final'])[-1])
# print(sorted(students, key=lambda i: i['final'])[0])


# Задача 5

from math import pow

# a = [3, 6, 8, 9, 1, 2]
# print(list(map(lambda x, y: x * y, a, [round(pow(i, 3)) for i in range(len(a))])))

# Задача 6

# from math import pow
#
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(list(map(lambda i: int(pow(i, 2)), nums)))
# print(list(map(lambda i: int(pow(i, 3)), nums)))
