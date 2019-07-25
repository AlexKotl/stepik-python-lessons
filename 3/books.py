class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        if page < 0:
            raise PageNotFoundError('Page should be greater than zero')
        try:
            return self.content[page]
        except:
            raise PageNotFoundError(page)

    def write(self, page, text):
        raise NotImplementedError
        
    def set_bookmark(self, person, page):
        raise NotExistingExtensionError

    def get_bookmark(self, person):
        raise NotExistingExtensionError
        
    def del_bookmark(self, person):
        raise NotExistingExtensionError

class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        super().__init__(title, content)
        self.author = author
        self.year = year
        self.bookmark = {}

    def set_bookmark(self, person, page):
        self.bookmark.update({ person: page })

    def get_bookmark(self, person):
        if person not in self.bookmark:
            raise PageNotFoundError
        return self.bookmark[person]

    def del_bookmark(self, person):
        try:
            self.bookmark[person] # try to throw error if not exists
            self.bookmark.pop(person)
        except IndexError:
            raise PageNotFoundError

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

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if page < 0:
            raise PageNotFoundError('Page should be greater than zero')
        try:
            if len(text) + len(self.content[page]) > self.max_sign:
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
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        return book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        return book.set_bookmark(self, page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        return book.get_bookmark(self)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        return book.del_bookmark(self)
        
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
