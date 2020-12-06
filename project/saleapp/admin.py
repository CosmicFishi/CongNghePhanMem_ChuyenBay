from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user

from saleapp.models import maybay, khchuyenbay, chuyenbay, khachhang, sanbay, sanbaytrunggian, loaighe

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
class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class View(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_export = True
    can_delete = False

admin.add_view(View(maybay, db.session))
admin.add_view(View(khchuyenbay, db.session))
admin.add_view(View(chuyenbay, db.session))
admin.add_view(View(khachhang, db.session))
admin.add_view(View(sanbay, db.session))
admin.add_view(View(sanbaytrunggian, db.session))
admin.add_view(View(loaighe, db.session, name='loai ghe '))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(LogoutView(name='Logout'))
