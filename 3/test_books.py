from books import *

person = Person('Igor')
print(person.name)

from string import ascii_lowercase as alphabet
content = [sign for sign in alphabet]
notebook = Notebook('note', 24, 100, content)
print(notebook.title)
print(notebook.max_sign)
print(notebook.size)
print(notebook.content)

novel = Novel('Grin', 1925, 'Gold chain')
print(novel.size)
print(novel.author)
print(novel.year)
print(novel.title)
print(person.read(notebook, 10))
person.write(notebook, 10, '+new_value')
print(person.read(notebook, 10))
#print(person.read(notebook, 100))

too_long_text = alphabet * 1000
#person.write(notebook, 0, too_long_text)

novel = Novel('Grin', 1925, 'Gold chain', content)
# person.write(novel, 10, 'new_value')

person.set_bookmark(novel, 10)
print(person.get_bookmark(novel))
person.del_bookmark(novel)
print(person.get_bookmark(novel))
