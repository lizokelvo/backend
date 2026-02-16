from flask import Flask, url_for, redirect, abort, render_template  # type: ignore
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab5 import lab6
from lab5 import lab7
from lab5 import lab8
from lab5 import lab9
import datetime

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

app.secret_key = 'my_secret_key_254685'

#@app.route("/")
#def hello():
#    return "Flask работает! Главная страница"


@app.errorhandler(404)
def not_found(err):
    css_path = url_for("static", filename="lab1.css")
    return '''<!doctype html>
<html>
<head>
    <title>404 - Страница не найдена</title>
    <link rel="stylesheet" href="''' + css_path + '''">
    <style>
        .error-emoji {
            font-size: 6em;
            margin: 20px 0;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-30px);}
            60% {transform: translateY(-15px);}
        }
        
        .error-funny {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 20px auto;
            max-width: 400px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content-card" style="text-align: center;">
            <div class="error-emoji">🔍❌🌌</div>
            
            <h1 style="color: #ff6b6b; font-size: 3em;">404</h1>
            <h2>Страница пропала в цифровой пучине!</h2>
                        
            <p>Возможные причины:</p>
            <ul style="text-align: left; max-width: 400px; margin: 0 auto;">
                <li>Страница в разработке</li>
                <li>Неправильная ссылка</li>
                <li>Страница переехала в другое измерение</li>
                <li>Временные технические неполадки</li>
            </ul>
            
            <div class="navigation" style="margin-top: 30px;">
                <a href="/" class="nav-link">На главную</a>
                <a href="/lab1" class="nav-link">К лабораторным</a>
            </div>
        </div>
    </div>
</body>
</html>''', 404


@app.errorhandler(500)
def internal_server_error(err):
    css_path = url_for("static", filename="lab1.css")
    
    return '''<!doctype html>
<html>
<head>
    <title>500 - Внутренняя ошибка сервера</title>
    <link rel="stylesheet" href="''' + css_path + '''">
    <style>
        .server-error {
            text-align: center;
            padding: 40px 20px;
        }
        
        .error-code {
            font-size: 6em;
            font-weight: bold;
            color: #ff4757;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.2);
            margin: 0;
            line-height: 1;
        }
        
        .error-message {
            font-size: 2em;
            color: #f8f9fa;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .error-description {
            font-size: 1.2em;
            color: #b2ebf2;
            max-width: 700px;
            margin: 0 auto 30px;
            line-height: 1.6;
            text-align: left;
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
        }
        
        .tech-info {
            background: rgba(255,0,0,0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 20px auto;
            max-width: 600px;
            text-align: left;
        }
        
        .solution-list {
            text-align: left;
            max-width: 500px;
            margin: 0 auto;
        }
        
        .fire-emoji {
            font-size: 4em;
            animation: flicker 1.5s infinite alternate;
        }
        
        @keyframes flicker {
            0% {opacity: 1;}
            50% {opacity: 0.7;}
            100% {opacity: 1;}
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content-card server-error">            
            <div class="error-code">500</div>            
            <div class="error-message">Произошла внутренняя ошибка сервера</div>
            <div class="error-description">
                <strong>Что случилось?</strong><br>
                На сервере произошла непредвиденная ошибка. Это не ваша вина - наши разработчики уже бегут с огнетушителями!
            </div>
            
            <div class="tech-info">
                <strong>Техническая информация:</strong>
                <ul>
                    <li>Ошибка: Internal Server Error</li>
                    <li>Код: 500</li>
                    <li>Время: ''' + str(datetime.datetime.now()) + '''</li>
                    <li>Сервер: Flask Web Server</li>
                </ul>
            </div>
            
            <div style="margin: 30px auto; max-width: 500px;">
                <h3>Что можно сделать?</h3>
                <div class="solution-list">
                    <p>Обновите страницу через несколько минут</p>
                    <p>Вернитесь на главную страницу</p>
                    <p>Сообщите администратору об ошибке</p>
                    <p>Не паникуйте - ошибки бывают у всех!</p>
                </div>
            </div>
            
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
                <a href="javascript:location.reload()" class="nav-link">Обновить страницу</a>
                <a href="/lab1" class="nav-link">К лабораторным</a>
            </div>
            
            <div style="margin-top: 30px; padding: 15px; background: rgba(255,255,255,0.05); border-radius: 10px;">
                <small style="color: #888;">
                   Если ошибка повторяется, пожалуйста, свяжитесь с технической поддержкой
                </small>
            </div>
        </div>
    </div>
</body>
</html>''', 500


