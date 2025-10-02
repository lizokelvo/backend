from flask import Flask, url_for, request, redirect, make_response
import datetime
app = Flask(__name__)

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

@app.route('/400')
def bad_request():
    return '''<!doctype html>
<html>
<head>
    <title>400 Bad Request</title>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1 class="text-danger">400 Bad Request</h1>
            <p>Сервер не может обработать запрос из-за некорректного синтаксиса.</p>
            <p>Проверьте правильность вашего запроса.</p>
            <div class="navigation">
                <a href="/" class="nav-link">На главную</a>
            </div>
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
</html>'''

@app.route("/lab1/web")
def web():
    css_path = url_for("static", filename="lab1.css")
    return """<!doctype html>
        <html>
            <head>
                <title>Главная lab1</title>
                <link rel="stylesheet" href="""" + css_path + """">
            </head>
            <body>
                <div class="container">
                    <div class="content-card">
                        <h1>web-сервер на flask</h1>
                        <div class="navigation">
                            <a href="/lab1/author" class="nav-link">Автор</a>
                            <a href="/index" class="nav-link">Главная сайта</a>
                            <a href="/lab1" class="nav-link">Описание lab1</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>""", 200, {
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Ворошилова Елизавета Андреевна"
    group = "ФБИ-34"
    faculty = "ФБ"
    css_path = url_for("static", filename="lab1.css")

    return """<!doctype html>
        <html>
            <head>
                <title>Об авторе</title>
                <link rel="stylesheet" href="""" + css_path + """">
            </head>
            <body>
                <div class="container">
                    <div class="content-card">
                        <h1>Информация об авторе</h1>
                        <p class="text-success">Студент: """ + name + """</p>
                        <p class="text-warning">Группа: """ + group + """</p>
                        <p class="text-primary">Факультет: """ + faculty + """</p>
                        <div class="navigation">
                            <a href="/lab1/web" class="nav-link">Главная lab1</a>
                            <a href="/index" class="nav-link">Главная сайта</a>
                            <a href="/lab1" class="nav-link">Описание lab1</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>"""

@app.route("/lab1/image")
def image():
    path = url_for("static", filename="cru.jpg")
    css_path = url_for("static", filename="lab1.css")
    
    html_content = '''
    <!doctype html>
    <html>
        <head>
            <title>Цыпленок</title>
            <link rel="stylesheet" href="''' + css_path + '''">
        </head>
        <body>
            <div class="container">
                <div class="content-card">
                    <h1>Цыпленок</h1>
                    <img src="''' + path + '''" class="styled-image" alt="Цыпленок">
                    <p class="text-center text-info">Прекрасный цыпленок с красивой стилизацией</p>
                    <div class="navigation">
                        <a href="/lab1/web" class="nav-link">Главная lab1</a>
                        <a href="/index" class="nav-link">Главная сайта</a>
                        <a href="/lab1/counter" class="nav-link">Счетчик</a>
                    </div>
                </div>
            </div>
        </body>
    </html>'''
    
    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Language': 'ru',
        'X-Student-Name': 'Voroshilova-Elizaveta',
        'X-Student-Group': 'FBI-34',
        'X-University': 'NSTU',
        'X-Custom-Header': 'Flask-Lab-Work',
        'X-Image-Description': 'Cute chicken picture',
        'X-Server-Time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return html_content, 200, headers

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    css_path = url_for("static", filename="lab1.css")

    return '''
    <!doctype html>
    <html>
        <head>
            <title>Счетчик</title>
            <link rel="stylesheet" href="''' + css_path + '''">
        </head>
        <body>
            <div class="container">
                <div class="content-card">
                    <h1>Счетчик посещений</h1>
                    <p>Сколько раз вы сюда заходили: <span class="text-success">''' + str(count) + '''</span></p>
                    <hr>
                    <p>Дата и время: ''' + str(time) + '''</p>
                    <p>Запрошенный адрес: ''' + url + '''</p>
                    <p>Ваш IP-адрес: ''' + client_ip + '''</p>
                    <div class="navigation">
                        <a href="/lab1/counter/clear" class="nav-link">Очистить счетчик</a>
                        <a href="/lab1/web" class="nav-link">Главная lab1</a>
                        <a href="/index" class="nav-link">Главная сайта</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''

@app.route('/lab1/counter/clear')
def clear_counter():
    global count
    count = 0
    return redirect('/lab1/counter')

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    css_path = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <title>Создано</title>
        <link rel="stylesheet" href="''' + css_path + '''">
    </head>
    <body>
        <div class="container">
            <div class="content-card">
                <h1>Создано успешно</h1>
                <div><i>что-то создано...</i></div>
                <div class="navigation">
                    <a href="/lab1/web" class="nav-link">Главная lab1</a>
                    <a href="/index" class="nav-link">Главная сайта</a>
                </div>
            </div>
        </div>
    </body>
</html>
''', 201

@app.route("/lab1")
def lab1():
    css_path = url_for("static", filename="lab1.css")
    return '''<!doctype html>
<html>
<head>
    <title>Лабораторная 1</title>
    <link rel="stylesheet" href="''' + css_path + '''">
</head>
<body>
    <div class="container">
        <div class="content-card">
            <h1>Лабораторная работа 1</h1>
            
            <div class="text-content" style="text-align: left; line-height: 1.8; font-size: 1.1em;">
                <p>
                    Flask — фреймворк для создания веб-приложений на языке программирования Python, 
                    использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. 
                    Относится к категории так называемых микрофреймворков — минималистичных каркасов 
                    веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                </p>
                
                <p style="margin-top: 20px; font-style: italic; color: #b2ebf2;">
                    Flask позволяет быстро создавать веб-приложения с минимальными настройками 
                    и provides flexibility for developers.
                </p>
            </div>
            
            <div class="navigation" style="margin-top: 30px;">
                <a href="/" class="nav-link">← На главную сайта</a>
                <a href="/lab1/web" class="nav-link">К лабораторной 1 →</a>
            </div>

            <h2 style="margin-top: 40px; color: #ffeb3b; border-bottom: 2px solid #ffeb3b; padding-bottom: 10px;">
                Список роутов
            </h2>
            
            <div class="routes-list" style="text-align: left; margin: 20px 0;">
                <h3>Основные страницы:</h3>
                <ul style="list-style: none; padding: 0;">
                    <a href="/" class="nav-link" style="display: inline-block; padding: 5px 15px;">/</a> - Главная страница</li>
                    <a href="/index" class="nav-link" style="display: inline-block; padding: 5px 15px;">/index</a> - Главная страница (альтернатива)</li>
                    <a href="/lab1" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1</a> - Описание лабораторной работы</li>
                </ul>
                
                <h3>Лабораторная работа 1:</h3>
                <ul style="list-style: none; padding: 0;">
                    <a href="/lab1/web" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/web</a> - Главная страница lab1</li>
                    <a href="/lab1/author" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/author</a> - Информация об авторе</li>
                    <a href="/lab1/image" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/image</a> - Страница с изображением</li>
                    <a href="/lab1/counter" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/counter</a> - Счетчик посещений</li>
                    <a href="/lab1/counter/clear" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/counter/clear</a> - Очистка счетчика</li>
                    <a href="/lab1/info" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/info</a> - Перенаправление на автора</li>
                    <a href="/lab1/created" class="nav-link" style="display: inline-block; padding: 5px 15px;">/lab1/created</a> - Страница создания (201 код)</li>
                </ul>
                
                <h3>HTTP Ошибки:</h3>
                <ul style="list-style: none; padding: 0;">
                    <a href="/400" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #ff6b6b, #c23616);">/400</a> - Bad Request</li>
                    <a href="/401" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #e84118, #c23616);">/401</a> - Unauthorized</li>
                    <a href="/402" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #fbc531, #e1b12c);">/402</a> - Payment Required</li>
                    <a href="/403" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #ff4757, #c23616);">/403</a> - Forbidden</li>
                    <a href="/405" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #3742fa, #2f3542);">/405</a> - Method Not Allowed</li>
                    <a href="/418" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #6f4e37, #8B4513);">/418</a> - I'm a teapot</li>
                    <a href="/gjdnjh" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #6f4e37, #8B4513);">/gjdnjh</a> - Перенаправление на 418</li>
                    <a href="/errors" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #ff4757, #c23616;">/errors</a> - Список всех ошибок</li>
                </ul>
                
                <h3>Тестовые роуты:</h3>
                <ul style="list-style: none; padding: 0;">
                    <a href="/generate-error" class="nav-link" style="display: inline-block; padding: 5px 15px; background: linear-gradient(45deg, #ff6b6b, #c23616);">/generate-error</a> - Генерация 500 ошибки</li>
                </ul>
            </div>
            
            <div class="navigation" style="margin-top: 30px;">
                <a href="/" class="nav-link">На главную сайта</a>
                <a href="/lab1/web" class="nav-link">Главная lab1</a>
                <a href="/lab1/author" class="nav-link">Об авторе</a>
            </div>
        </div>
    </div>
</body>
</html>'''

@app.route("/lab2/a/")
def a2():
    return 'со слешем'

@app.route("/lab2/a")
def a():
    return 'без слеша'
