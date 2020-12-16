from flask import render_template, request, session, jsonify, send_file
from saleapp import app, utils, login, decorator
from saleapp.admin import *
from saleapp.models import customer, flight, airport, UserRole, seat_type, intermediate_airport
from datetime import datetime, timedelta
from flask_login import logout_user, current_user
from saleapp.config import MoMo
import json
from PIL import Image
import qrcode


@app.route("/")
def index():
    flights = flight.query.all()
    return render_template('index.html', flights=flights)


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
            email = request.form.get('email')

            if utils.check_register(account_name=account_name,
                                    user_name=user_name,
                                    password=password, phone=phone,
                                    id_card=id_card,
                                    email=email):
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


@app.route('/book', methods=['get'])
def book():
    airports = utils.get_airport()
    return render_template('book.html', airports=airports)


@app.route('/book-detail', methods=['post'])
def book_detail():
    ticket = {}
    ticket['flight_from'] = (request.form.get('flight_from')).split('.')[1]
    ticket['flight_to'] = (request.form.get('flight_to')).split('.')[1]
    session['ticket'] = ticket

    flight_from = int((request.form.get('flight_from')).split('.')[0])
    flight_to = int((request.form.get('flight_to')).split('.')[0])
    flight_return = request.form.get('return')
    flight_depart = request.form.get('depart')

    flight_depart = datetime.strptime(flight_depart, '%Y-%m-%d')
    flights = utils.get_flight(flight_from=flight_from,
                               flight_to=flight_to,
                               flight_depart=flight_depart,
                               flight_return=flight_return)

    if len(flights) == 0:
        mess = "Sorry! We can not found a flight"
        airports = utils.get_airport()
        return render_template('book.html', mess=mess, airports=airports)
    else:
        inter_airport = []
        seat = []
        for i in flights:
            inter_airport.append(utils.get_intermediate_airport(flightID=i.id))
            seat.append(utils.get_seat_type_by_flight(plane_id=i.plane_id, flight_id=i.id))
        if len(inter_airport[0]) == 0:
            inter_airport = None
        return render_template('book-detail.html', flights=flights, inter_airport=inter_airport, seat=seat)


@app.route('/book-history')
def book_history():
    if not current_user.is_authenticated:
        return render_template('book-history.html')
    else:
        b_history_flight_from, b_history_flight_to = utils.get_book_history(current_user_id=current_user.id);

        return render_template('book-history.html', b_history_flight_from=b_history_flight_from,
                               b_history_flight_to=b_history_flight_to)


@app.route('/add_ticket', methods=['post'])
def add_ticket():
    data = json.loads(request.data)
    if 'ticket' not in session:
        session['ticket'] = {}
    ticket = session['ticket']

    ticket['flight_id'] = data.get("flight_id")
    ticket['plane_id'] = data.get("plane_id")
    ticket['seat_type_id'] = data.get("seat_type_id")
    ticket['seat_name'] = data.get("seat_name")
    ticket['count_seat'] = data.get("count_seat")
    ticket['price'] = data.get("price")

    if current_user.is_authenticated:
        ticket['customer_id'] = current_user.id
        session['ticket'] = ticket
        return jsonify({
            "status": 200,
            "mess": 'Book success!!',
        })
    else:
        session['ticket'] = ticket
        return jsonify({
            "status": 204,
            "mess": 'Book success!!',
        })


@app.route('/fill-info', methods=['get', 'post'])
def fill_info():
    if request.method == 'POST':
        email = request.form.get('email')
        email_confirm = request.form.get('email-confirm')

        if email != email_confirm:
            return render_template('fill-info.html', mess="Email not match!!!")
        else:
            name = request.form.get('name')
            phone1 = request.form.get('phone1')
            phone2 = request.form.get('phone2')
            ticket = session['ticket']
            ticket['email'] = email
            ticket['name'] = name
            ticket['phone'] = str(phone1) + str(phone2)
            session['ticket'] = ticket
            return redirect('/seat-selection')

    return render_template('fill-info.html')


@app.route('/seat-selection', methods=['get'])
def seat_selection():
    if 'ticket' not in session:
        mess = "Sorry you not have any ticket"
        return render_template('seat-selection.html', mess=mess)
    else:
        ticket = session['ticket']
        seat_used = utils.get_seat_used(flight_id=ticket['flight_id'])
        seat = utils.get_seat_available(plane_id=ticket['plane_id'])
        return render_template('seat-selection.html', ticket=ticket, seat=seat, seat_used=seat_used)


