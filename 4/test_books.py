from books import *

page = Page('text')
page += 123
print(page)

s = 'string_' + page
print(type(s))
print(s)

new_page = page + '123'
print(f"{id(page)}, {id(new_page)}")

page1 = Page('text')
print(len(page1))
print(page1 > page)

content = [Page('Page {}'.format(str(num))) for num in range(1,10)]
book = Book('my_book', content)
print(len(book))

print(book[1])

book[9] = 'Last page'
print(book[9]) # Last page

book[9] += '\nnew_string'
print(book[9])

print(type(book[9]))

book2 = Book('book2')
print(book2 == book)