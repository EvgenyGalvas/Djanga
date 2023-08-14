from flask import Flask, render_template, url_for, request, flash, session, redirect, g
import sqlite3
import os
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '8f222bba2bb35888f80ec03a3e255cbc2a3d5ead'




app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SECRET_KEY'] = 'jdghgblxi3874lvicn545nlncldklfjs'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

menu = [
    {'name': 'Главная страница', 'url': 'books'},
    {'name': 'Книги в наличии', 'url': 'items'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
]

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def books():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('books.html', title='Главная страница библиотеки', menu=dbase.get_menu(),
                           books=dbase.get_books_annonce())

@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_book(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления книги', category='error')
            else:
                flash('Книга добавлена успешно', category='success')
        else:
            flash('Ошибка добавления книги', category='error')

    return render_template('add_book.html', menu=dbase.get_menu(), title='Добавление книги')

@app.route("/book/<alias>")
def show_book(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(alias)
    return render_template('book.html', menu=dbase.get_menu(), title=title, post=post)

@app.route('/items')
def items():
    print(url_for('items'))
    return render_template('items.html', title='Книги в наличии', menu=menu)

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно!', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # print(request.form)
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title='Обратная связь', menu=menu)
    return render_template('contact.html', title='Обратная связь', menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
