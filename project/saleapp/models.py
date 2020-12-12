from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, login_required
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from saleapp import db
from enum import Enum as UserEnum

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class customer(db.Model, UserMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String(50), nullable=False)

    account_name = Column(String(255), nullable=False)
    password = Column(String(50), nullable=False)
    type_user = Column(Enum(UserRole), default=UserRole.USER)
    id_card = Column(String(12), nullable=False)
    phone = Column(String(11), nullable=False)
    active = Column(Boolean, default=True)

    scheduled = relationship('scheduled', lazy=True)

    def is_accessible(self):
        return False


class plane(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    plane_name = Column(String(255))
    airlines = Column(String(50))

    seat_type = relationship('seat_type', lazy=True)
    flight = relationship('flight', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class airport(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    airport_name = Column(String(255), nullable=False)
    image = Column(String(300), nullable=False)
    intermediate_airport = relationship('intermediate_airport', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class flight(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    plane_id = Column(Integer, ForeignKey(plane.id))
    flight_from = Column(Integer, ForeignKey(airport.id), nullable=False)
    flight_to = Column(Integer, ForeignKey(airport.id), nullable=False)
    time_start = Column(String(255), nullable=False)
    flight_time = Column(String(255), nullable=False)

    scheduled = relationship('scheduled', lazy=True)
    intermediate_airport = relationship('intermediate_airport', lazy=True)
    flight_to_id = relationship('airport', lazy=True, foreign_keys=[flight_to])
    flight_from_id = relationship('airport', lazy=True, foreign_keys=[flight_from])

    def is_accessible(self):
        return current_user.is_authenticated


class seat_type(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
<<<<<<< HEAD

    plane_id = Column(Integer, ForeignKey(plane.id))
    seat_name = Column(String(255), nullable=False)
    amount = Column(String(255), nullable=False)
    row_from = Column(Integer, nullable=False)
    row_to = Column(Integer, nullable=False)
    amount_row = Column(Integer, nullable=False)
=======

    plane_id = Column(Integer, ForeignKey(plane.id))
    seat_name = Column(String(255), nullable=False)
    amount = Column(String(255), nullable=False)
    row_from = Column(Integer, nullable=False)
    row_to = Column(Integer, nullable=False)

>>>>>>> 8c4fe4a848b4fc421c275206bfc3f70526642a47
    scheduled = relationship('scheduled', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class scheduled(db.Model):
    flight_id = Column(Integer, ForeignKey(flight.id), primary_key=True)
    customer_id = Column(Integer, ForeignKey(customer.id), primary_key=True)
    seat_type_id = Column(Integer, ForeignKey(seat_type.id), primary_key=True)

    count_seat = Column(String(255), nullable=False)
    price = Column(String(255), nullable=False)
    DaDung = Column(Boolean, default=False)

    def is_accessible(self):
        return current_user.is_authenticated


class intermediate_airport(db.Model):
    flight_id = Column(Integer, ForeignKey(flight.id), primary_key=True)
    id = Column(Integer, ForeignKey(airport.id), nullable=True)

    time_layover = Column(String(255), nullable=False)
    order = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

    def is_accessible(self):
        return current_user.is_authenticated


if __name__ == '__main__':
    db.create_all()
