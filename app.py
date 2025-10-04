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
@app.route("/lab2/a/")
def a2():
    return 'со слешем'

@app.route("/lab2/a")
def a():
    return 'без слеша'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/')
@app.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if name is None:
        abort(400)
    
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Ворошилова Елизавета', 2, 'ФБИ-34', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html',
                            name=name, lab_num=lab_num, group=group,
                            course=course, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase  = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/flower/<int:flower_id>')
def flower(flower_id):
    if flower_id >= len(flower_list) or flower_id < 0:
        abort(404)
    
    flower = flower_list[flower_id]
    return f'''
<!doctype html>
<html>
<head>
    <title>Цветок #{flower_id}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        .flower-info {{ background: #ecf0f1; padding: 20px; border-radius: 10px; }}
        a {{ color: #3498db; text-decoration: none; margin-right: 15px; }}
        a:hover {{ text-decoration: underline; }}
        .nav {{ margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>Цветок #{flower_id}</h1>
    
    <div class="flower-info">
        <p><strong>Название:</strong> {flower}</p>
        <p><strong>ID:</strong> {flower_id}</p>
    </div>
    
    <div class="nav">
        {"<a href='/lab2/flowers/" + str(flower_id-1) + "'>← Предыдущий цветок</a>" if flower_id > 0 else ""}
        {"<a href='/lab2/flowers/" + str(flower_id+1) + "'>Следующий цветок →</a>" if flower_id < len(flower_list)-1 else ""}
    </div>
    
    <div>
        <a href="/lab2/flowers/"> Все цветы ({len(flower_list)})</a> |
        <a href="/lab2/add_flower/">Добавить цветок</a> |
        <a href="/lab2/clear_flowers"> Очистить список</a> |
        <a href="/lab2"> К лабораторной 2</a>
    </div>
</body>
</html>
'''

