source = input()
search = input()

source = source.lower()
search = search.lower()
processed = ''

for letter in search:
    occurances = ''
    
    if letter in processed or not letter.isalpha():
        continue
        
    processed += letter
    n = 0
    for l in source:
        n += 1
        if l == letter:
            occurances += ' ' + str(n)
            
    if occurances == '':
        occurances = ' None'
    
    print(letter + occurances)
