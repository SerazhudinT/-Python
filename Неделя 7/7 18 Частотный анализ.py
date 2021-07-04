fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt')

myDict = {}

for elem in fin:
    elem = elem.split()
    
    for word in elem:
        myDict[word] = myDict.get(word, 0) + 1
        
myList = []

for elem in myDict:
    myList.append((-myDict[elem], elem))

myList.sort()

for elem in myList:
    print(elem[1])

