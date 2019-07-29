from calendar import *
book = CalendarBook('2018')
print(len(book)) # 377

print(book.title) # 2018
print(book[1])
print(book[2])
print(book[32])
print(book[33])
book[0] # PageNotFoundError

print(book.bookmark) # 0
book.bookmark = 7
print(book.bookmark) # 7
del book.bookmark # AttributeError: __delete__
print(book.bookmark) # 7
book[2] += '\nHappy New Year!!!'
print(book[2]) # added string