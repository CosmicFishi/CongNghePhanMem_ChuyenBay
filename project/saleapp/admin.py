from saleapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_admin import BaseView, expose
from flask_login import current_user, logout_user

from saleapp.models import plane, scheduled, flight, customer, airport, intermediate_airport, seat_type, admin_properties


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

    def is_accessible(self):
        return current_user.is_authenticated


class RuleView(BaseView):
    @expose('/')
    def index(self):
        rules = db.session.query(admin_properties).first()
        planes = db.session.query(plane).all()

        return self.render('admin/rule.html', rules=rules, planes=planes)

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


admin.add_view(View(plane, db.session, name='Máy bay'))
admin.add_view(View(scheduled, db.session, name="Vé"))
admin.add_view(View(flight, db.session, name='Chuyến bay'))
admin.add_view(View(customer, db.session, name='Khách hàng'))
admin.add_view(View(airport, db.session, name='Sân bay'))
admin.add_view(View(intermediate_airport, db.session, name='Sân bay trung gian'))
admin.add_view(View(seat_type, db.session, name='Loại ghế'))
admin.add_view(ContactView(name='Liên hệ'))
admin.add_view(LogoutView(name='Logout'))
admin.add_view(RuleView(name='Rules'))
admin.add_view(View(admin_properties, db.session, name="Thay đổi quy định"))
