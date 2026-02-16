from flask import Blueprint, render_template, request, session, redirect, url_for, flash, current_app  # type: ignore
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab5_index():
    return render_template('lab5/lab5.html', login=session.get('login'))

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'yelizaveta_voroshilova_knowledge_base',
            user = 'yelizaveta_voroshilova_knowledge_base',
            password = '854625',
            client_encoding='UTF8'
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        return render_template('lab5/login.html', error="Заполните поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login = %s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login = ?;", (login,))

    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html',
                               error='Логин и/или пароль неверны')

    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html',
                               error='Логин и/или пароль неверны')

    session['login'] = login
    db_close(conn, cur)
    return redirect('/lab5')

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login or not password:
        return render_template('lab5/register.html', error='Заполните все')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login,))
    existing_user = cur.fetchone()

    if existing_user:
        db_close(conn, cur)
        return render_template('lab5/register.html',
                            error="Такой пользователь уже существует")

    password_hash = generate_password_hash(password)

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))
    else:
        cur.execute("INSERT INTO users (login, password) VALUES (?, ?);", (login, password_hash))

    db_close(conn, cur)
    return redirect('/lab5/login')

@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)
    return redirect('/lab5')

@lab5.route('/lab5/list')
def list():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login=?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return redirect('/lab5/login')

    login_id = user["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE user_id = %s ORDER BY id DESC;", (login_id,))
    else:
        cur.execute("SELECT * FROM articles WHERE login_id = ? ORDER BY id DESC;", (login_id,))

    articles = cur.fetchall()
    db_close(conn, cur)
    
    return render_template('lab5/articles.html', articles=articles)

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('lab5/create.html')

    title = request.form.get('title')
    article_text = request.form.get('article_text')

    if not title or not title.strip():
        return render_template('lab5/create.html', error='Название статьи не может быть пустым')
    
    if not article_text or not article_text.strip():
        return render_template('lab5/create.html', error='Текст статьи не может быть пустым')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login = ?;", (login,))

    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return redirect('/lab5/login')

    login_id = user["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO articles (user_id, title, article_text, is_favorite, is_public, likes) VALUES (%s, %s, %s, %s, %s, %s);", 
                   (login_id, title.strip(), article_text.strip(), False, True, 0))
    else:
        cur.execute("INSERT INTO articles (login_id, title, article_text, is_favorite, is_public, likes) VALUES (?, ?, ?, ?, ?, ?);", 
                   (login_id, title.strip(), article_text.strip(), False, True, 0))

    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/edit/<int:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login = ?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return redirect('/lab5/login')

    login_id = user["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM articles WHERE id = %s AND user_id = %s;", (article_id, login_id))
    else:
        cur.execute("SELECT * FROM articles WHERE id = ? AND login_id = ?;", (article_id, login_id))
    
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return "Статья не найдена или у вас нет прав на её редактирование", 404

    if request.method == 'GET':
        db_close(conn, cur)
        return render_template('lab5/edit.html', article=article)

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = 'is_public' in request.form
    is_favorite = 'is_favorite' in request.form

    if not title or not title.strip():
        return render_template('lab5/edit.html', article=article, error='Название статьи не может быть пустым')
    
    if not article_text or not article_text.strip():
        return render_template('lab5/edit.html', article=article, error='Текст статьи не может быть пустым')

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("""
            UPDATE articles 
            SET title = %s, article_text = %s, is_public = %s, is_favorite = %s 
            WHERE id = %s AND user_id = %s;
        """, (title.strip(), article_text.strip(), is_public, is_favorite, article_id, login_id))
    else:
        cur.execute("""
            UPDATE articles 
            SET title = ?, article_text = ?, is_public = ?, is_favorite = ? 
            WHERE id = ? AND login_id = ?;
        """, (title.strip(), article_text.strip(), is_public, is_favorite, article_id, login_id))

    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/delete/<int:article_id>', methods=['POST'])
def delete(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT id FROM users WHERE login = %s;", (login,))
    else:
        cur.execute("SELECT id FROM users WHERE login = ?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return redirect('/lab5/login')

    login_id = user["id"]

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("DELETE FROM articles WHERE id = %s AND user_id = %s;", (article_id, login_id))
    else:
        cur.execute("DELETE FROM articles WHERE id = ? AND login_id = ?;", (article_id, login_id))

    db_close(conn, cur)
    return redirect('/lab5/list')
