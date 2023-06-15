import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import json
from classes import create_table, Publisher, Sale, Book, Stock, Shop

SQLsystem = 'postgresql'
login = 'postgres'
password = '836098'
host = 'localhost'
port = 5432
db_name = "orm"
DSN = f'{SQLsystem}://{login}:{password}@{host}:{port}/{db_name}'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_table(engine)

with open('test_data.json', 'r') as db:
    data = json.load(db)

for line in data:
    method = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[line['model']]
    session.add(method(id=line['pk'], **line.get('fields')))
session.commit()

search_author = input('Введите имя писателя: ')
for c in session.query(Publisher).filter(Publisher.name.like(f'%{search_author}%')).all():
    print(c)

search_publisher = input('Введите имя издателя: ')
res = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale).\
    join(Publisher).join(Stock).join(Sale).join(Shop).\
    filter(Publisher.name == search_publisher)

for book, shop, price, count, date in res:
    print(f"{book: <40} | {shop: <10} | {price*count: <8} | {date.strftime('%d-%m-%Y')}")

session.close()