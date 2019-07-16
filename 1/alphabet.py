source = input()
source = sorted(source.lower())
result = ''

for letter in source:
    if not letter.isalpha():
        continue
        
    if letter not in result:
        result += letter
        
print(result)