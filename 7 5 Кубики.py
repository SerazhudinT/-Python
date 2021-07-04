fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

N, M = map(int, fin.readline().split())

A = set()
B = set()

for i in range(N):
    A.add(int(fin.readline().split()[0]))
    
for i in range(M):
    B.add(int(fin.readline().split()[0]))

fin.close()

answer = [A & B, A - (A & B), B - (A & B)]

for elem in answer:
    print(len(elem))
    print(*sorted(list(elem)))

