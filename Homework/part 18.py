
# Задача 1

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# names1 = names.copy()
# ind = -1
# while ind != 0:
#     ind = 0
#     temp_list = []
#     for i in names1:
#         if isinstance(i, list):
#             temp_list.extend(i)
#             ind += 1
#         else:
#             temp_list.append(i)
#     names1 = temp_list
# print(names)
# print(names1)
# print(len(names1))

# Задача 2

# def negative(lst):
#     flag = 0
#     if not lst:
#         return flag
#     if lst[0] < 0:
#         flag = 1
#     return flag + negative(lst[1:])
#
#
# num = [-2, 3, 8, -11, -4, 6]
# print('n =', negative(num))
