from flask import Flask, url_for, redirect, abort, render_template  # type: ignore
from lab1 import lab1
import datetime

app = Flask(__name__)
app.register_blueprint(lab1)


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


@app.route('/generate-error')
def generate_error():
    result = 1 / 0
    return str(result)


@app.errorhandler(400)
def bad_request(err):
    return '''<!doctype html>
<html>
<head>
    <title>400 - Неверный запрос</title>
</head>
<body>
    <div style="text-align: center; padding: 50px;">
        <h1 style="color: #ff6b6b; font-size: 3em;">400</h1>
        <h2>Вы не задали имя цветка!</h2>
        <p>Пожалуйста, укажите название цветка в URL:</p>
        <p><code>/lab2/add_flower/роза</code></p>
        <p><code>/lab2/add_flower/тюльпан</code></p>
        <p><code>/lab2/add_flower/нарцисс</code></p>
        
        <div style="margin-top: 30px;">
            <a href="/lab2" style="padding: 10px 20px; background: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">
                К лабораторной 2
            </a>
        </div>
    </div>
</body>
</html>''', 400


@app.route('/401')
def unauthorized():
    return '''<!doctype html>
<html>
<head>
    <title>401 Unauthorized</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-danger">401 Unauthorized</h1>
            <p>Требуется аутентификация.</p>
            <p>Пожалуйста, авторизуйтесь.</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
        </div>
    </div>
</body>
</html>''', 401


@app.route('/402')
def payment_required():
    return '''<!doctype html>
<html>
<head>
    <title>402 Payment Required</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-danger">402 Payment Required</h1>
            <p>Требуется оплата для доступа к ресурсу.</p>
            <p>Этот код зарезервирован для будущего использования.</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
        </div>
    </div>
</body>
</html>''', 402


@app.route('/403')
def forbidden():
    return '''<!doctype html>
<html>
<head>
    <title>403 Forbidden</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-danger">403 Forbidden</h1>
            <p>Доступ к запрошенному ресурсу запрещен.</p>
            <p>У вас недостаточно прав для просмотра этой страницы.</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
        </div>
    </div>
</body>
</html>''', 403


@app.route('/405')
def method_not_allowed():
    return '''<!doctype html>
<html>
<head>
    <title>405 Method Not Allowed</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-danger">405 Method Not Allowed</h1>
            <p>Метод запроса не поддерживается для данного ресурса.</p>
            <p>Проверьте используемый HTTP метод (GET, POST, etc.).</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
        </div>
    </div>
</body>
</html>''', 405


@app.route('/418')
def teapot():
    return '''<!doctype html>
<html>
<head>
    <title>418 I'm a teapot</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-warning">418 I'm a teapot</h1>
            <p>Ошибка</p>
            <p>Это код ошибки из RFC 2324.</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
                <a href="/gjdnjh" class="nav-link" style="background: linear-gradient(45deg, #6f4e37, #8B4513);">Попробовать снова</a>
            </div>
        </div>
    </div>
</body>
</html>''', 418


@app.route('/gjdnjh')
def gjdnjh():
    return redirect('/418')


@app.route('/errors')
def errors_list():
    css_path = url_for("static", filename="lab1.css")
    return '''<!doctype html>
<html>
<head>
    <title>Список HTTP ошибок</title>
    <link rel="stylesheet" href="''' + css_path + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1>Список HTTP ошибок для тестирования</h1>
            
            <div class="navigation">
                <a href="/400" class="nav-link" style="background: linear-gradient(45deg, #ff6b6b, #c23616);">400 Bad Request</a>
                <a href="/401" class="nav-link" style="background: linear-gradient(45deg, #e84118, #c23616);">401 Unauthorized</a>
                <a href="/402" class="nav-link" style="background: linear-gradient(45deg, #fbc531, #e1b12c);">402 Payment Required</a>
                <a href="/403" class="nav-link" style="background: linear-gradient(45deg, #ff4757, #c23616);">403 Forbidden</a>
                <a href="/405" class="nav-link" style="background: linear-gradient(45deg, #3742fa, #2f3542);">405 Method Not Allowed</a>
                <a href="/418" class="nav-link" style="background: linear-gradient(45deg, #6f4e37, #8B4513);">418 I'm a teapot</a>
            </div>
            
            <div style="margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px;">
                <h3>Как проверить коды ответа:</h3>
                <ol style="text-align: left; margin-left: 20px;">
                    <li>Откройте инструменты разработчика (F12)</li>
                    <li>Перейдите на вкладку "Network"</li>
                    <li>Нажмите на любую ссылку выше</li>
                    <li>В списке запросов найдите ваш запрос</li>
                    <li>В колонке "Status" увидите код ответа</li>
                </ol>
            </div>
            
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
        </div>
    </div>
</body>
</html>'''


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
                <a href="/lab1/web" class="nav-link">Главная lab1</a>
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
