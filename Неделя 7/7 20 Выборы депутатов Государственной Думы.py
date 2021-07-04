def sumVotes(arr):
    total = 0

    for elem in arr:
        total += int(elem[1])

    return total


fin = open('input.txt')

myList = []
i = 0

for elem in fin:
    elem = elem.split()

    myList.append([' '.join(elem[:-1]), int(elem[-1]), i])

    i += 1

PICH = sumVotes(myList) / 450

for elem in myList:
    elem[1] /= PICH

if sumVotes(myList) < 450:
    myList.sort(reverse=True, key=lambda x: x[1] - int(x[1]))

    for elem in myList:
        elem[1] += 1

        if sumVotes(myList) >= 450:
            break

for elem in sorted(myList, key=lambda x: x[2]):
    print(elem[0], int(elem[1]))
