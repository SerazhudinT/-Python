fin = open('input.txt', 'r', encoding='utf-8')

score = 3 * [0]
n = 3 * [0]

for now in fin:
    grade, mark = map(int, now.split()[2:])

    score[grade - 9] += mark
    n[grade - 9] += 1

print(score[0] / n[0], score[1] / n[1], score[2] / n[2])
