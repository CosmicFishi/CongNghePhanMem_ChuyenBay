from flask_admin import BaseView, expose

from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.model import maybay, khchuyenbay, chuyenbay, khachhang, sanbay, sanbaytrunggian, loaighe

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

admin.add_view(ModelView(maybay, db.session))
admin.add_view(ModelView(khchuyenbay, db.session))
admin.add_view(ModelView(chuyenbay, db.session))
admin.add_view(ModelView(khachhang, db.session))
admin.add_view(ModelView(sanbay, db.session))
admin.add_view(ModelView(sanbaytrunggian, db.session))
admin.add_view(ModelView(loaighe, db.session))

admin.add_view(ContactView(name="lien he"))