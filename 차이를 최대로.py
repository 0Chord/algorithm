import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
res = -int(1e8)

for permutation in permutations(arr, n):
    calc = 0
    for idx in range(1, len(list(permutation))):
        calc += abs(list(permutation)[idx] - list(permutation)[idx - 1])
    res = max(calc, res)
print(res)
