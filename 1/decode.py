alphabet = 'abcdefghijklmnopqrstuvwxyz'

str = input().lower()
code = input().lower()
result = ''

for letter in str:
    if not letter.isalpha():
        result += letter
        continue
        
    pos = code.index(letter)
    result += alphabet[pos]
    
print(result)