from flask import request, redirect, flash
from saleapp import db
from saleapp.models import customer, UserRole, flight, airport, scheduled, seat_type
from flask_login import login_user

from datetime import datetime
import hashlib
import json


def read_data(path='data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# def read_products(cate_id=None, kw=None, from_price=None, to_price=None):
#     products = read_data(path='data/products.json')
#
# if cate_id:
#     cate_id = int(cate_id)
#     products = [p for p in products \
#                 if p['category_id'] == cate_id]
#
#     if kw:
#         products = [p for p in products \
#                     if p['name'].find(kw) >= 0]
#
#     if from_price and to_price:
#         from_price = float(from_price)
#         to_price = float(to_price)
#         products = [p for p in products \
#                     if to_price >= p['price'] >= from_price]
#
#     return products


def get_product_by_id(product_id):
    products = read_data(path='data/products.json')
    for p in products:
        if p["id"] == product_id:
            return p


def check_register(account_name, user_name, password, id_card, phone):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    u = customer(user_name=user_name, account_name=account_name, password=password, id_card=id_card, phone=phone)

    try:
        print('running')
        db.session.add(u)
        db.session.commit()
        return True
    except:
        return False


def check_user(type_user=UserRole.ADMIN):
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = customer.query.filter(customer.user_name == username.strip(),
                                     customer.password == password,
                                     customer.type_user == type_user).first()

        if user:
            login_user(user=user)
    return redirect('/')


def conver_str_time(string_time='', time_format="%d-%m-%Y - %H:%M"):
    d = datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
    return d.strftime(time_format)


def get_airport():
    return airport.query.all()


def get_flight(flight_from=None, flight_to=None, flight_depart=None, flight_return=None):
    return flight.query.filter(flight.flight_from == flight_from,
                               flight.flight_to == flight_to,
                               flight.time_start > flight_depart).all()


def get_book_history(current_user_id):
    b_history_flight_from = db.session.query(scheduled, seat_type, flight, airport) \
        .filter(current_user_id == scheduled.customer_id) \
        .filter(seat_type.id == scheduled.seat_type_id) \
        .filter(flight.id == scheduled.flight_id) \
        .filter(flight.flight_from == airport.id) \
        .all()
    b_history_flight_to = db.session.query(scheduled, flight, airport) \
        .filter(current_user_id == scheduled.customer_id) \
        .filter(flight.id == scheduled.flight_id) \
        .filter(flight.flight_to == airport.id) \
        .all()

    # b_history = b_history_flight_to

    return b_history_flight_from, b_history_flight_to
