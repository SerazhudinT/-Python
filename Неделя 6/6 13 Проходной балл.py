fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

K = int(fin.readline())

competition = []

for now in fin:
    marks = list(map(int, now.split()[-3:]))
    
    if min(marks) < 40:
        continue
        
    competition.append(sum(marks))
    
fin.close()

competition.sort(reverse=True)

if len(competition) <= K:
    print(0)
elif competition[0] == competition[K]:
    print(1)
elif competition[K - 1] == competition[K]:
    print(competition[K - 1 - competition[:K].count(competition[K - 1])])
else:
    print(competition[K - 1])
