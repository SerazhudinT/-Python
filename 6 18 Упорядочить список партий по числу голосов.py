fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

parties = []
now = fin.readline().split()
now = fin.readline().split()

while now[0] != 'VOTES:':
    parties.append([0, 0, ' '.join(now)])
    
    now = fin.readline().split()

for now in fin:
    now = ' '.join(now.split())
    
    for i in range(len(parties)):
        if parties[i][2] == now:
            parties[i][0] += 1
        
fin.close()

parties.sort()

for i in range(1, len(parties)):
    if parties[i - 1][0] == parties[i][0]:
        parties[i][1] = parties[i - 1][1] - 1

parties.sort(reverse=True, key=lambda tup: tup[0:2])

for elem in parties:
    print(elem[2])
