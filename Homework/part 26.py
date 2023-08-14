

class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec

    def __It__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec < other.sec

    def __Ie__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec <= other.sec

    def __ne__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec != other.sec


c1 = Clock(100)
c2 = Clock(200)
c4 = Clock(300)

c3 = c1 + c2 + c4
print(f'c3: {c3.get_format_time()}')
c5 = c3 - c2
print(f'c3 - c2: {c5.get_format_time()}')
c5 = c3 * c2
print(f'c3 * c2: {c5.get_format_time()}')
c5 = c3 // c2
print(f'c3 // c2: {c5.get_format_time()}')
c5 = c3 % c2
print(f'c3 % c2: {c5.get_format_time()}')
c3 -= c2
print(f'c3 -= c2: {c3.get_format_time()}')
c3 *= c2
print(f'c3 *= c2: {c3.get_format_time()}')
c3 //= c2
print(f'c3 //= c2: {c3.get_format_time()}')
c3 %= c2
print(f'c3 %= c2: {c3.get_format_time()}')
print()
c3 = c1 + c2 + c4
print(f'c3 == c1 {c3 == c1}')
print(f'c3 > c1 {c3 > c1}')
print(f'c3 >= c1 {c3 >= c1}')
print(f'c3 < c1 {c3 < c1}')
print(f'c3 <= c1 {c3 <= c1}')
print(f'c3 != c1 {c3 != c1}')
