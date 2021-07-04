class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
    
    
class Matrix:
    def __init__(self, lst):
        self.matrix = [string.copy() for string in lst ]
    
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, string)) for string in self.matrix])
        
    def size(self):
        return len(self.matrix), len(self.matrix[0])
    
    def __add__(self, other):
        if self.size() == other.size():
            newMatrix = []

            for i in range(len(self.matrix)):
                newString = []

                for j in range(len(self.matrix[0])):
                    newString.append(self.matrix[i][j] + other.matrix[i][j])

                newMatrix.append(newString)

            return Matrix(newMatrix)
        else:
            raise MatrixError(self, other)
    
    def  __mul__(self, scalar):
        newMatrix = []
        
        for string in self.matrix:
            newMatrix.append([scalar * elem for elem in string])
            
        return Matrix(newMatrix)
    
    __rmul__ = __mul__
    
    def transpose(self):
        self.matrix = list(map(list, zip(*self.matrix)))
        
        return self
        
    def transposed(self):
        return Matrix(list(map(list, zip(*self.matrix))))
