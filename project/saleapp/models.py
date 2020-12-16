from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, login_required
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Enum, DateTime
from sqlalchemy.orm import relationship
from saleapp import db
from enum import Enum as UserEnum
from sqlalchemy.sql import func


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2
    STAFF = 3

class customer(db.Model, UserMixin):
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String(50), nullable=False)

    email = Column(String(255), nullable=False)
    account_name = Column(String(255))
    password = Column(String(50))
    type_user = Column(Enum(UserRole), default=UserRole.USER)
    id_card = Column(String(12), nullable=False)
    phone = Column(String(11), nullable=False)
    active = Column(Boolean, default=True)

    scheduled = relationship('scheduled', lazy=True, backref="customer")

    def is_accessible(self):
        return False


class plane(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    plane_name = Column(String(255))
    airlines = Column(String(50))

    seat_type = relationship('seat_type', lazy=True, backref="plane")
    flight = relationship('flight', lazy=True, backref="plane")

    def is_accessible(self):
        return current_user.is_authenticated


class airport(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    place = Column(String(255), nullable=False)
    airport_name = Column(String(255), nullable=False)
    image = Column(String(300), nullable=False)
    intermediate_airport = relationship('intermediate_airport', lazy=True, backref="airport")

    def is_accessible(self):
        return current_user.is_authenticated


class flight(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)

    plane_id = Column(Integer, ForeignKey(plane.id))
    flight_from = Column(Integer, ForeignKey(airport.id), nullable=False)
    flight_to = Column(Integer, ForeignKey(airport.id), nullable=False)
    time_start = Column(DateTime, nullable=False)
    flight_time = Column(String(10), nullable=False)

    scheduled = relationship('scheduled', lazy=True, backref="flight")
    intermediate_airport = relationship('intermediate_airport', lazy=True, backref="flight")
    flight_to_id = relationship('airport', lazy=True, foreign_keys=[flight_to])
    flight_from_id = relationship('airport', lazy=True, foreign_keys=[flight_from])

    def is_accessible(self):
        return current_user.is_authenticated

    def get_flight_time(self):
        t = self.flight_time
        total_flight_time = ''
        if t[:2] > '00':
            total_flight_time += t[:2] + ' hr'
            if t[:2] > '01':
                total_flight_time += 's'
        if t[3:] > '00':
            total_flight_time += ' ' + t[2:] + ' min'
            if t[3:] > '01':
                total_flight_time += 's'
        return total_flight_time


class seat_type(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    plane_id = Column(Integer, ForeignKey(plane.id))
    seat_name = Column(String(255), nullable=False)
    row_from = Column(Integer, nullable=False)
    row_to = Column(Integer, nullable=False)
    amount_of_row = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    scheduled = relationship('scheduled', lazy=True, backref="seat_type")

    def is_accessible(self):
        return current_user.is_authenticated

    def get_total_seat(self):
        return (self.row_to - self.row_from) * self.amount_of_row

    def get_seat_left(self, flight_id):
        sch =  scheduled.query.filter(scheduled.flight_id == flight_id).all()
        used = 0;
        for i in sch:
            used += int(i.count_seat)
        return  self.get_total_seat() - used

    def seat_be_use(self):
        sch = scheduled.query.filter(scheduled.seat_type_id == self.id).all()
        used = [];
        for i in sch:
            used = used + i.position.split(',')
        return used

    def is_seat_be_use(self, position):
        return position in self.seat_be_use()

class scheduled(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    flight_id = Column(Integer, ForeignKey(flight.id), nullable=False)
    customer_id = Column(Integer, ForeignKey(customer.id), nullable=False)
    seat_type_id = Column(Integer, ForeignKey(seat_type.id), nullable=False)

    position = Column(String(255))
    count_seat = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    is_used = Column(Boolean, default=False)
    time_create = Column(DateTime(timezone=True), nullable=False, default=func.now())

    def is_accessible(self):
        return current_user.is_authenticated

    def get_total_money(self):
        return float(self.price) * int(self.count_seat)

class intermediate_airport(db.Model):
    flight_id = Column(Integer, ForeignKey(flight.id), primary_key=True)
    id = Column(Integer, ForeignKey(airport.id), primary_key=True)

    time_layover = Column(String(255), nullable=False)
    order = Column(String(255), nullable=False)
    note = Column(String(255), nullable=True)

    def is_accessible(self):
        return current_user.is_authenticated

    def get_time_layover(self):
        t = self.time_layover
        delay = ''
        if t[:2] > '00':
            delay += t[:2] + 'h'
        if t[2:] > '00':
            delay += ' ' + t[2:] + 'm'
        return delay

class admin_properties(db.Model):
    id = Column(Integer, autoincrement=True, primary_key=True)
    flight_time = Column(String(255), nullable=False, default="30")
    intermediate_airport = Column(Integer, nullable=False, default=2)
    flight_stopped_time = Column(String(255), nullable=False, default="20")
    time_for_cancel_ticket = Column(String(255), nullable=False, default="1 day")
    time_for_booking_ticket = Column(String(255), nullable=False, default="1 day")

if __name__ == '__main__':
    db.create_all()
