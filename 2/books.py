# def append_book(book, year, catalog={}):
#     if type(book) == str and type(year) == int:
#         catalog[book] = year
#         return catalog
# 
# Вариант кода 2
# def append_book(book, year, catalog=None):
#     catalog = catalog or {}
#     if isinstance(book, str) and isinstance(year, int):
#         catalog.update({book: year})
#         return catalog
#     return catalog

# # Вариант кода 3
# def append_book(book, year, catalog=None):
#     if catalog is None:
#         catalog = {}
#     if type(book) == str and type(year) == int:
#         catalog.update({book: year})
#         return catalog

# # Вариант кода 4
# def append_book(book, year, catalog=None):
#     if catalog is None:
#         catalog = dict()
#     if isinstance(book, str) and isinstance(year, int):
#         catalog.update({book: year})
#         return catalog
# 
# # Вариант кода 5
# def append_book(book, year, catalog={}):
#     if isinstance(book, str) and isinstance(year, int):
#         catalog[book] = year
#         return catalog
#     return catalog
# 
# # Вариант кода 6
# def append_book(book, year, catalog=None):
#     if catalog is None:
#         catalog = dict()
#     if type(book) == str and type(year) == int:
#         catalog = catalog.fromkeys((book, year))
#         return catalog
#     return catalog
# 
# Вариант кода 7
# def append_book(book, year, catalog={}):
#     catalog = catalog if catalog else {}
#     if isinstance(book, str) and isinstance(year, int):
#         catalog[book] = year
#         return catalog
#     return catalog

# создаем словарь для Льва Толстого
tolstoy_books = append_book('War and Peace', 1867)
# добавляем книгу
tolstoy_books = append_book('Anna Karenina', 1873, tolstoy_books)
# полученный словарь
# {'War and Peace': 1868, 'Anna Karenina': 1873}
print(tolstoy_books)