@app.route('/payment', methods=['get', 'post'])
def payment():
    if 'ticket' not in session:
        mess = "Sorry you not have any ticket"
        return render_template('payment.html', mess=mess)

    if request.method == 'POST':
        data = json.loads(request.data)

        payment = data.get("payment")
        position = data.get("position")

        ticket = session['ticket']
        ticket['payment'] = payment
        ticket['position'] = position
        session['ticket'] = ticket

        return jsonify({
            "mess": 'Book success!!',
        })
    else:
        return render_template('payment.html')


@app.route('/airport-pay', methods=['post'])
def airport_pay():
    data = request.get_json('ticket')

    img = qrcode.make(data)

    return send_file(img, mimetype='image')


@app.route('/momo-pay', methods=['post'])
def momo_pay():
    ticket = session['ticket']
    total = int((ticket['count_seat'] * ticket['price']) * 22000)

    momo = MoMo(amount=str(total))
    rs = momo.send_momo()

    if rs:
        return jsonify({
            'link': rs
        })
    else:
        jsonify({
            "mess": "Can be pay by MoMo, plz try again.!!!"
        })


@app.route('/staff-pay', methods=['post'])
@decorator.login_staff_required
def staff_pay():
    ticket = session['ticket']
    ticket['position'] = request.get_json('position')['position']
    session['ticket'] = ticket

    if utils.add_ticket_to_db():
        return jsonify({
            'status': 200,
            "mess": "Add sussecc"
        })
    else:
        return jsonify({
            'status': 203,
            "mess": "Add fail, plz try again.!!!"
        })


@app.route('/status_payment')
def status_payment():
    return render_template('status_payment.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect('/login')


@app.route('/staff-seat-selection', methods=['get'])
@decorator.login_staff_required
def staff_seat_selection():
    if 'ticket' not in session:
        mess = "Sorry you not have any ticket"
        return render_template('seat-selection.html', mess=mess)
    else:
        ticket = session['ticket']
        seat_used = utils.get_seat_used(flight_id=ticket['flight_id'])
        seat = utils.get_seat_available(flight_id=ticket['flight_id'], plane_id=ticket['plane_id'])
        return render_template('staff-seat-selection.html', ticket=ticket, seat=seat, seat_used=seat_used)


@app.route('/staff-book', methods=['get', 'post'])
@decorator.login_staff_required
def staff_book():
    if request.method == 'POST':
        flight_from = int((request.form.get('flight_from')).split('.')[0])
        flight_to = int((request.form.get('flight_to')).split('.')[0])
        flight_depart = request.form.get('depart')

        flights = flight.query.filter(flight.flight_from == flight_from,
                                      flight.flight_to == flight_to,
                                      flight.time_start > flight_depart).all()
        if len(flights) == 0:
            mess = "Sorry! We can not found a flight"
            airports = utils.get_airport()
            return render_template('book.html', mess=mess, airports=airports)
        else:
            return render_template('staff-book-detail.html', flights=flights)
    else:
        airports = utils.get_airport()
        return render_template('book.html', airports=airports)


@app.route('/staff-book-history', methods=['get', 'post'])
@decorator.login_staff_required
def staff_book_history():
    if request.method == 'POST':
        id = request.form.get('id')

    his = utils.get_history()
    b_history_flight_from, b_history_flight_to = utils.get_book_history(current_user_id=current_user.id);

    return render_template('staff-book-history.html', b_history_flight_from=b_history_flight_from,
                           b_history_flight_to=b_history_flight_to, historys=his)


@app.route('/staff-find', methods=['get'])
@decorator.login_staff_required
def staff_find():
    pass


@app.route('/login-staff', methods=['get', 'post'])
def login_for_staff():
    if request.method == 'POST':
        return utils.check_user(type_user=UserRole.STAFF)
    else:
        return render_template('login.html', re='/login-staff')


@app.route('/login', methods=['get', 'post'])
def login_for_user():
    if request.method == 'POST':
        return utils.check_user(type_user=UserRole.USER)
    else:
        return render_template('login.html')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    return utils.check_user(type_user=UserRole.ADMIN)


@app.route('/report', methods=['get', 'post'])
@decorator.login_admin_staff_required
def report():
    info = ''
    month = ''
    year = ''
    sum = 0
    if request.method == 'POST':
        if request.form.get('month'):
            month = request.form.get('month')

        if request.form.get('year'):
            year = request.form.get('year')

        info = utils.get_scheduled(month=month, year=year)
        if info:
            for i in info:
                sum += i.sum_price

    return render_template('report.html', info=info, year=year, month=month, sum=sum)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@login.user_loader
def load_user(user_id):
    return customer.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
