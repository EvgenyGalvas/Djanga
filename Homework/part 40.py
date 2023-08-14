from jinja2 import Template

# Задание 1

site = [
    {'href': '/index', 'title': 'Главная'},
    {'href': '/news', 'title': 'Новости'},
    {'href': '/about', 'title': 'О компании'},
    {'href': '/shop', 'title': 'Магазин'},
    {'href': '/contacts', 'title': 'Контакты'}
]

link = """<ul>
{% for k in site -%}
{%- if k.title == 'Главная' -%}
<li><a href="{{ k.href }}" class="active">{{ k.title }}</a></li>
{%- else %}
<li><a href="{{ k.href }}">{{ k.title }}</a></li>
{%- endif -%}
{% endfor %}
</ul>"""

tm = Template(link)
msg = tm.render(site=site)

print(msg)


# Задание 2

# html = """
# {%- macro text_input(name, placeholder, type='text') -%}
# <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
#
# <p>{{ text_input("firstname", "Имя") }}</p>
# <p>{{ text_input("lastname", "Фамилия") }}</p>
# <p>{{ text_input("address", "Адрес") }}</p>
# <p>{{ text_input("phone", "Телефон", type="tel") }}</p>
# <p>{{ text_input("email", "Почта", type="email") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

