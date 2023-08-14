
from math import pi, sqrt
from random import randrange, randint
# Задача 1

print("Вычисление площади фигур\n")
while True:
    print("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - окружность")
    try:
        type_figure = int(input(": "))
    except ValueError:
        print("Вы ввели некорректное значение!")
        choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
        if choose == "Y":
            continue
        else:
            break

    if type_figure == 1:
        try:
            a = int(input("Введите сторону а = "))
            b = int(input("Введите сторону b = "))
            c = int(input("Введите сторону c = "))
        except ValueError:
            print("Вы ввели некорректное значение!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break
        if a > 0 and b > 0 and c > 0:
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = sqrt(p * (p - a) * (p - b) * (p - c))
                print(round(s, 2))
                break
            else:
                print("Такой треугольник не существует!")
                choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
                if choose == "Y":
                    continue
                else:
                    break
        else:
            print("Такой треугольник не существует!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break

    elif type_figure == 2:
        try:
            a = int(input("Введите сторону а = "))
            b = int(input("Введите сторону b = "))
        except ValueError:
            print("Вы ввели некорректное значение!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break
        if a > 0 and b > 0:
            s = a * b
        else:
            print("Такой прямоугольник не существует!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break
        print(round(s))
        break

    elif type_figure == 3:
        try:
            r = int(input("Введите радиус окружности r = "))
        except ValueError:
            print("Вы ввели некорректное значение!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break
        if r > 0:
            s = pi * r ** 2
        else:
            print("Такая окружность не существует!")
            choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
            if choose == "Y":
                continue
            else:
                break
        print(round(s, 2))
        break
    else:
        print("Вы ввели некорректное значение!")
        choose = input("Хотите продолжить (Y) или выйти из программы (Нажмите любую клавишу): ")
        if choose == "Y":
            continue
        else:
            break

# Задача 2

# k = 3
# x = 4
#
# matrix = [[x + k * 4 for x in range(1, x + 1)] for k in range(k)]
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()
#
# print()
#
# s = [[matrix[j][i] for j in range(k)] for i in range(x)]
# for i in s:
#     for j in i:
#         print(j, end="\t")
#     print()

# Задача 3

# n = 6
# matrix = [[randrange(11) for _ in range(n)] for _ in range(n)]
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()
#
# print()
#
# matrix2 = [randrange(11) for _ in range(n)]
# print(matrix2)
#
# for i in range(len(matrix)):
#     if i % 2 == 0:
#         matrix[i] = matrix2
# print()
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()


# Задача 4

# n = 6
# matrix = [[randrange(11) for _ in range(n)] for _ in range(n)]
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()
#
# print()
#
# for i in range(len(matrix)):
#     if i % 2 == 0:
#         matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
# print()
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print()

# Задача 5 Вариант вывода матрицы в одну строку

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# print(matrix)
# [print(('\t'.join([str(x) for x in row])), end="\n") for row in matrix]