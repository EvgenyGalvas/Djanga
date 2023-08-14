from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)
tm = env.get_template('main.html')
msg = tm.render(title='Домашнее задание', teg_1='Страница с домашним заданием',
                teg_2='Домашнее задание выполнено!!!')
print(msg)