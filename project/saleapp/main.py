from flask import render_template, request, session, jsonify
from saleapp import app, utils, login, decorator
from saleapp.admin import *
from saleapp.models import customer, flight, airport, UserRole
from datetime import datetime, timedelta
from flask_login import logout_user, current_user
import json


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

        card['TGXuatPhat'] = utils.conver_str_time(i.time_start)
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
    else:
        airports = utils.get_airport()
        return render_template('book.html', airports=airports)


@app.route('/book-detail', methods=['post'])
def book_detail():
    flight_from = int((request.form.get('flight_from')).split('.')[0])
    flight_to = int((request.form.get('flight_to')).split('.')[0])
    flight_return = request.form.get('return')
    flight_depart = request.form.get('depart')

    flight_depart = datetime.strptime(flight_depart, '%Y-%m-%d')
    flights = utils.get_flight(flight_from=flight_from,
                               flight_to=flight_to,
                               flight_depart=flight_depart,
                               flight_return=flight_return)

    for i in flights:
        a = datetime.strptime(i.time_start, "%Y-%m-%d %H:%M:%S")
        b = a + timedelta(hours=int(i.flight_time[:2]), minutes=int(i.flight_time[3:]))

        setattr(i, 'time_end', (str(b))[11:16])
        i.time_start = i.time_start[11:16]
        i.flight_time = i.flight_time[:2] + ' hrs ' + i.flight_time[3:] + ' mins'

    return render_template('book-detail.html', flights=flights)


@app.route('/book-history')
def book_history():
    b_history_flight_from, b_history_flight_to = utils.get_book_history(current_user_id=current_user.id);
    # import pdb
    # pdb.set_trace()
    return render_template('book-history.html', b_history_flight_from=b_history_flight_from,
                           b_history_flight_to=b_history_flight_to)


@app.route('/add_ticket', methods=['post'])
def add_ticket():
    if 'ticket' not in session:
        session['ticket'] = {}

    ticket = session['ticket']

    data = json.loads(request.data)

    flight_id = str(data.get("flight_id"))
    customer_id = data.get("customer_id", None)
    seat_type_id = data.get("seat_type_id")
    count_seat = data.get('count_seat')
    price = data.get('price')
    id = flight_id + seat_type_id

    ticket[id] = {
        "id": id,
        "flight_id": flight_id,
        "customer_id": customer_id,
        "seat_type_id": seat_type_id,
        "count_seat": count_seat,
        "price": price,
    }

    session['ticket'] = ticket

    quantity, amount = 0, 0

    return jsonify({
        "total_quantity": quantity,
        "total_amount": amount
    })


@app.route('/profile')
def profile():
    return render_template('profile.html')


# @app.route('/payment')
# def payment():
#     quantity, amount = utils.cart_stats(session.get('cart'))
#     cart_info = {
#         "total_quantity": quantity,
#         "total_amount": amount
#     }
#     return render_template('payment.html', cart_info=cart_info)
#
#
# @app.route('/api/pay', methods=['post'])
# @decorator.login_required
# def pay():
#     if utils.add_receipt(session.get('cart')):
#         del session['cart']
#
#         return jsonify({
#             "message": "Add receipt successful!",
#             "err_code": 200
#         })
#
#     return jsonify({
#         "message": "Failed"
#     })

@app.route('/logout')
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect('/login')


@app.route('/login', methods=['get', 'post'])
def login_for_user():
    if request.method == 'POST':
        return utils.check_user(type_user=UserRole.USER)
    else:
        return render_template('login.html')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    return utils.check_user(type_user=UserRole.ADMIN)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@login.user_loader
def load_user(user_id):
    return customer.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
