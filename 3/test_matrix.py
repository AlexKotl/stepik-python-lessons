from matrix import Matrix
from time import time

start = time()
matrix = Matrix()
for k in range(10):
    matrix.append(k)
end = time()
print(end - start)
quit()

matrix = Matrix()
for i in range(1, 4):
    matrix.append(i)
    print(matrix)
    print('*' * 10)

matrix.pop()
print(matrix)

matrix.append(None)
print(matrix)

matrix = Matrix(max_size=2)
for i in range(1, 5):
    matrix.append(i)
    print(matrix)
    print('#' * 10)
matrix.append(5)

matrix = Matrix.from_iter([1,2,3])
print(matrix)

matrix = Matrix.from_iter(range(3))
print(matrix)

matrix = Matrix.from_iter(range(9), max_size=3)
print(matrix)

matrix = Matrix.from_iter(range(30), max_size=3)

matrix = Matrix.from_iter([None,1,2,None,None,3,None,4,None,None,None], max_size=2)
print(matrix)