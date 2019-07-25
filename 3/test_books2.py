from books_advanced import *
person  = AdvancedPerson('Ivan')

from string import ascii_lowercase as alphabet
content = [sign for sign in alphabet]
table = {'start_page': 0}
novel = NovelWithTable('Grin', 1925, 'Gold chain', content, table)
print(novel.table)
print(person.search(novel, 'start_page'))
print(person.search(novel, 'non-exist_page'))