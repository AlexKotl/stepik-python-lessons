from books import *

person = Person('Igor')
print(person.name)

from string import ascii_lowercase as alphabet
content = [sign for sign in alphabet]
notebook = Notebook('note', 24, 100, content)
print(notebook.title)
print(notebook.max_sign)
print(notebook.content)
