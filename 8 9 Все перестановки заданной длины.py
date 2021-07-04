from itertools import permutations

print(*map(lambda x: ''.join(x), permutations(map(str, range(1, int(input()) + 1)))), sep='\n')

