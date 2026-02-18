from flask import Blueprint, render_template, request, redirect, url_for

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def lab8_index():
    return render_template('lab8/lab8.html', page='main')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/lab8.html', page='login')
   
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not login or not password:
        return render_template('lab8/lab8.html', page='login', error='Заполните все поля')
    
    return redirect(url_for('lab8.lab8_index'))

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/lab8.html', page='register')
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not login or not password:
        return render_template('lab8/lab8.html', page='register', error='Заполните все поля')
    
    return redirect(url_for('lab8.lab8_index'))

@lab8.route('/lab8/articles')
def articles():
    return render_template('lab8/lab8.html', page='articles')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('lab8/lab8.html', page='create')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    if not title or not article_text:
        return render_template('lab8/lab8.html', page='create', error='Заполните все поля')
    
    return redirect(url_for('lab8.articles'))