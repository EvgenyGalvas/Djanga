
class Car:

    def __init__(self, model, year, maker, power, color, price):
        self.model = model
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print('Данные автомобиля'.center(40, '*'))
        print(f'Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.maker}\n'
              f'Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}')
        print('=' * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_maker(self, maker):
        self.maker = maker

    def get_maker(self):
        return self.maker

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


c1 = Car('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
c1.print_info()
c1.set_model('CX-5')
c1.set_year('2023')
c1.set_maker('Mazda')
c1.set_power('210 л.с.')
c1.set_color('red')
c1.set_price('4320000')
c1.print_info()
print(c1.get_model())
print(c1.get_year())
print(c1.get_maker())
print(c1.get_power())
print(c1.get_color())
print(c1.get_price())

