fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

all = []

for now in fin:
    surname, name, school, mark = now.split()

    all.append(' '.join([surname, name, mark]))

all.sort()

for now in all:
    print(now, file=fout)

fin.close()
fout.close()
