fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt')

myDict = {}
myList = []

for elem in fin:
    elem = elem.split()
    
    for word in elem:
        myList.append(myDict.get(word, 0))
        
        myDict[word] = myDict.get(word, 0) + 1
        
print(*myList)

