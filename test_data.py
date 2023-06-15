[
  {"model": "publisher", "pk": 1, "fields": {"name": "O\u2019Reilly"}},
  {"model": "publisher", "pk": 2, "fields": {"name": "Pearson"}},
  {"model": "publisher", "pk": 3, "fields": {"name": "Microsoft Press"}},
  {"model": "publisher", "pk": 4, "fields": {"name": "No starch press"}},
  {"model": "book", "pk": 1, "fields": {"title": "Programming Python, 4th Edition", "id_publisher": 1}},
  {"model": "book", "pk": 2, "fields": {"title": "Learning Python, 4th Edition", "id_publisher": 1}},
  {"model": "book", "pk": 3, "fields": {"title": "Natural Language Processing with Python", "id_publisher": 1}},
  {"model": "book", "pk": 4, "fields": {"title": "Hacking: The Art of Exploitation", "id_publisher": 4}},
  {"model": "book", "pk": 5, "fields": {"title": "Modern Operating Systems", "id_publisher": 2}},
  {"model": "book", "pk": 6, "fields": {"title": "Code Complete: Second Edition", "id_publisher": 3}},
  {"model": "shop", "pk": 1, "fields": {"name": "Labirint"}},
  {"model": "shop", "pk": 2, "fields": {"name": "OZON"}},
  {"model": "shop", "pk": 3, "fields": {"name": "Amazon"}},
  {"model": "stock", "pk": 1, "fields": {"id_shop": 1, "id_book": 1, "count": 34}},
  {"model": "stock", "pk": 2, "fields": {"id_shop": 1, "id_book": 2, "count": 30}},
  {"model": "stock", "pk": 3, "fields": {"id_shop": 1, "id_book": 3, "count": 0}},
  {"model": "stock", "pk": 4, "fields": {"id_shop": 2, "id_book": 5, "count": 40}},
  {"model": "stock", "pk": 5, "fields": {"id_shop": 2, "id_book": 6, "count": 50}},
  {"model": "stock", "pk": 6, "fields": {"id_shop": 3, "id_book": 4, "count": 10}},
  {"model": "stock", "pk": 7, "fields": {"id_shop": 3, "id_book": 6, "count": 10}},
  {"model": "stock", "pk": 8, "fields": {"id_shop": 2, "id_book": 1, "count": 10}},
  {"model": "stock", "pk": 9, "fields": {"id_shop": 3, "id_book": 1, "count": 10}},
  {"model": "sale", "pk": 1, "fields": {"price": "50.05", "date_sale": "2018-10-25T09:45:24.552Z", "count": 16, "id_stock": 1}},
  {"model": "sale", "pk": 2, "fields": {"price": "50.05", "date_sale": "2018-10-25T09:51:04.113Z", "count": 10, "id_stock": 3}},
  {"model": "sale", "pk": 3, "fields": {"price": "10.50", "date_sale": "2018-10-25T09:52:22.194Z", "count": 9, "id_stock": 6}},
  {"model": "sale", "pk": 4, "fields": {"price": "16.00", "date_sale": "2018-10-25T10:59:56.230Z", "count": 5, "id_stock": 5}},
  {"model": "sale", "pk": 5, "fields": {"price": "16.00", "date_sale": "2018-10-25T10:59:56.230Z", "count": 5, "id_stock": 9}},
  {"model": "sale", "pk": 6, "fields": {"price": "16.00", "date_sale": "2018-10-25T10:59:56.230Z", "count": 1, "id_stock": 4}}
]