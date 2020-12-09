from flask import render_template, request, redirect
from flask_login import login_user
import hashlib
from saleapp import app, utils, login
from saleapp.admin import *
from saleapp.models import khachhang


@app.route("/")
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)


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

# @app.route('/login-admin', methods=['post', 'get'])
# def login_admin():
#     if request.method == "POST":
#
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#         user = User.query.filter(User.username == username.strip(),
#                                  User.password == password).first()
#         if user:
#             login_user(user=user)
#     return redirect('/admin')
#
#
@login.user_loader
def load_user(user_id):
    return khachhang.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
