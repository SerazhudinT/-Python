fin = open('input.txt')

myDict = {}

for elem in fin:    
    customer, product, number = elem.split()
    
    myDict[(customer, product)] = myDict.get((customer, product), 0) + int(number)
    
name = ''
    
for elem in sorted(myDict):
    if name != elem[0]:
        name = elem[0]
        
        print(name + ':')
        
    print(elem[1], myDict[elem])
    
    
