from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'askdjasdauo12r1qrt8y93ohto2bt8iou18y3r14ih8yhde8tt8hoi2'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:haungo@localhost:3308/db?charset=utf8'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost/db?charset=utf8'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Aerial", template_mode='bootstrap4')
login = LoginManager(app=app)

# Thông tin đăng nhâp momo
# haungo H@ungo230899
# pass mysql pythonany where: dunghau123