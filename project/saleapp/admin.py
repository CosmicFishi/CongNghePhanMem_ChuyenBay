from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user

from saleapp.models import maybay, khchuyenbay, chuyenbay, khachhang, sanbay, sanbaytrunggian, loaighe

class AuthenticatedView(BaseView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_export = True
    can_delete = True
    def is_accessible(self):
        return current_user.is_authenticated

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')
    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(LogoutView(name='Logout'))
admin.add_view(ModelView(maybay, db.session, name='Máy bay'))
admin.add_view(ModelView(khchuyenbay, db.session, name='Vé'))
admin.add_view(ModelView(chuyenbay, db.session, name='Chuyến bay'))
admin.add_view(ModelView(khachhang, db.session, name='Khách hàng'))
admin.add_view(ModelView(sanbay, db.session, name='Sân bay'))
admin.add_view(ModelView(sanbaytrunggian, db.session, name='Sân bay TG'))
admin.add_view(ModelView(loaighe, db.session, name='Loại Vé'))
