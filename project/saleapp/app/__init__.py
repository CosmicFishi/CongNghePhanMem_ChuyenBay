from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.secret_key="askdjasdauo12r1qrt8y93ohto2bt8iou18y3r14ih8yhde8tt8hoi2"
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:haungo@localhost:3308/db?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name="IT SHOP", template_mode="bootstrap4")