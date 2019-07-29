class Page:

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign
        
    def __add__(self, obj):
        if len(self._text + obj) > self.max_sign:
            raise TooLongTextError
        self._text += obj
        return self
        
    # def __iadd__(self, other):
    #     return self.__add__(other)
        
    def __str__(self):
        return str(self._text)
    
    def __hash__(self):
        return hash(self._text)
        
    def __radd__(self, obj):
        return obj + self._text
        
    def __len__(self):
        return len(self._text)
        
    def __lt__(self, other):
        return len(self) < len(other)
        
    def __le__(self, other):
        return len(self) <= len(other)
        
    def __gt__(self, other):
        return len(self) > len(other)
        
    def __ge__(self, other):
        return len(self) >= len(other)


class Book:

    def __init__(self, title, content=None):
        self.title = title
        self._content = content or []
        
    def __len__(self):
        return len(self._content)
        
    def __getitem__(self, index):
        if index > len(self._content):
            raise PageNotFoundError
        return self._content[index - 1]
    
    def __setitem__(self, index, value):
        #print(f"setting value {type(value)}")
        if isinstance(value, Page):
            self._content[index - 1] = value
        else:
            self._content[index - 1] = Page(value)
        


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

