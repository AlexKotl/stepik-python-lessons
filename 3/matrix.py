from collections import Iterable

class Matrix:
    MAX_SIZE = 1000  

    def __init__(self, max_size=None):
        self.matrix = [None]
        self.MAX_SIZE = max_size or self.MAX_SIZE
        
    def __create_matrix(self, size):    
        matrix = [None for x in range(size ** 2)] 
        return matrix

    def append(self, element=None):
        if element is None:
            return self.matrix
        
        index = self.matrix.index(None)

        self.matrix[index] = element
        size = int(len(self.matrix) ** 0.5)
        if index == size * (size - 1):
            self.matrix.extend([None] * ((size + 1) ** 2 - len(self.matrix)))
        
        return self.matrix

    def pop(self):
        size = len(self.matrix)
        if size == 1 and self.matrix[0] == None:
            raise IndexError("Matrix has no elements")
        
        index = self.matrix.index(None) - 1
        found_el = self.matrix[index]
        self.matrix[index] = None
        size = int(len(self.matrix) ** 0.5)
        if index + (size - 1) <= (size - 1)**2: 
            self.matrix = self.matrix[:-(size**2 - (size-1)**2)]
        return found_el

    def __str__(self):
        result = ''
        size = int(len(self.matrix) ** 0.5)
        for row in range(size):
            result += ' '.join([str(i) for i in self.matrix[size * row : size * (row + 1)]]) + '\n'
        return result

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        if not isinstance(iter_obj, Iterable):
            raise TypeError("Object not iterable. {} given".format(type(iter_obj)))
        
        matrix = cls(max_size)   
        for el in iter_obj:
            matrix.append(el)
        return matrix
        