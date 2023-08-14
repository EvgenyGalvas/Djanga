# Вариант 1

# s = 0
#
#
# def square(k, l, m):
#     def sq(x, y):
#         return x * y
#
#     global s
#     s = 2 * (sq(k, l) + sq(k, m) + sq(l, m))
#
#
# square(2, 4, 6)


# print(s)
# square(5, 8, 2)
# print(s)
# square(1, 6, 8)
# print(s)

# Вариант 2

# def square(k, l, m):
#     def sq(x, y):
#         return x * y
#
#     s = 2 * (sq(k, l) + sq(k, m) + sq(l, m))
#
#     return s
#
#
# print(square(2, 4, 6))
# print(square(5, 8, 2))
# print(square(1, 6, 8))

# Вариант 3

# def square(k, l, m):
#     s = 0
#
#     def sq():
#         nonlocal s
#         s = 2 * (k * l + l * m + k * m)
#
#     sq()
#     return s
#
#
# print(square(2, 4, 6))
# print(square(5, 8, 2))
# print(square(1, 6, 8))
