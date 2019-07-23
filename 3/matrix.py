class Matrix:
    MAX_SIZE = 1000  

    def __init__(self, max_size=None):
        self.matrix = [[None]]
        self.MAX_SIZE = max_size or self.MAX_SIZE
        
    def __extend_matrix(self, reduce=False):
        list = []
        for row in self.matrix:
            for el in row:
                list.append(el)
        
        self.matrix = self.__create_matrix(len(self.matrix) + (1 if not reduce else -1))
        
        for el in list:
            self.append(el)
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
                    if x == size - 1:
                        self.__extend_matrix()
                        self.append(element)
                        return self.matrix
                    self.matrix[x][y] = element
                    return self.matrix
        return matrix

    def pop(self):
        size = len(self.matrix)
        if size == 1 and self.matrix[0][0] == None:
            raise IndexError("Matrix has no elements")
        
        for x in range(size - 1, -1, -1):
            for y in range(size - 1, -1, -1):
                if self.matrix[x][y] != None:
                    
                    el = self.matrix[x][y]
                    self.matrix[x][y] = None
                    
                    # check if we need to reduce
                    sum = 0
                    for el in self.matrix[size - 1]:
                        sum += el if el != None else 0
                    if sum == 0: 
                        self.__extend_matrix(True)
                    return el

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
        pass