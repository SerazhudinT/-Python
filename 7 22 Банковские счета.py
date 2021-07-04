fin = open('input.txt')

myDict = {}

for elem in fin:
    elem = elem.split()

    if elem[0] == 'DEPOSIT':
        myDict[elem[1]] = myDict.get(elem[1], 0) + int(elem[2])
    elif elem[0] == 'WITHDRAW':
        myDict[elem[1]] = myDict.get(elem[1], 0) - int(elem[2])
    elif elem[0] == 'TRANSFER':
        myDict[elem[1]] = myDict.get(elem[1], 0) - int(elem[3])
        myDict[elem[2]] = myDict.get(elem[2], 0) + int(elem[3])
    elif elem[0] == 'INCOME':
        for customer in myDict:
            if myDict[customer] > 0:
                myDict[customer] += int(myDict[customer] * int(elem[1]) / 100)
    elif elem[0] == 'BALANCE':
        if myDict.get(elem[1]) is not None:
            print(myDict[elem[1]])
        else:
            print('ERROR')
