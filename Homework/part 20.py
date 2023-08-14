

# Задача 1

# file = 'text.txt'
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
#
# with open(file, 'w') as my_file:
#     my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
#
# with open(file, 'r') as my_file:
#     lst = my_file.readlines()
#     lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
#     print(''.join(lst))
#
# with open(file, 'w') as my_file:
#     my_file.writelines(lst)


# Задача 2

# file = 'text.txt'
#
# with open(file, 'w') as my_file:
#     my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
#
# with open(file, 'r') as my_file:
#     lst = my_file.readlines()[::-1]
#     print(''.join(lst))
#
# with open(file, 'w') as my_file:
#     my_file.writelines(lst)

# Задача 3

# file1 = 'text1.txt'
# file2 = 'text2.txt'
# file3 = 'text3.txt'
#
# with open(file1, 'w') as f1, open(file2, 'w') as f2:
#     f1.write('Первый файл.')
#     f2.write('Второй файл.')
#
# with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'w') as f3:
#     f3.write(f'Третий файл = {f1.read()}{f2.read()}')
