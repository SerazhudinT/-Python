fin = open('input.txt', 'r', encoding='utf8')

schools = 100 * [0]

for now in fin:
    schoolNumber = int(now.split()[-2])

    schools[schoolNumber] += 1

fin.close()

maxNumber = max(schools)

for i in range(1, 100):
    if schools[i] == maxNumber:
        print(i, end=' ')
