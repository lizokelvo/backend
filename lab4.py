from flask import Blueprint, render_template, request # type: ignore

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    if x2 == '0':
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 / x2

    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '':
        result = x1 + 0
    else:
        result = x1 + x2

    if x2 == '':
        result = x1 + 0
    else:
        result = x1 + x2

    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2

    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

tree_count = 0
MAX_TREES = 10  

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
  
    if request.method == 'POST': # type: ignore
        operation = request.form.get('operation') # type: ignore
        
        if operation == 'plant' and tree_count < MAX_TREES:
            tree_count += 1
        elif operation == 'cut' and tree_count > 0:
            tree_count -= 1

        return redirect('/lab4/tree') # type: ignore
    
    return render_template('lab4/tree.html',  # type: ignore
                         tree_count=tree_count,
                         max_trees=MAX_TREES,
                         can_plant=tree_count < MAX_TREES,
                         can_cut=tree_count > 0)

CORRECT_LOGIN = 'lizok'
CORRECT_PASSWORD = '254685'

users = [
    {'login': 'alex', 'password': '123'},
    {'login': 'bob', 'password': '555'},
    {'login': 'user1', 'password': 'qwerty'},
    {'login': 'admin', 'password': 'admin123'},
    {'login': 'test', 'password': 'test123'}
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    error = None
    authorized = False
    user_login = None
    
    if request.method == 'POST':
        login_input = request.form.get('login')
        password_input = request.form.get('password')
        
        # Проверка учетных данных по списку пользователей
        for user in users:
            if login_input == user['login'] and password_input == user['password']:
                authorized = True
                user_login = login_input
                break  # Прерываем цикл, если нашли пользователя
        
        if not authorized:
            error = 'Неверные логин и/или пароль'
    
    # Рендерим шаблон с соответствующими параметрами
    return render_template('lab4/login.html', 
                         authorized=authorized,
                         login=user_login,
                         error=error)