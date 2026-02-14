from flask import Blueprint, render_template, request, session, redirect, url_for, flash  # type: ignore
import psycopg2
from psycopg2.extras import RealDictCursor

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab5_index():
    return render_template('lab5/lab5.html', login=session.get('login'))

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error="Заполние поля")

    conn = psycopg2.connect(
        host = 'localhost',
        database = 'yelizaveta_voroshilova_knowledge_base',
        user = 'yelizaveta_voroshilova_knowledge_base',
        password = '854625' 
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"SELECT * FROM users WHERE login='{login}';")
    user = cur.fetchone()

    if not user:
        cur.close()
        conn.close()
        return render_template('lab5/login.html', 
                               error='Логин и/или пароль неверны')

    if user['password'] != password:
        cur.close()
        conn.close()
        return render_template('lab5/login.html', 
                               error='Логин и/или пароль неверны')
    
    session['login'] = login
    cur.close()
    conn.close()
    return render_template('lab5/success_login.html', login=login)
    
@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')


    if not login or not password:
        return render_template('lab5/register.html', error='Заполните все')

    try:
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'yelizaveta_voroshilova_knowledge_base',
            user = 'yelizaveta_voroshilova_knowledge_base',
            password = '854625'
        )
        cur = conn.cursor()

        cur.execute("SELECT login FROM users WHERE login = %s;", (login,))
        existing_user = cur.fetchone()
        
        if existing_user:
            cur.close()
            conn.close()
            return render_template('lab5/register.html',
                                error="Такой пользовательуже существует")
        
        cur.execute(
            "INSERT INTO users (login, password) VALUES (%s, %s);",
            (login, password)
        )
        conn.commit()
        cur.close()
        conn.close()
        return render_template('lab5/success.html', login=login)

    except Exception as e:
        return render_template('lab5/register.html', error=f"Ошибка: {e}")

@lab5.route('/lab5/list')
def list_articles():
    return render_template('lab5/list.html')

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create_article():
    return render_template('lab5/create.html')
