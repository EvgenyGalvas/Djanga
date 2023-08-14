import os.path

import click
from flask import render_template, url_for, request, flash, session, redirect, g, Flask
import sqlite3
from f_data import FDataBase

DATABASE = 'flask_base.db'
DEBUG = True

app = Flask(__name__)

SECRET_KEY = '2b71c1ed2dc317653673b28ddfcbe70da5a616ddddce'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flask_base.db')))


@app.route("/")
def base():
    return render_template('rely_home.html')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with app.open_resource('sqhema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@app.route("/products")
def home():
    # db = get_db()
    # pos_res = db.execute('SELECT * FROM newtab').fetchall()
    # return render_template('one.html', menu=pos_res)
    return render_template('one.html')


@app.route("/list_products")
def get():
    db = get_db()
    res = db.execute('SELECT * FROM chip').fetchall()
    return render_template('list.html', res=res)


@app.route("/adition/")
def get_add():

    return render_template('add.html')


# @app.route("/add_post", methods=["POST", "GET"])
# def add_post():
#     db = get_db()
#     dbase = FDataBase(db)
#
#     if request.method == "POST":
#         res = dbase.add_post(request.form['name'], request.form['post'], request.form['price'])
#         if not res:
#             print('Error')
#         else:
#             print('Success')
#
#     return render_template('sec.html', menu=dbase.get_menu(), title="Добавление статьи")


@app.route('/add_chip', methods=['GET', 'POST'])
def add_chip():
    if request.method == 'POST':
        name = request.form['name']
        characteristic = request.form['characteristic']
        price = request.form['price']

        conn = get_db()
        conn.execute('INSERT INTO chip (name, characteristic, prise) VALUES (?, ?, ?)', (name, characteristic, price))
        conn.commit()
        conn.close()

        return redirect(url_for('base'))

    return render_template('list.html')






if __name__ == "__main__":
    app.run()
