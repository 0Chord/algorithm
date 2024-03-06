import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
min_num = 10000000000000
result = 0
for el in combinations(numbers, 3):
    cnt = sum(el)
    if cnt <= m and m - cnt < min_num:
        result = cnt
        min_num = m - cnt
print(result)
