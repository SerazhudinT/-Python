fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

N = int(fin.readline().split()[0])

Yes = set(range(1, N + 1))

for elem in fin:
    elem = elem.split()
    
    if elem[0] == 'HELP':
        break
    
    arr = list(map(int, elem))

    answer = fin.readline().split()[0]
    
    if answer == 'YES':            
        Yes &= set(arr)
    else:
        Yes -= set(arr)

fin.close()

print(*sorted(list(Yes)))

