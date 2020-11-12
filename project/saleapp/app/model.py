from sqlalchemy import Column, Integer, Float, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship

from app import db


class DefaultClass(db.Model):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class Category(DefaultClass):
    __tablename__ = 'category'

    products = relationship('Product', backref='category', lazy=True)


class Product(DefaultClass):
    __tablename__ = 'product'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(180))

    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    db.create_all()
