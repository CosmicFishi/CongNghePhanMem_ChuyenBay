from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')
    #
    def is_accessible(self):
        return current_user.is_authenticated

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated

# admin.add_view(ModelView(Category, db.session))
# admin.add_view(ModelView(Product, db.session))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(LogoutView(name='Logout'))