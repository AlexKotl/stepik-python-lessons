from books import *

class AdvancedPerson(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def search(self, book, name_page):
        return book.search(name_page)

    def read(self, book, page):
        if isinstance(page, int):
            return super().read(book, page)
        else:
            return super().read(book, self.search(book, page))

    def write(self, book, page, text):
        if isinstance(page, int):
            return super().write(book, page, text)
        else:
            return super().write(book, self.search(book, page), text)


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    def __init__(self, author, year, title, content=None, table=None):
        super().__init__(author, year, title, content)
        self.table = table or {}

    def search(self, name_page):
        if name_page not in self.table:
            raise PageNotFoundError
        return self.table[name_page]

    def add_chapter(self, chapter, page):
        return self.table.update({ chapter: page })

    def remove_chapter(self, chapter):
        if chapter not in self.table:
            raise PageNotFoundError
        del self.table[chapter]