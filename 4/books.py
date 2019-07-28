class Page:

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign


class Book:

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content
