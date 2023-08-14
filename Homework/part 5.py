import random

# Задача 1

list1 = [random.randint(0, 100) for i in range(10)]
print(list1)
Max = max(list1)
print("Max:", Max)
del list1[list1.index(Max)]
list1.insert(0, Max)
print(list1)

# Задача 2

# list2 = [random.randint(-20, 20) for i in range(10)]
# print(list2)
# list2.sort(reverse = True)
# print(list2)

# Задача 3

# list3 = [random.randint(0, 100) for i in range(10)]
# print(list3)
# Min = min(list3)
# print("Min:", Min)
# Index = list3.index(Min)
# print("Index Min:",Index)
# print(list3[Index:])
