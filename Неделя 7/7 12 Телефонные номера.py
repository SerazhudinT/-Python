fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt')

numbers = fin.readlines()

for i in range(4):
    numbers[i] = ''.join(''.join(''.join(numbers[i].strip('+\n').split('-')).split('(')).split(')'))
    
    if len(numbers[i]) == 11:
        numbers[i] = numbers[i][1:]
        
        if numbers[i][:3] == '495':
            numbers[i] = numbers[i][3:]

for i in range(1, 4):
    if numbers[i] == numbers[0]:
        print('YES')
    else:
        print('NO')

