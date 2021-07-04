def level(tree, parent):
    for elem in tree[parent][0]:
        tree[elem][2] = tree[parent][2] + 1

        level(tree, elem)


fin = open('input.txt')

N = int(fin.readline())

tree = {}

for i in range(N - 1):
    child, parent = fin.readline().split()

    if tree.get(child) is None:
        tree[child] = [[], '', 0]

    tree[child][1] = parent

    if tree.get(parent) is None:
        tree[parent] = [[], '', 0]

    tree[parent][0].append(child)

for elem in tree:
    if tree[elem][1] == '':
        level(tree, elem)
        
        break

for elem in sorted(tree):
    print(elem, tree[elem][2])
