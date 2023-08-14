class NonNegative:
    @staticmethod
    def verify_len(value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError('Значение должно быть положительным целым числом!')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_len(value)
        instance.__dict__[self.name] = value


class Triangle:
    a = NonNegative()
    b = NonNegative()
    c = NonNegative()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def true_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует")
        else:
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует")


p1 = Triangle(2, 5, 6)
p1.true_triangle()
p2 = Triangle(5, 2, 8)
p2.true_triangle()
p3 = Triangle(7, 3, 6)
p3.true_triangle()



