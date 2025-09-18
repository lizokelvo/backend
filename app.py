from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404

@app.route("/")
@app.route("/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">author</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-Type': 'text/plain; charset=utf-8'
        }

@app.route("/author")
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
                <a href="/web"> web </a>
            </body>
        </html>"""

@app.route("/image")
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
                        <a href="/web" class="nav-link">На главную</a>
                        <a href="/author" class="nav-link">Об авторе</a>
                        <a href="/counter" class="nav-link">Счетчик</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''
count = 0

@app.route('/counter')
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
    return redirect('/counter')

@app.route("/info")
def info():
    return redirect("/author")

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