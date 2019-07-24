class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content):
        self.author = author
        self.year = year
        self.bookmark = {}
        self.title = title
        self.content = content

    def read(self, page):
        """возвращает страницу"""

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        try:
            return self.bookmark[person]
        except:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""

    def write(self, page, text):
        """делает запись текста text на страницу page """


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""
    MAX_SIGN = 2000
    SIZE = 12

    def __init__(self, title, size, max_sign, content):
        self.max_sign = max_sign or self.MAX_SIGN
        self.size = len(content) if len(content) > 0 else self.SIZE

    def read(self, page):
        """возвращает страницу с номером page"""

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""