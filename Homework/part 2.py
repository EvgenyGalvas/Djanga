# n = int(input("Введите число от 1 до 99: "))
# if 1 <= n <= 99:
#     if n == 1 or n == 21 or n == 31 or n == 41 or n == 51 or n == 61 or n == 71 or n == 81 or n == 91:
#         print(n, "копейка")
#     elif 2 <= n <= 4 or 22 <= n <= 24 or 32 <= n <= 34 or 42 <= n <= 44 or 52 <= n <= 54 or 62 <= n <= 64 or \
#             72 <= n <= 74 or 82 <= n <= 84 or 92 <= n <= 94:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("Неверный диапазон ввода.")

n = int(input("Введите число от 1 до 99: "))
if 1 <= n <= 99:
    if n % 10 == 1:
        print(n, "копейка")
    elif 2 <= (n % 10) <= 4:
        print(n, "копейки")
    else:
        print(n, "копеек")
else:
    print("Неверный диапазон ввода.")