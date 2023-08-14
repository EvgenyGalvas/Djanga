# Задача 1

import random
number = random.randint(1, 100)
#print(number)

counter = 0

while True:
    try:
        attempt = int(input("Введите число от 1 до 100: "))
    except ValueError:
        print("\nВы ввели некорректное значение. Повторите попытку\n")
        continue
    if attempt > number:
        print("Загаданное число меьше")
        counter += 1
    elif 0 < attempt < number:
        print("Загаданное число больше")
        counter += 1
    elif attempt == 0:
        print("Игра окончена.")
        break
    elif attempt == number:
        counter += 1
        print("Вы угадали загаданное число с " + str(counter) + " раза")
        break
    else:
        print("\nВы ввели некорректное значение. Повторите попытку\n")

        continue


# Задача 2

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка:\nn = ")))]
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")



# Задача 3

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
#
# for i in range(len(a)):
#     counter = 0
#     for j in range(len(a)):
#         if a[i] == a[j]:
#             counter +=1
#     if counter == 1:
#         print(a[i], end=" ")

# Задача 4

# n = 8
# for i in range(n + 1):
#     print("*" * (n - i))