# Вариант 1

# class Point3D:
#     def __init__(self, x, y, z):
#         if not Point3D.__check_value(x) and not Point3D.__check_value(y) and not Point3D.__check_value(z):
#             raise ValueError('Координата должна быть числом не равным нулю')
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, (int, float)) and z != 0:
#             return True
#         return False
#
#     def __str__(self):
#         return f'{self.x}, {self.y}, {self.z}'
#
#     def __getitem__(self, item):
#         if item == 'x':
#             return self.x
#         if item == 'y':
#             return self.y
#         if item == 'z':
#             return self.z
#
#     def __add__(self, other):
#         return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
#
#     def __truediv__(self, other):
#         return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)
#
#     def __eq__(self, other):
#         if self.x == other.x and self.y == other.y and self.z == other.z:
#             return True
#         return False
#
#     def __setitem__(self, key, value):
#         if not Point3D.__check_value(value):
#             raise ValueError("Координата должна быть числом не равным нулю")
#         if key == 'x':
#             self.x = value
#         if key == 'y':
#             self.y = value
#         if key == 'z':
#             self.z = value
#
#
# p1 = Point3D(12, 15, 18)
# p2 = Point3D(6, 3, 9)
#
# print(f"Kоординаты 1-й точки: {p1}")
# print(f"Kоординаты 2-й точки: {p2}")
#
# p3 = p1 + p2
# print(f'Сложение координат: ({p3})')
# p3 = p1 - p2
# print(f'Вычитание координат: ({p3})')
# p3 = p1 * p2
# print(f'Умножение: ({p3})')
# p3 = p1 / p2
# print(f'Деление: ({p3})')
#
# print(f'Равенство координат: {p1 == p2}')
#
# print(f"x = {p1['x']} x1 = {p2['x']}")
# print(f"y = {p1['y']} y1 = {p2['y']}")
# print(f"z = {p1['z']} z1 = {p2['z']}")
#
# print()
# print('Запись координат в 1-ю точку:')
# p1['x'] = 20
# print('Запись значения в координату х:', p1['x'])
# p1['y'] = 20
# print('Запись значения в координату y:', p1['y'])
# p1['z'] = 20
# print('Запись значения в координату z:', p1['z'])
# print()
# print(f"Новые координаты 1-й точки: {p1}")
#
# print()
# print('Запись координат во 2-ю точку:')
# p2['x'] = 10
# print('Запись значения в координату х:', p2['x'])
# p2['y'] = 25
# print('Запись значения в координату y:', p2['y'])
# p2['z'] = 40
# print('Запись значения в координату z:', p2['z'])
# print()
# print(f"Новые координаты 2-й точки: {p2}")


# Вариант 2


# class Point3D:
#     def __init__(self, *coord):
#         for k in coord:
#             if not isinstance(k, int) or k == 0:
#                 raise ValueError("Координата должна быть целым числом не равным нулю")
#         self.coord = list(coord)
#
#     def __str__(self):
#         return f'{self.coord}'.strip("[]")
#
#     def __getitem__(self, item):
#         return self.coord[item]
#
#     def __add__(self, other):
#         return tuple(map(lambda x, y: x + y, self.coord, other.coord))
#
#     def __sub__(self, other):
#         return tuple(map(lambda x, y: x - y, self.coord, other.coord))
#
#     def __mul__(self, other):
#         return tuple(map(lambda x, y: x * y, self.coord, other.coord))
#
#     def __truediv__(self, other):
#         return tuple(map(lambda x, y: x / y, self.coord, other.coord))
#
#     def __eq__(self, other):
#         return self.coord == other.coord
#
#     def __len__(self):
#         return len(self.coord)
#
#     def __setitem__(self, key, value):
#         if not isinstance(value, int) or value == 0:
#             raise ValueError("Координата должна быть целым числом не равным нулю")
#         self.coord[key] = value
#
#
# p1 = Point3D(12, 15, 18)
# p2 = Point3D(6, 3, 9)
#
# print(f"Kоординаты 1-й точки: {p1}")
# print(f"Kоординаты 2-й точки: {p2}")
# p3 = p1 + p2
# print(f'Сложение координат: {p3}')
# p3 = p1 - p2
# print(f'Вычитание координат: {p3}')
# p3 = p1 * p2
# print(f'Умножение: {p3}')
# p3 = p1 / p2
# print(f'Деление: {p3}')
#
# print(f'Равенство координат: {p1 == p2}')
#
# for i in range(len(p1)):
#     c = ['x', 'y', 'z']
#     print(f"{c[i]} = {p1[i]} {c[i]}1 = {p2[i]}")
#
# print()
# print('Запись координат в 1-ю точку:')
# p1[0] = 20
# print('Запись значения в координату х:', p1[0])
# p1[1] = 20
# print('Запись значения в координату y:', p1[1])
# p1[2] = 20
# print('Запись значения в координату z:', p1[2])
# print()
# print(f"Новые координаты 1-й точки: {p1}")
#
# print()
# print('Запись координат во 2-ю точку:')
# p2[0] = 10
# print('Запись значения в координату х:', p2[0])
# p2[1] = 20
# print('Запись значения в координату y:', p2[1])
# p2[2] = 30
# print('Запись значения в координату z:', p2[2])
# print()
# print(f"Новые координаты 2-й точки: {p2}")

