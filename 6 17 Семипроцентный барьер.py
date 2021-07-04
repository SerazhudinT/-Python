fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

parties = []
now = fin.readline().split()
now = fin.readline().split()

while now[0] != 'VOTES:':
    parties.append(now)
    
    now = fin.readline().split()
    
number = len(parties) * [0]

for now in fin:
    now = now.split()
    
    for i in range(len(parties)):
        if parties[i] == now:
            number[i] += 1
        
fin.close()

for i in range(len(parties)):
    if number[i] / sum(number) >= 0.07:
        print(*parties[i])
