from books import *

page = Page('text')
page += '_new_text'
print(page)

s = 'string_' + page
print(type(s))
print(s)

# new_page = page + 123

new_page = page + '123'
print(id(page) == id(new_page))