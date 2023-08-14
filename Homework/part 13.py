def sum1_decorator(fn):
    def wrap(*args_1):
        print("Сумма чисел", ", ".join([str(i) for i in args_1]), "=", fn(*args_1))
        print("Среднее арифметическое чисел", ", ".join([str(i) for i in args_1]), "=", fn(*args_1) / len(args_1))

    return wrap


@sum1_decorator
def sum1(*args):
    return sum(args)


sum1(2, 3, 3, 4)