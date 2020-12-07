from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user, login_required
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db


class User(UserMixin, db.Model):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class khachhang(db.Model):

    MaKH = Column(Integer, autoincrement=True, primary_key=True)
    TenKH = Column(String(255), nullable=False)
    CMND = Column(String(12), nullable=False)
    SDT = Column(String(11), nullable=False)

    khchuyenbay_khachhang = relationship('khchuyenbay', lazy=True)
    def is_accessible(self):
        return False


class maybay(db.Model):
    MaMayBay = Column(Integer, autoincrement=True, primary_key=True)
    TenMayBay = Column(String(255))

    loaighe_maybay = relationship('loaighe', lazy=True)
    chuyenbay_maybay = relationship('chuyenbay', lazy=True)
    def is_accessible(self):
        return current_user.is_authenticated


class sanbay(db.Model):
    MaSanBay = Column(Integer, autoincrement=True, primary_key=True)
    TenSanBay = Column(String(255), nullable=False)

    sanbaytrunggian_sanbay = relationship('sanbaytrunggian', lazy=True)
    khchuyenbay_sanbay = relationship('sanbaytrunggian', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class chuyenbay(db.Model):
    MaMayBay = Column(Integer, ForeignKey(maybay.MaMayBay))
    MaChuyenBay = Column(Integer, autoincrement=True, primary_key=True)
    SanBayDi = Column(Integer, ForeignKey(sanbay.MaSanBay), nullable=False)
    SanBayDen = Column(Integer, ForeignKey(sanbay.MaSanBay), nullable=False)
    TGXuatPhat = Column(String(255), nullable=False)
    TGBay = Column(String(255), nullable=False)

    khchuyenbay_chuyenbay = relationship('khchuyenbay', lazy=True)
    sanbaytrunggian_chuyenbay = relationship('sanbaytrunggian', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class loaighe(db.Model):
    MaMayBay = Column(Integer, ForeignKey(maybay.MaMayBay))
    MaGhe = Column(Integer, autoincrement=True, primary_key=True)
    MaChuyenBay = Column(Integer, nullable=False)
    TenGhe = Column(String(255), nullable=False)
    SoLuong = Column(String(255), nullable=False)

    khchuyenbay_loaighe = relationship('khchuyenbay', lazy=True)

    def is_accessible(self):
        return current_user.is_authenticated


class khchuyenbay(db.Model):
    MaKH = Column(Integer, ForeignKey(khachhang.MaKH), primary_key=True)
    MaChuyenBay = Column(Integer, ForeignKey(chuyenbay.MaChuyenBay), primary_key=True)
    MaGhe = Column(Integer, ForeignKey(loaighe.MaGhe), primary_key=True)
    SLGhe = Column(String(255), nullable=False)
    DonGia = Column(String(255), nullable=False)
    DaDung = Column(Boolean, default=False)

    def is_accessible(self):
        return current_user.is_authenticated


class sanbaytrunggian(db.Model):
    MaChuyenBay = Column(Integer, ForeignKey(chuyenbay.MaChuyenBay), primary_key=True)
    MaTrungGian = Column(Integer, ForeignKey(sanbay.MaSanBay), nullable=True)
    ThoiGianDung = Column(String(255), nullable=False)
    ThuTu = Column(String(255), nullable=False)
    GhiChu = Column(String(255), nullable=True)

    def is_accessible(self):
        return current_user.is_authenticated


if __name__ == '__main__':
    db.create_all()
