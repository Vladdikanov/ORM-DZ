import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Book, Stock, Shop, Publisher, Sale

DSN = "postgresql://postgres:03051997@localhost:5432/ormdz"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open("tests_data.json", "rt") as f:
    file = json.load(f)

for i in file:
    if i["model"] == "publisher":
        pub = Publisher(id= i["pk"], name= i["fields"]["name"])
        session.add(pub)
        session.commit()
    if i["model"] == "book":
        book = Book(id= i["pk"], title= i["fields"]["title"], id_publisher= i["fields"]["publisher"])
        session.add(book)
        session.commit()
    if i["model"] == "shop":
        shop = Shop(id=i["pk"], name=i["fields"]["name"])
        session.add(shop)
        session.commit()
    if i["model"] == "stock":
        stock = Stock(id= i["pk"], id_shop= i["fields"]["shop"], id_book=i["fields"]["book"], count= i["fields"]["count"])
        session.add(stock)
        session.commit()
    if i["model"] == "sale":
        sale = Sale(id= i["pk"], price= i["fields"]["price"], date_sale= i["fields"]["date_sale"], count= i["fields"]["count"], id_stock= i["fields"]["stock"])
        session.add(sale)
        session.commit()
x = input("Введите имя или индификатор автора")
if x.isdigit() != True:
    for c in session.query(Book, Shop, Sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name.ilike(x)):
        print(c)
else:
    for c in session.query(Book, Shop, Sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id == x):
        print(c)
# x = input("Введите имя или индификатор автора")
# for c in session.query(Book, Shop, Sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(or_(Publisher.name.ilike(f"%{x}%"), Publisher.id == int(x))):
#     print(c)
session.close()
