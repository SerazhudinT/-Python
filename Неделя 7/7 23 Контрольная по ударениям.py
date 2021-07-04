def letterCount(word):
    number = 0
    
    for letter in word:
        if letter.isupper():
            number += 1
            
    return number

fin = open('input.txt')

N = int(fin.readline())

Dict = {}
DictLower = {}

for i in range(N):
    elem = fin.readline().strip()
    
    Dict[elem] = 0
    DictLower[elem.lower()] = 0

Petya = fin.readline().split()

errorNumber = 0

for elem in Petya:
    ElemLower = elem.lower()
    
    if DictLower.get(ElemLower) is None and letterCount(elem) != 1 or DictLower.get(ElemLower) is not None and Dict.get(elem) is None:
        errorNumber += 1

print(errorNumber)

