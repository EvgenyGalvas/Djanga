import json


class Country:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital

    def add_data(self, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = dict()

        data[self.country] = self.capital

        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def del_data(filename):
        try:
            data = json.load(open(filename))
            if data:
                country_del = input('Введите название страны, которую хотите удалить (с заглавной буквы): ')
                temp_data = data.copy()
                if country_del in temp_data:
                    del temp_data[country_del]
                    print('Запись удалена!')
                else:
                    print('Такой страны в базе данных нет!')
            else:
                print('База данных пустая!')
                return
            with open(file, 'w') as f:
                json.dump(temp_data, f)

        except FileNotFoundError:
            print('База данных отсутствует!')

    @staticmethod
    def search_data(filename):
        try:
            data = json.load(open(filename))
            if data:
                country_search = input('Введите название страны или столицы которые вы хотите найти (с заглавной буквы): ')
                c = 0
                for item in data.items():
                    if country_search in item:
                        print(item[country_search == item[0]])
                        c += 1
                if c == 0:
                    print("Такого названия нет.")
            else:
                print('База данных пустая!')

        except FileNotFoundError:
            print('База данных отсутствует!')

    @staticmethod
    def edit_data(filename):
        try:
            data = json.load(open(filename))
            if data:
                country_edit = input('Введите название страны для редактирования (с заглавной буквы): ')

                temp_data = data.copy()
                if country_edit in temp_data:
                    new_capital = input('Ведите название столицы страны (с заглвной буквы): ')
                    temp_data[country_edit] = new_capital
                    print('Запись отредактирована!')
                else:
                    print('Такой страны в базе данных нет!')
            else:
                print('База данных пустая!')
                return
            with open(file, 'w') as f:
                json.dump(temp_data, f)

        except FileNotFoundError:
            print('База данных отсутствует!')

    @staticmethod
    def watch_data(filename):
        try:
            data = json.load(open(filename))
            if data:
                print(data)
            else:
                print('База данных пустая!')

        except FileNotFoundError:
            print('База данных отсутствует!')

    @staticmethod
    def load_from_file(filename):
        with open(filename) as f:
            return json.load(f)


def my_decorator(func):
    def wrap():
        print("*" * 30)
        func()
        print("*" * 30)
    return wrap


file = 'world.json'


@my_decorator
def action():
    while True:
        print('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных'
              '\n5 - просмотр данных\n6 - заверщение работы')
        a = input("Ввод: ")
        if a == '1':
            new_country = input('Введите название страны (с заглавной буквы): ')
            new_capital = input('Введите название столицы страны (с заглавной буквы): ')
            p1 = Country(new_country, new_capital)
            p1.add_data(file)
            print('Файл сохранен')
            # print(Country.load_from_file(file))
            print('*' * 30)
        elif a == '2':
            Country.del_data(file)
            print('*' * 30)
        elif a == '3':
            Country.search_data(file)
            print('*' * 30)
        elif a == '4':
            Country.edit_data(file)
            print('*' * 30)
        elif a == '5':
            Country.watch_data(file)
            print('*' * 30)
        elif a == '6':
            break
        else:
            print('Введите число в диапазоне от 1 до 6!')
            continue


action()
