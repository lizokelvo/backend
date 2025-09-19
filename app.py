from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

@app.route("/")
@app.route("/index")
def index():
    css_path = url_for("static", filename="lab1.css")
    return """<!doctype html>
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
                        </nav>
                        <footer style="margin-top: 40px; padding-top: 20px; border-top: 2px solid rgba(255,255,255,0.2);">
                            <p class="text-center text-info">
                                Ворошилова Елизавета Андреевна, ФБИ-34, 3 курс, 2025 год
                            </p>
                        </footer>
                    </div>
                </div>
            </body>
        </html>"""

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
                        </div>
                    </div>
                </div>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
def author():
    name = "Ворошилова Елизавета Андреевна"
    group = "ФБИ-34"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web"> web </a>
            </body>
        </html>"""

@app.route("/lab1/image")
def image ():
    path = url_for("static", filename="cru.jpg")
    css_path = url_for("static", filename="lab1.css")
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Цыпленок</title>
            <link rel="stylesheet" href="''' + css_path + '''">
        </head>
        <body>
            <div class="container">
                <div class="image-page">
                    <h1 class="image-title">Цыпленок</h1>
                    <img src="''' + path + '''" class="styled-image" alt="Цыпленок">
                    <div class="navigation">
                        <a href="/lab1/web" class="nav-link">На главную</a>
                        <a href="/lab1/author" class="nav-link">Об авторе</a>
                        <a href="/lab1/counter" class="nav-link">Счетчик</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''
count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''
        <!doctype html>
        <html>
            <body>
                Сколько раз вы сюда заходили: ''' + str(count) + '''
                <hr>
                Дата и время: ''' + str(time) + '''<br>
                Запрошенный адрес: ''' + url + '''<br>
                Ваш IP-адрес: ''' + client_ip + '''<br>
                <a href="/counter/clear"> counter clear </a>
            </body>
        </html>
        '''

@app.route('/counter/clear')
def clear_counter():
    global count
    count = 0
    return redirect('/lab1/counter')

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
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
            
            <div class="navigation" style="margin-top: 20px;">
                <a href="/lab1/author" class="nav-link">Автор</a>
                <a href="/lab1/image" class="nav-link">Изображение</a>
                <a href="/lab1/counter" class="nav-link">Счетчик</a>
            </div>
        </div>
    </div>
</body>
</html>'''