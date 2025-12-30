from flask import Blueprint, render_template, request, session, redirect, url_for, flash  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore

lab5 = Blueprint('lab5', __name__)

# Временные данные для демонстрации
# В реальном приложении нужно использовать базу данных
users_db = {}
articles_db = []

@lab5.route('/lab5/')
def lab5_index():
    """Главная страница лабораторной работы 5"""
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    """Страница входа"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Проверка учетных данных
        if username in users_db and check_password_hash(users_db[username]['password'], password):
            session['username'] = username
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('lab5.lab5_index'))
        else:
            flash('Неверное имя пользователя или пароль', 'error')
    
    return render_template('lab5/login.html')

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    """Страница регистрации"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Валидация
        if not username or not password:
            flash('Все поля обязательны для заполнения', 'error')
        elif len(username) < 3:
            flash('Имя пользователя должно содержать не менее 3 символов', 'error')
        elif len(password) < 6:
            flash('Пароль должен содержать не менее 6 символов', 'error')
        elif password != confirm_password:
            flash('Пароли не совпадают', 'error')
        elif username in users_db:
            flash('Пользователь с таким именем уже существует', 'error')
        else:
            # Регистрация пользователя
            users_db[username] = {
                'password': generate_password_hash(password),
                'created_at': '2025-01-01'  # В реальном приложении нужно использовать datetime
            }
            flash('Регистрация прошла успешно! Теперь вы можете войти.', 'success')
            return redirect(url_for('lab5.login'))
    
    return render_template('lab5/register.html')

@lab5.route('/lab5/list')
def list_articles():
    """Список статей"""
    return render_template('lab5/list.html', articles=articles_db)

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create_article():
    """Создание статьи"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Заполните все поля', 'error')
        else:
            article = {
                'id': len(articles_db) + 1,
                'title': title,
                'content': content,
                'author': session.get('username', 'Anonymous'),
                'created_at': '2025-01-01'  # В реальном приложении нужно использовать datetime
            }
            articles_db.append(article)
            flash('Статья успешно создана!', 'success')
            return redirect(url_for('lab5.list_articles'))
    
    return render_template('lab5/create.html')

@lab5.route('/lab5/logout')
def logout():
    """Выход из системы"""
    session.pop('username', None)
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('lab5.lab5_index'))