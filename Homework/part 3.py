# Задача 1

while True:
    try:
        number = int(input("Количество символов: "))
        if number > 0:
            break
        else:
            print("\nВы не ввели целое положительное число!\n")
            continue
    except ValueError:
        print("\nВы не ввели целое положительное число!\n")
        continue
type_symbol =input("Тип символа: ")
print("0 - горизонтальная\n1 - вертикальная")
while True:
    try:
        orient = int(input("ориентация линии: "))
        if orient == 0 or orient == 1:
            break
        else:
            print("\nНеверное направление\n")
            continue
    except ValueError:
        print("\nНеверное направление\n")
        continue


while number > 0:
    if orient == 0:
        print(type_symbol, end=" ")
    else:
        print(type_symbol)
    number -= 1



# Задача 2

# i = 5
# while i > 0:
#     if i % 2 != 0:
#         print("+" * 16)
#     else:
#         print("-" * 16)
#     i -= 1

# Задача 3

# while True:
#     try:
#         a = int(input("Введите первое число: "))
#         b = int(input("Введите второе число: "))
#         c = int(input("Введите третье число: "))
#         break
#     except ValueError:
#         print("\nНеверный тип данных! Введите целое число!")
#         continue
#
# bigest_number = a if a >= b and a >= c else b if b >= a and b >= c else c
#
# print("Максимальное значение: ", bigest_number)

# Задача 4

# print('Выберите операцию:\
#       \n1 - "r" - применяет унарный минус к операнду\
#       \n2 - "+" - сложение\
#       \n3 - "-" - вычитание\
#       \n4 - "/" - деление\
#       \n5 - "*" - умножение\
#       \n6 - "%" - деление по модулю (остаток от деления)\
#       \n7 - "<" - минимальное из двух чисел\
#       \n8 - ">" - максимальное из двух чисел')
#
# while True:
#     try:
#         act = int(input("Введите цифру от 1 до 8: "))
#     except ValueError:
#         print("\nНекорректно введены данные!\n")
#         continue
#     if 1 <= act <= 8:
#         try:
#             number1 = int(input("Введите первое число: "))
#             number2 = int(input("Введите второе число: "))
#             break
#         except ValueError:
#             print("\nНекорректно введены данные!\n")
#             continue
#     else:
#         print("\nНекорректно введены данные!\n")
#         continue
#
#
# if number2 == 0 and (act == 4 or act == 6):
#     print("На 0 делить нельзя!")
# elif act == 1:
#     print(-number1)
#     print(-number2)
# elif act == 2:
#     print(number1 + number2)
# elif act == 3:
#     print(number1 - number2)
# elif act == 4:
#     print(number1 / number2)
# elif act == 5:
#     print(number1 * number2)
# elif act == 6:
#     print(number1 % number2)
# elif act == 7:
#     if number1 > number2:
#         print(number2)
#     else:
#         print(number1)
# elif act == 8:
#     if number1 > number2:
#         print(number1)
#     else:
#         print(number2)

# Задача 5

# size = int(input("Введите размер поля: "))
# num = int(input("Введите количество символов: "))
# a = 1
# while a <= size:
#     if a % 2 != 0:
#         i = 1
#         while i <= num:
#             j = 1
#             while j <= size:
#                 if j % 2 != 0:
#                     print("* " * num, end="")
#                 else:
#                     print("  " * num, end="")
#                 j += 1
#             print()
#             i += 1
#     else:
#         i = 1
#         while i <= num:
#             j = 1
#             while j <= size:
#                 if j % 2 != 0:
#                     print("  " * num, end="")
#                 else:
#                     print("* " * num, end="")
#                 j += 1
#             print()
#             i += 1
#     a += 1





