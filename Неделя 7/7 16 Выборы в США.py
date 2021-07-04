fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt')

myDict = {}

for elem in fin:
    candidate, votes = elem.split()
    
    myDict[candidate] = myDict.get(candidate, 0) + int(votes)
    
for elem in sorted(myDict):
    print(elem, myDict[elem])
    
