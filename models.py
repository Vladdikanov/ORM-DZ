import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key= True)
    name = sq.Column(sq.String(length=40),unique= True)

    book = relationship("Book", back_populates="publisher")
    def __repr__(self):
        return f"{self.id} {self.name}"

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key= True)
    title = sq.Column(sq.String(length=40),unique= True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable= False)

    publisher = relationship(Publisher, back_populates="book")
    stock = relationship("Stock", back_populates= "book")
    def __repr__(self):
        return self.title

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key= True)
    name = sq.Column(sq.String(length=40),unique= True)

    stock = relationship("Stock", back_populates="shop")
    def __repr__(self):
        return self.name

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key= True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable= False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable= False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, back_populates= "stock")
    shop = relationship(Shop, back_populates="stock")
    def __repr__(self):
        return ""

class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key= True)
    price = sq.Column(sq.Float, nullable= False)
    date_sale = sq.Column(sq.DateTime, nullable= False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable= False)
    count = sq.Column(sq.Integer, nullable= False)

    stock = relationship(Stock, backref= "sale" )
    def __repr__(self):
        return f"{self.price} {self.date_sale}"


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


