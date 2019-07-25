from books import *

class AdvancedPerson(Person):
    def search(book, name_page):
        """возвращает номер страницы name_page из книги book"""

    def read(self, book, page):
        # переопределите метод
        pass

    def write(self, book, page, text):
        # переопределите метод
        pass


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    def __init__(self, title, content=None, table=None):
        # переопределите метод
        pass

    def search(self, name_page):
        # напишите вашу реализацию метода здесь
        pass

    def add_chapter(self, chapter, page):
        # напишите вашу реализацию метода здесь
        pass

    def remove_chapter(self, chapter):
        # напишите вашу реализацию метода здесь
        pass 