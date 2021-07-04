fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

candidates = {}

for elem in fin:
    elem = elem.strip()

    candidates[elem] = candidates.get(elem, 0) + 1

myList = []
allVotes = 0

for elem in candidates:
    myList.append((candidates[elem], elem))

    allVotes += candidates[elem]

myList.sort(reverse=True)

print(myList[0][1], file=fout)

if myList[0][0] / allVotes <= 1 / 2:
    print(myList[1][1], file=fout)

fout.close()
