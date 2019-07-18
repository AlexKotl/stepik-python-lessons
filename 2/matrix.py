def create_matrix(size):    
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное None).
    :param size: int
    :return: list
    """
    matrix = [[None for x in range(size)] for y in range(size)] 
    return matrix

def extend_matrix(matrix):
    list = []
    for row in matrix:
        for el in row:
            list.append(el)
    
    new = create_matrix(len(matrix) + 1)
    
    for el in list:
        add_element(el, new)
    return new

def add_element(element, matrix):
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: string
    :param matrix: list
    :return: list
    """
    if element == None:
        return matrix
        
    size = len(matrix)
    for x in range(size):
        for y in range(size):
            if matrix[x][y] == None:
                if x == size - 1:
                    new = extend_matrix(matrix)
                    add_element(element, new)
                    return new
                matrix[x][y] = element
                return matrix
    return matrix


def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix
    :param matrix: list
    :return: string
    """
    result = ''
    for x in range(len(matrix)):
        if x > 0:
            result += '\n'
        for y in range(len(matrix)):
            if (y > 0):
                result += ' '
            result += str(matrix[x][y])
    return result
    
sample = create_matrix(3)
sample = add_element(1, sample)
sample = add_element(2, sample)
sample = add_element(3, sample)
sample = add_element(4, sample)
sample = add_element(5, sample)
sample = add_element(6, sample)
print(matrix_to_string(sample))
sample = add_element(7, sample)
print(matrix_to_string(sample))
