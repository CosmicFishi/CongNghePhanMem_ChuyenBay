from flask import render_template, request, redirect
from flask_login import login_user
import hashlib
from saleapp import app, utils, login
from saleapp.admin import *
from saleapp.models import khachhang, chuyenbay, sanbay, UserRole
import time, datetime

@app.route("/")
def index():
    CB = chuyenbay.query.all()
    cards = []

    for i in CB:
        card = {}
        SB = sanbay.query.get(i.SanBayDen)
        card['Anh'] = SB.Anh
        card['BayDen'] = SB.TenSanBay
        card['MaChuyenBay'] = i.MaChuyenBay
        card['TGXuatPhat'] = datetime.datetime.fromtimestamp(int(i.TGXuatPhat)).strftime("%d/%m/%Y")
        card['BayTu'] = sanbay.query.get(i.SanBayDi).TenSanBay
        cards.append(card)

    categories = utils.read_data()
    # import pdb
    # pdb.set_trace()
    return render_template('index.html', categories=categories, cards=cards)


@app.route("/register", methods=['get', 'post'])
def register():
    msg = ''
    if request.method == "POST":
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')

        if confirm == password:
            name = request.form.get('name')
            username = request.form.get('username')
            CMND = request.form.get('CMND')
            SDT = request.form.get('SDT')

            if utils.check_register(name=name, username=username, password=password, SDT=SDT, CMND=CMND):
                msg = "dang ki thanh cong"
            else:
                msg = "dang ki that bai, he thong dang loi"

    return render_template('register.html', msg_error=msg)


@app.route('/login', methods=['post', 'get'])
def log():
    return render_template('login.html')

@app.route('/query', methods=['post', 'get'])
def quer():
    return render_template('query.html')

@app.route('/flight-detail')
def flight_detail():
    return render_template('flight-detail.html')

@app.route('/book-detail')
def bookk_detail():
    return render_template('book-detail.html')


def check_user(loai_nguoi_dung=UserRole.ADMIN):
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = khachhang.query.filter(khachhang.TenTK == username.strip(),
                                      khachhang.MatKhau == password,
                                      khachhang.loai_nguoi_dung == loai_nguoi_dung).first()

        if user:
            login_user(user=user)
    return redirect('/admin')


@app.route('/login-admin', methods=['post', 'get'])
def login_admin():
    return check_user()


@app.route('/login-user', methods=['post', 'get'])
def log_user():
    return check_user(loai_nguoi_dung=UserRole.USER)

@login.user_loader
def load_user(user_id):
    return khachhang.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
