from parse import Parser


def main():
    for i in range(1, 5):
        pars = Parser(f'https://freelance.habr.com/tasks?page={i}', 'freework.csv')
        pars.run()


if __name__ == '__main__':
    main()
