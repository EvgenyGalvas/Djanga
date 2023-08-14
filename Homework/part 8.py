# Задача 1

# def thirteen(list1):
#     s = []
#     for i in list1:
#         if i % 13 == 0 and i > 0:
#             s.append(i)
#     if s:
#         return max(s)
#     else:
#         return "no such numbers"
#
#
# a = [2, 7, 0, 3, 1, 5, -13]
# b = [2, 7, 0, 3, 1, 5, -13, 13]
# c = [26]
# d = [99, 99, 100, 34, -39]
# e = [99, 39, 99, 100, 34]
#
# print(thirteen(a))
# print(thirteen(b))
# print(thirteen(c))
# print(thirteen(d))
# print(thirteen(e))

# Задача 2

# a = ('ab', 'abcd', 'cde', 'abc', 'def')
#
# if input("Введите искомое значение: ") in a:
#     print("YES")
# else:
#     print("NO")

# Задача 3

# a = input("Введите по порядку, без пробелов, элементы кортежа: ")
# tpl = tuple(a)
# print(tpl)
# print("Количество 2 =", tpl.count('2'))
# print("Количество 5 =", tpl.count('5'))
# print("Количество 3 =", tpl.count('3'))
# print("Количество 6 =", tpl.count('6'))
# print("Количество 1 =", tpl.count('1'))
