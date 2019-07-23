import matrix

matrix = matrix.Matrix()
for i in range(1, 4):
    matrix.append(i)
    print(matrix)
    print('*' * 10)
    
matrix.pop()
print(matrix)