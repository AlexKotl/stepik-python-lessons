class Page:

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign
        
    def __add__(self, obj):
        if len(self._text + obj) > self.max_sign:
            raise TooLongTextError
        self._text += obj
        return self
        
    def __str__(self):
        return self._text
    
    def __hash__(self):
        return hash(self._text)
        
    def __radd__(self, obj):
        return obj + self._text


class Book:

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content
