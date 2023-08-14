from math import pi, sqrt


class Sphere:

    def __init__(self, x, y, z, r, a, b, c):
        self.__x = self.__y = self.__z = self.__r = self.__a = self.__b = self.__c = 0
        if Sphere.__check_value_coord(x) and Sphere.__check_value_coord(y) and Sphere.__check_value_coord(z) \
                and Sphere.__check_value_radius(r) and Sphere.__check_value_coord(a) and Sphere.__check_value_coord(b)\
                and Sphere.__check_value_coord(c):
            self.__x = x
            self.__y = y
            self.__z = z
            self.__r = r
            self.__a = a
            self.__b = b
            self.__c = c

    def __check_value_coord(f):
        if isinstance(f, (int, float)):
            return True
        else:
            return False

    def __check_value_radius(f):
        if isinstance(f, (int, float)) and f > 0:
            return True
        else:
            return False

    @property
    def radius(self):
        return self.__r

    @radius.setter
    def radius(self, r):
        if Sphere.__check_value_radius(r):
            self.__r = r
        else:
            print("Значение радиуса должно быть любым положительным числом!")

    def set_coords_center(self, x, y, z):
        if Sphere.__check_value_coord(x) and Sphere.__check_value_coord(y) and Sphere.__check_value_coord(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            print("Значение координаты центра сферы должно быть числом!")

    def get_coords_center(self):
        return self.__x, self.__y, self.__z

    def set_is_point_inside(self, a, b, c):
        if Sphere.__check_value_coord(a) and Sphere.__check_value_coord(b) and Sphere.__check_value_coord(c):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            print("Значение координаты точки должно быть числом!")

    def get_is_point_inside(self):
        return self.__a, self.__b, self.__c

    def is_point_inside(self):
        m = sqrt((self.__a - self.__x) ** 2 + (self.__b - self.__y) ** 2 + (self.__c - self.__z) ** 2)
        if m > self.__r:
            return False
        else:
            return True

    def volume(self):
        return (4 * pi * self.__r ** 3) / 3

    def square(self):
        return 4 * pi * self.__r ** 2


p1 = Sphere(0, 0, 0, 0, 0, 0, 0)
p1.radius = 0.6
p1.set_coords_center(0, 0, 0)
print("get_radius:", p1.radius)
print("get_volume:", p1.volume())
print("get_square:", p1.square())
print("get_center:", p1.get_coords_center())
p1.set_is_point_inside(0, -1.5, 0)
print(f"is_point_inside{p1.get_is_point_inside()}:", p1.is_point_inside())
p1.radius = 1.6
print(f"set_radius({p1.radius}):", p1.radius)
print("get_volume:", p1.volume())
print("get_square:", p1.square())
print(f"is_point_inside{p1.get_is_point_inside()}:", p1.is_point_inside())


