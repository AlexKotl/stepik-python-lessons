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

    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author
        self.year = year
        self.bookmark = {}

    def read(self, page):
        """возвращает страницу"""
        pass

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        pass

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        try:
            return self.bookmark[person]
        except:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        pass

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError("Novel cant be modified")


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""
    MAX_SIGN = 2000
    SIZE = 12

    def __init__(self, title, size=None, max_sign=None, content=None):
        super().__init__(title, content)
        self.max_sign = max_sign or self.MAX_SIGN
        self.size = len(content) if content!=None and len(content) > 0 else size
        self.size = self.size or self.SIZE
        if content == None:
            self.content = ['' for _ in range(self.size)]

    def read(self, page):
        """возвращает страницу с номером page"""
        try:
            return self.content[page]
        except IndexError:
            raise PageNotFoundError(page)

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        try:
            if len(text) + self.content[page] > self.max_sign:
                raise TooLongTextError
            self.content[page] += text
        except IndexError:
            raise PageNotFoundError(page)


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        try:
            return book.content[page]
        except IndexError:
            raise PageNotFoundError(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        book.bookmark[self] = page

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        try:
            return book.bookmark[self]
        except IndexError:
            raise PageNotFoundError

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        try:
            del book.bookmark[self]
        except IndexError:
            raise PageNotFoundError
        
# ERRORS

class BookIOErrors(Exception):
    pass
    
class NotExistingExtensionError(BookIOErrors):
    pass

class PermissionDeniedError(BookIOErrors):
    pass
    
class PageNotFoundError(BookIOErrors):
    pass
    
class TooLongTextError(BookIOErrors):
    pass