@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
<!doctype html>
<html>
<head>
    <title>Список очищен</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; text-align: center; }}
        h1 {{ color: #e74c3c; }}
        .message {{ background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; margin: 20px 0; }}
        a {{ color: #3498db; text-decoration: none; margin: 0 10px; padding: 10px 20px; background: #ecf0f1; border-radius: 5px; }}
        a:hover {{ background: #bdc3c7; }}
    </style>
</head>
<body>
    <h1> Список цветов очищен</h1>
    
    <div class="message">
        Все цветы были удалены из списка. Список теперь пуст.
    </div>
    
    <div style="margin-top: 30px;">
        <a href="/lab2/flowers/"> Посмотреть все цветы (0)</a>
        <a href="/lab2/add_flower/"> Добавить первый цветок</a>
        <a href="/lab2"> К лабораторной 2</a>
    </div>
</body>
</html>
'''

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)

@app.route('/lab2/calc/')
def calc_default():
    """Перенаправляет с /lab2/calc/ на /lab2/calc/1/1"""
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def calc_single(a):
    """Перенаправляет с /lab2/calc/<a> на /lab2/calc/<a>/1"""
    return redirect(f'/lab2/calc/{a}/1')

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc_full(a, b):
    """Основной обработчик калькулятора с двумя числами"""
    return render_template('calc.html', a=a, b=b)

@app.route('/lab2/books')
def books_list():
    books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 671},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Роман-эпопея', 'pages': 1225},
    {'author': 'Антон Чехов', 'title': 'Рассказы', 'genre': 'Рассказы', 'pages': 320},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Роман', 'pages': 480},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 240},
    {'author': 'Николай Гоголь', 'title': 'Мёртвые души', 'genre': 'Поэма', 'pages': 352},
    {'author': 'Иван Тургенев', 'title': 'Отцы и дети', 'genre': 'Роман', 'pages': 288},
    {'author': 'Александр Островский', 'title': 'Гроза', 'genre': 'Драма', 'pages': 120},
    {'author': 'Михаил Лермонтов', 'title': 'Герой нашего времени', 'genre': 'Роман', 'pages': 224},
    {'author': 'Иван Гончаров', 'title': 'Обломов', 'genre': 'Роман', 'pages': 576},
    {'author': 'Александр Грибоедов', 'title': 'Горе от ума', 'genre': 'Комедия', 'pages': 160},
    {'author': 'Николай Лесков', 'title': 'Левша', 'genre': 'Повесть', 'pages': 96}
]
    """Страница со списком всех книг"""
    return render_template('books.html', books=books)

berries = [
    {
        'name': 'Клубника',
        'image': 'strawberry.jpg',
        'description': 'Сладкая красная ягода, богатая витамином C и антиоксидантами.',
        'season': 'июнь-июль',
        'color': 'красный'
    },
    {
        'name': 'Малина',
        'image': 'raspberry.jpg', 
        'description': 'Ароматная ягода с нежной текстурой, используется в десертах и лекарствах.',
        'season': 'июль-август',
        'color': 'красный'
    },
    {
        'name': 'Черника',
        'image': 'blueberry.jpg',
        'description': 'Маленькая синяя ягода, улучшает зрение и память.',
        'season': 'июль-август', 
        'color': 'синий'
    },
    {
        'name': 'Ежевика',
        'image': 'blackberry.jpg',
        'description': 'Тёмная сочная ягода с кисло-сладким вкусом, растёт на колючих кустах.',
        'season': 'август-сентябрь',
        'color': 'чёрный'
    },
    {
        'name': 'Голубика',
        'image': 'bilberry.jpg',
        'description': 'Лесная ягода с характерным сизым налётом, очень полезна для глаз.',
        'season': 'июль-август',
        'color': 'синий'
    },
    {
        'name': 'Смородина чёрная',
        'image': 'blackcurrant.jpg',
        'description': 'Ягода с насыщенным вкусом, чемпион по содержанию витамина C.',
        'season': 'июль-август',
        'color': 'чёрный'
    },
    {
        'name': 'Смородина красная', 
        'image': 'redcurrant.jpg',
        'description': 'Прозрачная кисловатая ягода, идеальна для желе и компотов.',
        'season': 'июль-август',
        'color': 'красный'
    },
    {
        'name': 'Крыжовник',
        'image': 'gooseberry.jpg',
        'description': 'Ягода с плотной кожицей, бывает зелёного, жёлтого и красного цвета.',
        'season': 'июль-август',
        'color': 'зелёный'
    },
    {
        'name': 'Облепиха',
        'image': 'seabuckthorn.jpg',
        'description': 'Оранжевые ягоды на колючих ветках, очень богаты витаминами.',
        'season': 'август-октябрь',
        'color': 'оранжевый'
    },
    {
        'name': 'Брусника',
        'image': 'lingonberry.jpg',
        'description': 'Красные кислые ягоды, растут в хвойных лесах, хорошо хранятся.',
        'season': 'август-сентябрь',
        'color': 'красный'
    },
    {
        'name': 'Клюква',
        'image': 'cranberry.jpg', 
        'description': 'Кислая болотная ягода, природный антисептик, хороша для морсов.',
        'season': 'сентябрь-октябрь',
        'color': 'красный'
    },
    {
        'name': 'Земляника',
        'image': 'wild_strawberry.jpg',
        'description': 'Лесная родственница клубники, мелкая но очень ароматная.',
        'season': 'июнь-июль',
        'color': 'красный'
    },
    {
        'name': 'Морошка',
        'image': 'cloudberry.jpg',
        'description': 'Янтарная ягода северных болот, ценный источник витаминов.',
        'season': 'июль-август',
        'color': 'оранжевый'
    },
    {
        'name': 'Жимолость',
        'image': 'honeysuckle.jpg',
        'description': 'Синие продолговатые ягоды, одни из самых ранних, созревают в июне.',
        'season': 'июнь',
        'color': 'синий'
    },
    {
        'name': 'Ирга',
        'image': 'serviceberry.jpg',
        'description': 'Сладкие тёмно-синие ягоды, привлекают птиц, хороши в выпечке.',
        'season': 'июль-август',
        'color': 'синий'
    },
    {
        'name': 'Калина',
        'image': 'viburnum.jpg',
        'description': 'Красные горьковатые ягоды, после заморозков становятся слаще.',
        'season': 'сентябрь-октябрь',
        'color': 'красный'
    },
    {
        'name': 'Рябина',
        'image': 'rowan.jpg',
        'description': 'Оранжево-красные горькие ягоды, используются в народной медицине.',
        'season': 'сентябрь-октябрь',
        'color': 'оранжевый'
    },
    {
        'name': 'Шиповник',
        'image': 'rosehip.jpg',
        'description': 'Плоды дикой розы, рекордсмен по витамину C, используется для чая.',
        'season': 'август-октябрь',
        'color': 'оранжевый'
    },
    {
        'name': 'Боярышник',
        'image': 'hawthorn.jpg',
        'description': 'Красные мучнистые ягоды, полезны для сердечно-сосудистой системы.',
        'season': 'сентябрь-октябрь',
        'color': 'красный'
    },
    {
        'name': 'Бузина',
        'image': 'elderberry.jpg',
        'description': 'Чёрные мелкие ягоды, используются в медицине и кулинарии.',
        'season': 'август-сентябрь',
        'color': 'чёрный'
    }
]

@app.route('/lab2/berries')
def berries_list():
    """Страница со всеми ягодами"""
    return render_template('berries.html', berries=berries)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')