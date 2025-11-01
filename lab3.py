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

            response.delete_cookie('color')
            response.delete_cookie('bg_color')
            response.delete_cookie('font_size')
            response.delete_cookie('font_family')
        else:

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
        
        return response
    
    return render_template('lab3/color.html')