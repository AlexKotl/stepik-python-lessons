import calendar

class Book:

    def __init__(self, title, content=None):
        self.title = title
        self._content = content or []
        bookmark = CalendarBookmark()
        
    def __len__(self):
        return len(self._content)
        
    def __getitem__(self, index):
        if index > len(self._content) or index < 1:
            raise PageNotFoundError
        return self._content[index - 1]
    
    def __setitem__(self, index, value):
        if index > len(self._content) or index < 1:
            raise PageNotFoundError
            
        if isinstance(value, Page):
            self._content[index - 1] = value
        else:
            self._content[index - 1] = Page(value)
            
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return len(self) == len(other)
        
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return len(self) < len(other)
        
    def __le__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return len(self) <= len(other)
        
    def __gt__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return len(self) > len(other)
        
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        return len(self) >= len(other)  
        
class Page:

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign
        
    def __add__(self, obj):
        if not isinstance(obj, str):
            raise TypeError
            
        if len(self._text + obj) > self.max_sign:
            raise TooLongTextError
        self._text += obj
        return self

    def __str__(self):
        return str(self._text)
    
    def __hash__(self):
        return hash(self._text)
        
    def __radd__(self, obj):
        return obj + self._text
        
    def __len__(self):
        return len(self._text)
        
    def __eq__(self, other):
        return len(self) == len(other)
        
    def __lt__(self, other):
        return len(self) < len(other)
        
    def __le__(self, other):
        return len(self) <= len(other)
        
    def __gt__(self, other):
        return len(self) > len(other)
        
    def __ge__(self, other):
        return len(self) >= len(other)

class CalendarBookmark:
    def __init__(self):
        self.bookmark = 0
    
    def __get__(self, obj, obj_type):
        return self.bookmark
        
    def __set__(self, obj, value):
        self.bookmark = value

class CalendarBook(Book):
    bookmark = CalendarBookmark()
    
    def __init__(self, title, content=None):
        super().__init__(title, content)
        
        
        year = int(title)
        tc = calendar.TextCalendar()
        for month in range(1,13):
            self._content.append(tc.formatmonth(year, month))
            for day in tc.itermonthdates(year, month):
                if day.month != month:
                    continue
                self._content.append(str(day))
        
        

        
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