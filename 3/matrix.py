from collections import Iterable

class Matrix:
    MAX_SIZE = 1000  

    def __init__(self, max_size=None):
        self.matrix = [[None]]
        self.MAX_SIZE = max_size or self.MAX_SIZE
        
    def __extend_matrix(self, reduce=False):
        list = []
        for row in self.matrix:
            for el in row:
                if el != None:
                    list.append(el)
        
        new_size = len(self.matrix) + (1 if not reduce else -1)
        self.matrix = self.__create_matrix(new_size)
            
        for x in range(new_size):
            for y in range(new_size):
                if len(list) == 0:
                    return
                
                el = list.pop(0)
                self.matrix[x][y] = el

        return self.matrix
        
    def __create_matrix(self, size):    
        matrix = [[None for x in range(size)] for y in range(size)] 
        return matrix

    def append(self, element=None):
        if element == None:
            return self.matrix
            
        size = len(self.matrix)
        for x in range(size):
            for y in range(size):
                if self.matrix[x][y] == None:
                    if x == size - 1 and size < self.MAX_SIZE:
                        self.__extend_matrix()
                        self.append(element)
                        return self.matrix
                    self.matrix[x][y] = element
                    return self.matrix

        raise IndexError("Matrix is full")

    def pop(self):
        size = len(self.matrix)
        if size == 1 and self.matrix[0][0] == None:
            raise IndexError("Matrix has no elements")
        
        for x in range(size - 1, -1, -1):
            for y in range(size - 1, -1, -1):
                if self.matrix[x][y] != None:
                    
                    found = self.matrix[x][y]
                    self.matrix[x][y] = None
                    
                    # check if we need to reduce
                    el_count = 0
                    for x in range(size):
                        for y in range(size):
                            if self.matrix[x][y] != None:
                                el_count += 1
                    
                    if el_count + (size - 1) <= (size - 1)**2: 
                        self.__extend_matrix(True)
                    return found

    def __str__(self):
        result = ''
        for x in range(len(self.matrix)):
            if x > 0:
                result += '\n'
            for y in range(len(self.matrix)):
                if (y > 0):
                    result += ' '
                result += str(self.matrix[x][y])
        return result

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        if not isinstance(iter_obj, Iterable):
            raise TypeError("Object not iterable. {} given".format(type(iter_obj)))
        
        matrix = cls(max_size)   
        for el in iter_obj:
            matrix.append(el)
        return matrix
        