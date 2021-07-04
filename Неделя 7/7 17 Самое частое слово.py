fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt')

myDict = {}

for elem in fin:
    elem = elem.split()
    
    for word in elem:
        myDict[word] = myDict.get(word, 0) + 1

maxKey = ''
maxValue = 0

for elem in myDict:
    if maxValue < myDict[elem]:
        maxKey = elem
        maxValue = myDict[elem]
    elif maxValue == myDict[elem]:
        maxKey = min(maxKey, elem)
    
print(maxKey)

