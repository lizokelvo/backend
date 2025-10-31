from flask import Blueprint, url_for, request, redirect, abort, render_template # type: ignore
import datetime

lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/a/")
def a2():
    return 'со слешем'


@lab2.route("/lab2/a")
def a():
    return 'без слеша'


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "цветок: " + flower_list[flower_id]


@lab2.route('/lab2/add_flower/')
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name=None):
    if name is None:
        abort(400)
    
    flower_list.lab2end(name)
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


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase  = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)


@lab2.route('/lab2/flower/<int:flower_id>')
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


@lab2.route('/lab2/clear_flowers')
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


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)


@lab2.route('/lab2/calc/')
def calc_default():
    """Перенаправляет с /lab2/calc/ на /lab2/calc/1/1"""
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    """Перенаправляет с /lab2/calc/<a> на /lab2/calc/<a>/1"""
    return redirect(f'/lab2/calc/{a}/1')


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc_full(a, b):
    """Основной обработчик калькулятора с двумя числами"""
    return render_template('calc.html', a=a, b=b)


@lab2.route('/lab2/books')
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


@lab2.route('/lab2/berries')
def berries_list():
    """Страница со всеми ягодами"""
    return render_template('berries.html', berries=berries)


@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')
