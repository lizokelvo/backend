from flask import Blueprint, render_template, request, session, redirect, url_for, flash  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore

lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab5_index():
    """Главная страница лабораторной работы 5"""
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    """Страница входа"""   
    return render_template('lab5/login.html')

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    """Страница регистрации"""
    return render_template('lab5/register.html')

@lab5.route('/lab5/list')
def list_articles():
    """Список статей"""
    return render_template('lab5/list.html')

@lab5.route('/lab5/create', methods=['GET', 'POST'])
def create_article():
    """Создание статьи"""
    return render_template('lab5/create.html')
