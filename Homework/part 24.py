
class Pair:
    def __init__(self, a, b):
        self.__a = self.__b = 0
        if Pair.val(a) and Pair.val(b):
            self.__a = a
            self.__b = b

    @staticmethod
    def val(z):
        if isinstance(z, int) and z > 0:
            return True
        return False

    @property
    def af(self):
        return self.__a

    @af.setter
    def af(self, a):
        if Pair.val(a):
            self.__a = a
        else:
            print('Значение должно быть целым положительным числом!')

    @property
    def bf(self):
        return self.__b

    @bf.setter
    def bf(self, b):
        if Pair.val(b):
            self.__b = b
        else:
            print('Значение должно быть целым положительным числом!')

    def mult(self):
        return self.__a * self.__b

    def summ(self):
        return f'Сумма: {self.__a + self.__b}'


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        return round(((self.af ** 2 + self.bf ** 2) ** 0.5), 2)

    def square(self):
        return f'Площадь △ABC: {super().mult() * 0.5}'

    def mult(self):
        return f'Произведение: {super().mult()}'

    def info(self):
        return f'Прямоугольный треугольник △ABC ({self.af}, {self.bf}, {self.hypotenuse()})'


p1 = RightTriangle(5, 8)
print(f'Гипотенуза △ABC: {p1.hypotenuse()}')
print(p1.info())
print(p1.square())
print()
print(p1.summ())
print(p1.mult())
print()
p1.af = 8
p1.bf = 10
print(f'Гипотенуза △ABC: {p1.hypotenuse()}')
p1.af = 10
p1.bf = 20
print(f'Гипотенуза △ABC: {p1.hypotenuse()}')
print(p1.summ())
print(p1.mult())
print(p1.square())











