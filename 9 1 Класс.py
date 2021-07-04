class Matrix:
    def __init__(self, lst):
        self.lst = []
        
        for elem in lst:
            self.lst.append(elem.copy())
    
    def __str__(self):
        string = ''
        
        for elem in self.lst:
            string = '\n'.join([string, '\t'.join(map(str, elem))])
            
        return string[1:]
        
    def size(self):
        return len(self.lst), len(self.lst[0])
