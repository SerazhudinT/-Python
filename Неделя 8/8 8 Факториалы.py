import itertools
import operator

print(*itertools.accumulate(range(1, int(input()) + 1), operator.mul, initial=1))