@app.route("/")
@app.route("/index")
def index():

    css_path = url_for("static", filename="lab1.css")
    return '''<!doctype html>
<html>
<head>
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet" href="''' + css_path + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <header>
                <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
            </header>
            
            <nav class="navigation">
                <a href="/lab1" class="nav-link">Первая лабораторная</a>
                <a href="/lab2" class="nav-link">Вторая лабораторная</a>
                <a href="/lab3" class="nav-link">Третья лабораторная</a>
                <a href="/lab4" class="nav-link">Четвертая лабораторная</a>
                <a href="/lab5" class="nav-link">Пятая лабораторная</a>
                <a href="/lab6" class="nav-link">Шестая лабораторная</a>
                <a href="/lab7" class="nav-link">Седьмая лабораторная</a>
                <a href="/lab8" class="nav-link">Восьмая лабораторная</a>
                <a href="/lab9" class="nav-link">Девятая лабораторная</a>
                <a href="/lab3/ticket">Железнодорожный билет</a>
                <a href="/lab1/author" class="nav-link">Автор</a>
                <a href="/lab1/image" class="nav-link">Изображение</a>
                <a href="/lab1/counter" class="nav-link">Счетчик</a>
                <a href="/errors" class="nav-link" style="background: linear-gradient(45deg, #ff4757, #c23616);">HTTP Ошибки</a>
            </nav>
            
            <footer style="margin-top: 40px; padding-top: 20px; border-top: 2px solid rgba(255,255,255,0.2);">
                <p class="text-center text-info">
                    Ворошилова Елизавета Андреевна, ФБИ-34, 3 курс, 2025 год
                </p>
            </footer>
        </div>
    </div>
</body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Ворошилова Елизавета'
    return render_template('exemple.html', name=name)

@app.route('/refrigerator', methods=['GET', 'POST'])
def refrigerator():
    if request.method == 'POST': # type: ignore
        temp_input = request.form.get('temperature') # type: ignore

        # Проверка на пустое значение
        if not temp_input:
            return render_template('fridge.html',
                                 error='Ошибка: не задана температура')

        try:
            temperature = int(temp_input)
        except ValueError:
            return render_template('fridge.html',
                                 error='Ошибка: введите числовое значение')

        # Проверка диапазонов
        if temperature < -12:
            return render_template('fridge.html',
                                 error='Не удалось установить температуру — слишком низкое значение')
        elif temperature > -1:
            return render_template('fridge.html',
                                 error='Не удалось установить температуру — слишком высокое значение')

        # Успешные диапазоны
        success_message = f'Установлена температура: {temperature}°C'

        if -12 <= temperature <= -9:
            snowflakes_count = 3
            temp_range = "-12°C до -9°C"
        elif -8 <= temperature <= -5:
            snowflakes_count = 2
            temp_range = "-8°C до -5°C"
        elif -4 <= temperature <= -1:
            snowflakes_count = 1
            temp_range = "-4°C до -1°C"
        else:
            snowflakes_count = 0
            temp_range = "неопределен"

        return render_template('fridge.html',
                             success=success_message,
                             snowflakes_count=snowflakes_count,
                             temp_range=temp_range)

    return render_template('fridge.html')

app.run(debug=True)