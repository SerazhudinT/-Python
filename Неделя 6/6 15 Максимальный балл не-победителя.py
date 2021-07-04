fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

max1 = 3 * [0]
max2 = 3 * [0]

for now in fin:
    grade, mark = map(int, now.split()[-2:])
    
    grade -= 9
    
    if max1[grade] < mark:
        max1[grade], max2[grade] = mark, max1[grade]
    elif max2[grade] < mark and max1[grade] != mark:
        max2[grade] = mark
    
fin.close()

print(*max2)
