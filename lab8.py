from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from db import db
from db.models import User, Article
from werkzeug.security import generate_password_hash, check_password_hash

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def lab8_index():
    return render_template('lab8/lab8.html', page='main')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab8/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    remember = request.form.get('remember') == 'on'
    
    if not login or not password:
        return render_template('lab8/login.html', error='Заполните все поля')
    
    user = User.query.filter_by(login=login).first()
    
    if user and check_password_hash(user.password, password):
        login_user(user, remember=remember)
        return redirect(url_for('lab8.lab8_index'))
    
    return render_template('lab8/login.html', error='Неверный логин или пароль')

@lab8.route('/lab8/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not login or not password:
        return render_template('lab8/register.html', error='Заполните все поля')
    
    existing_user = User.query.filter_by(login=login).first()
    if existing_user:
        return render_template('lab8/register.html', error='Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password)
    new_user = User(login=login, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    login_user(new_user)
    return redirect(url_for('lab8.lab8_index'))

@lab8.route('/lab8/articles')
@login_required
def articles():
    user_articles = Article.query.filter_by(login_id=current_user.id).all()
    return render_template('lab8/lab8.html', page='articles', articles=user_articles)

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('lab8/lab8.html', page='create')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    if not title or not article_text:
        return render_template('lab8/lab8.html', page='create', error='Заполните все поля')
    
    new_article = Article(
        login_id=current_user.id,
        title=title,
        article_text=article_text,
        is_favorite=False,
        is_public=True,
        likes=0
    )
    
    db.session.add(new_article)
    db.session.commit()
    
    return redirect(url_for('lab8.articles'))

@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit(article_id):
    article = Article.query.get_or_404(article_id)
    
    if article.login_id != current_user.id:
        return redirect(url_for('lab8.articles'))
    
    if request.method == 'GET':
        return render_template('lab8/edit.html', article=article)
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    
    if not title or not article_text:
        return render_template('lab8/edit.html', article=article, error='Заполните все поля')
    
    article.title = title
    article.article_text = article_text
    db.session.commit()
    
    return redirect(url_for('lab8.articles'))

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete(article_id):
    article = Article.query.get_or_404(article_id)
    
    if article.login_id == current_user.id:
        db.session.delete(article)
        db.session.commit()
    
    return redirect(url_for('lab8.articles'))

@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('lab8.lab8_index'))