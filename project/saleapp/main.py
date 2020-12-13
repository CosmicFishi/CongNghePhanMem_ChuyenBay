from flask import render_template, request
import hashlib
from saleapp import app, utils, login
from saleapp.admin import *
from saleapp.models import customer, flight, airport, UserRole
import time, datetime


@app.route("/")
def index():
    f = flight.query.all()
    cards = []
    for i in f:
        card = {}
        SB = airport.query.get(i.flight_to)
        card['Anh'] = SB.image
        card['BayDen'] = SB.place
        card['MaChuyenBay'] = i.id
        card['TGXuatPhat'] = datetime.datetime.fromtimestamp(int(i.time_start)).strftime("%d/%m/%Y - %H:%M")
        card['BayTu'] = airport.query.get(i.flight_from).place
        cards.append(card)

    categories = utils.read_data()

    return render_template('index.html', categories=categories, cards=cards)


@app.route("/register", methods=['get', 'post'])
def register():
    msg = ''
    if request.method == "POST":
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        if confirm == password:
            account_name = request.form.get('name')
            user_name = request.form.get('username')
            id_card = request.form.get('CMND')
            phone = request.form.get('SDT')

            if utils.check_register(account_name=account_name,
                                    user_name=user_name,
                                    password=password, phone=phone,
                                    id_card=id_card):
                msg = "Đăng kí thành công"
                redirect('/')
            else:
                msg = "Đăng kí thất bại, vui lòng thử lại sau"

    return render_template('register.html', msg_error=msg)


@app.route('/login', methods=['get'])
def log():
    return render_template('login.html')


@app.route('/query', methods=['post', 'get'])
def quer():
    return render_template('query.html')


@app.route('/flight-detail')
def flight_detail():
    return render_template('flight-detail.html')


@app.route('/book', methods=['post', 'get'])
def book():
    if request.method == 'post':
        import pdb
        pdb.set_trace()
        return redirect('/')

    airports = utils.get_airport()
    return render_template('book.html', airports=airports)


@app.route('/book-detail', methods=['post'])
def book_detail():
    flight_from = request.form.get('flight_from')
    flight_to = request.form.get('flight_to')
    flight_return = request.form.get('return')
    flight_depart = request.form.get('depart')
    flights = utils.get_flight(flight_from=flight_from,
                               flight_to=flight_to,
                               flight_depart=flight_depart,
                               flight_return=flight_return)
    return render_template('book-detail.html', flights=flights)


@app.route('/book-history')
def book_history():
    return render_template('book-history.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    return utils.check_user()


@app.route('/login-user', methods=['post', 'get'])
def login_for_user():
    return utils.check_user(type_user=UserRole.USER)


@login.user_loader
def load_user(user_id):
    return customer.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
