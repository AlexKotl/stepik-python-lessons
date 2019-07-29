class Page:

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign
        
    def __add__(self, obj):
        print("obj is instance of Page: {}".format(isinstance(obj, Page)))
        new_text = self._text + obj
        if len(new_text) > self.max_sign:
            raise TooLongTextError
        self._text = new_text
        return self
        
    def __str__(self):
        return self._text
    
    def __hash__(self):
        return hash(self._text)


class Book:

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content
