from flask import Blueprint, render_template, request, jsonify  

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "The Conjuring",
        "title_ru": "Заклятье",
        "year": 2013,
        "description": "Эд и Лоррейн Уоррены — детективы, которые расследуют паранормальные дела. Однажды к ним обращается семья, страдающая от злого духа. Уоррены, вынужденные сражаться с могущественной демонической сущностью, сталкиваются с самым пугающим случаем в своей жизни."
    },
    {
        "title": "INSIDIOUS",
        "title_ru": "Астрал",
        "year": 2010,
        "description": "Джош и Рене переезжают с детьми в новый дом, но не успевают толком распаковать вещи, как начинаются странные события. Необъяснимо перемещаются предметы, в детской звучат странные звуки, но настоящий кошмар начинается, когда их десятилетний сын Далтон впадает в кому."
    },
    {
        "title": "Paranormal activity",
        "title_ru": "Паранормальное явление",
        "year": 2007,
        "description": "Молодая пара проживает в доме, который, как они подозревают, посещается некой злой силой. Чтобы зафиксировать паранормальную активность, они настраивают видеокамеру."
    },
    {
        "title": "REC",
        "title_ru": "Репортаж",
        "year": 2007,
        "description": "Начинающий телерепортёр Анхела Видаль жаждет сенсаций. С завидным упорством она ищет уникальный материал, а потому выезжает с командой спасателей на место происшествия."
    },
    {
        "title": "Тайна перевала Дятлова",
        "title_ru": "Тайна перевала Дятлова",
        "year": 2013,
        "description": "В 2012 году группа американских студентов отправляется в Уральские горы, следуя тем же маршрутом, что и группа Дятлова."
    },
]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET', 'DELETE'])
def handle_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    
    if request.method == 'GET':
        return jsonify(films[id])
    
    elif request.method == 'DELETE':
        del films[id]
        return '', 204
    
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        return jsonify({"error": "Film not found"}), 404
    
    film = request.get_json()
    if not film:
        return jsonify({"error": "No data provided"}), 400

    if not film.get('title') or film.get('title').strip() == '':
        film['title'] = film.get('title_ru', '')
    
    if film.get('description') == '':
        return jsonify({"description": "Заполните описание"}), 400
    
    films[id] = film
    return jsonify(films[id]), 200

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_films():
    new_film = request.get_json()
    
    if not new_film:
        return jsonify({"error": "No data provided"}), 400
    
    required_fields = ['title', 'title_ru', 'year', 'description']
    for field in required_fields:
        if field not in new_film:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    if not new_film.get('title') or new_film.get('title').strip() == '':
        new_film['title'] = new_film.get('title_ru', '')
    
    if new_film.get('description') == '':
        return jsonify({"description": "Заполните описание"}), 400
   
    films.append(new_film)
    
    new_index = len(films) - 1
    return jsonify({
        "message": "Film added successfully",
        "id": new_index,
        "film": films[new_index]
    }), 201