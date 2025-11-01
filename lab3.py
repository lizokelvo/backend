from flask import Blueprint, url_for, request, redirect, abort, render_template, make_response # type: ignore
import datetime

lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')
    
    if not name:
        name = 'Аноним'

    if not age:
        age = 'неизвестен'
    
    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'red')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    
    errors = {}
    if user is None:
        user = ''
    else:
        if not user:
            errors['user'] = 'Заполните поле имени'
    
    return render_template('lab3/form1.html', 
                         user=user, 
                         age=age, 
                         sex=sex, 
                         errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay', methods=['POST'])
def pay():
    drink = request.form.get('drink')
    additions = request.form.getlist('additions')
    return render_template('lab3/pay.html', drink=drink, additions=additions)


@lab3.route('/lab3/success', methods=['POST'])
def success():
    card = request.form.get('card')
    name = request.form.get('name')
    cvv = request.form.get('cvv')
    return render_template('lab3/success.html')


@lab3.route('/lab3/set_color', methods=['GET', 'POST'])
def set_color():
    if request.method == 'POST':
        response = make_response(redirect('/lab3/set_color'))
        
        if request.form.get('reset'):
            return reset_style()  
        
        color = request.form.get('color')
        custom_color = request.form.get('custom_color')
        if custom_color:
            response.set_cookie('color', custom_color, max_age=60*60*24*30)
        elif color:
            response.set_cookie('color', color, max_age=60*60*24*30)
        
        bg_color = request.form.get('bg_color')
        custom_bg_color = request.form.get('custom_bg_color')
        if custom_bg_color:
            response.set_cookie('bg_color', custom_bg_color, max_age=60*60*24*30)
        elif bg_color:
            response.set_cookie('bg_color', bg_color, max_age=60*60*24*30)
        
        font_size = request.form.get('font_size')
        custom_font_size = request.form.get('custom_font_size')
        if custom_font_size:
            response.set_cookie('font_size', custom_font_size, max_age=60*60*24*30)
        elif font_size:
            response.set_cookie('font_size', font_size, max_age=60*60*24*30)
        
        font_family = request.form.get('font_family')
        if font_family:
            response.set_cookie('font_family', font_family, max_age=60*60*24*30)
        
        header_color = request.form.get('header_color')
        if header_color:
            response.set_cookie('header_color', header_color, max_age=60*60*24*30)
        
        header_bg = request.form.get('header_bg')
        if header_bg:
            response.set_cookie('header_bg', header_bg, max_age=60*60*24*30)
     
        footer_color = request.form.get('footer_color')
        if footer_color:
            response.set_cookie('footer_color', footer_color, max_age=60*60*24*30)
        
        footer_bg = request.form.get('footer_bg')
        if footer_bg:
            response.set_cookie('footer_bg', footer_bg, max_age=60*60*24*30)
        
        return response
    
    return render_template('lab3/color.html')


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    errors = []
    
    if request.method == 'POST':

        fio = request.form.get('fio', '').strip()
        age_str = request.form.get('age', '').strip()
        shelf = request.form.get('shelf', '')
        departure = request.form.get('departure', '').strip()
        destination = request.form.get('destination', '').strip()
        travel_date = request.form.get('travel_date', '')
        
        bedding = 'bedding' in request.form
        luggage = 'luggage' in request.form
        insurance = 'insurance' in request.form
        
        if not fio:
            errors.append('ФИО пассажира обязательно для заполнения')
        if not age_str:
            errors.append('Возраст обязателен для заполнения')
        if not shelf:
            errors.append('Необходимо выбрать полку')
        if not departure:
            errors.append('Пункт выезда обязателен для заполнения')
        if not destination:
            errors.append('Пункт назначения обязателен для заполнения')
        if not travel_date:
            errors.append('Дата поездки обязательна для заполнения')
        
        age = None
        if age_str:
            try:
                age = int(age_str)
                if age < 1 or age > 120:
                    errors.append('Возраст должен быть от 1 до 120 лет')
            except ValueError:
                errors.append('Возраст должен быть числом')
        
        if errors:

            return render_template('lab3/ticket_form.html',
                                errors=errors,
                                fio=fio,
                                age=age_str,
                                shelf=shelf,
                                departure=departure,
                                destination=destination,
                                travel_date=travel_date,
                                bedding=bedding,
                                luggage=luggage,
                                insurance=insurance)
     
        base_price = 700 if age < 18 else 1000
        is_child = age < 18
        
        shelf_price = 100 if shelf in ['lower', 'lower_side'] else 0
        bedding_price = 75 if bedding else 0
        luggage_price = 250 if luggage else 0
        insurance_price = 150 if insurance else 0
        
        total_price = base_price + shelf_price + bedding_price + luggage_price + insurance_price
  
        return render_template('lab3/ticket_result.html',
                            fio=fio,
                            age=age,
                            shelf=shelf,
                            departure=departure,
                            destination=destination,
                            travel_date=travel_date,
                            bedding=bedding,
                            luggage=luggage,
                            insurance=insurance,
                            is_child=is_child,
                            base_price=base_price,
                            shelf_price=shelf_price,
                            bedding_price=bedding_price,
                            luggage_price=luggage_price,
                            insurance_price=insurance_price,
                            total_price=total_price)
  
    return render_template('lab3/ticket_form.html')


@lab3.route('/lab3/reset_style')
def reset_style():
    """Очистка всех кук стилей"""
    response = make_response(redirect('/lab3/set_color'))
    
    cookies_to_delete = [
        'color', 'bg_color', 'font_size', 'font_family',
        'header_color', 'header_bg', 'footer_color', 'footer_bg'
    ]
    
    for cookie_name in cookies_to_delete:
        response.delete_cookie(cookie_name)
    
    return response