class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'
    commission = 0.01

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname}, был открыт.")
        print("*" * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num}, принадлежащий {self.surname}, был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def print_balance(self):
        print(f"Текуший баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f'#{self.num}')
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print("-" * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.value -= val + val * Account.commission
            print(f'{val} {Account.suffix} было успешно снято! Комисcия {Account.commission * val} {self.suffix}.')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)