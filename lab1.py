from flask import Blueprint, url_for, request, redirect # type: ignore
import datetime

lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1/web")
def web():
    css_path = url_for("static", filename="lab1.css")
    return """
    <!doctype html>
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


@lab1.route("/lab1/author")
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


@lab1.route("/lab1/image")
def image():
    path = url_for("static\lab1", filename="cru.jpg")
    css_path = url_for("static\lab1", filename="lab1.css")
    
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


@lab1.route('/lab1/counter')
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

@lab1.route('/lab1/counter/clear')
def clear_counter():
    global count
    count = 0
    return redirect('/lab1/counter')

@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@lab1.route("/lab1/created")
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

@lab1.route("/lab1")
def lab1_page():
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
