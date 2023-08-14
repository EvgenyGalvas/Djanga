# Вариант 1

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.info = self.Info()
#
#     def print_information(self):
#         print(self.name, self.info.info)
#
#     class Info:
#         def __init__(self):
#             self.info = '=> HP, i7, 16'
#
#
# lst = [Student("Roman"), Student("Vladimir")]
# for q in lst:
#     q.print_information()


# Вариант 2

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     class Info:
#         def __init__(self, obj):
#             self.info = '=> HP, i7, 16'
#             self.obj = obj
#
#         def print_information(self):
#             print(self.obj.name, self.info)
#
#
# lst = [Student("Roman"), Student("Vladimir")]
# for q in lst:
#     q.Info(q).print_information()

