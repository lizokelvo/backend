from flask import Blueprint, render_template, request, session   # type: ignore

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

def user_exists(login):
    """Проверяет, существует ли пользователь с таким логином"""
    for user in users:
        if user['login'] == login:
            return True
    return False

def add_user(login, password):
    """Добавляет нового пользователя"""
    users.append({'login': login, 'password': password})
    return True

def authenticate_user(login, password):
    """Проверяет учетные данные пользователя"""
    for user in users:
        if user['login'] == login and user['password'] == password:
            return True, login
    return False, None

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

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None) # type: ignore
    return redirect('/lab4/login') # type: ignore

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None
    
    if request.method == 'POST':
        login_input = request.form.get('login')
        password_input = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # Валидация данных
        if not login_input or not password_input:
            error = 'Все поля обязательны для заполнения'
        elif len(login_input) < 3:
            error = 'Логин должен содержать не менее 3 символов'
        elif len(password_input) < 4:
            error = 'Пароль должен содержать не менее 4 символов'
        elif password_input != password_confirm:
            error = 'Пароли не совпадают'
        elif user_exists(login_input):
            error = 'Пользователь с таким логином уже существует'
        else:
            # Регистрируем нового пользователя
            add_user(login_input, password_input)
            success = f'Пользователь {login_input} успешно зарегистрирован!'
    
    return render_template('lab4/register.html',
                         error=error,
                         success=success)

@lab4.route('/lab4/grain', methods=['GET', 'POST'])
def grain():
    # Цены на зерно
    prices = {
        'barley': 12000,   # ячмень
        'oat': 8500,       # овёс
        'wheat': 9000,     # пшеница
        'rye': 15000       # рожь
    }
    
    # Русские названия зерна
    grain_names = {
        'barley': 'ячмень',
        'oat': 'овёс',
        'wheat': 'пшеница',
        'rye': 'рожь'
    }
    
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight_input = request.form.get('weight')
        
        # Проверка на пустые значения
        if not grain_type:
            return render_template('lab4/grain.html', 
                                 error='Выберите тип зерна')
        
        if not weight_input:
            return render_template('lab4/grain.html',
                                 error='Укажите вес заказа',
                                 grain_type=grain_type)
        
        try:
            weight = float(weight_input)
        except ValueError:
            return render_template('lab4/grain.html',
                                 error='Вес должен быть числом',
                                 grain_type=grain_type)
        
        # Проверка веса
        if weight <= 0:
            return render_template('lab4/grain.html',
                                 error='Вес должен быть больше 0',
                                 grain_type=grain_type,
                                 weight=weight_input)
        
        # Проверка максимального объема
        if weight > 100:
            return render_template('lab4/grain.html',
                                 error='Такого объёма сейчас нет в наличии (максимум 100 тонн)',
                                 grain_type=grain_type,
                                 weight=weight_input)
        
        # Расчет стоимости
        price_per_ton = prices[grain_type]
        original_price = weight * price_per_ton
        
        # Применение скидки
        discount_applied = False
        discount_amount = 0
        
        if weight > 10:
            discount_applied = True
            discount_amount = original_price * 0.1
            total_price = original_price - discount_amount
        else:
            total_price = original_price
        
        # Формирование сообщения
        grain_name = grain_names[grain_type]
        success_message = 'Заказ успешно сформирован'
        
        return render_template('lab4/grain.html',
                             success=success_message,
                             grain_name=grain_name,
                             weight=weight,
                             total_price=f"{total_price:,.0f}".replace(',', ' '),
                             discount_applied=discount_applied,
                             discount_amount=f"{discount_amount:,.0f}".replace(',', ' '),
                             original_price=f"{original_price:,.0f}".replace(',', ' '),
                             grain_type=grain_type)
    
    return render_template('lab4/grain.html')