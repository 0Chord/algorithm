import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
s = set()
for idx in range(1, n + 1):
    combination = combinations(arr, idx)
    for combi in combination:
        calc = 0
        for el in combi:
            calc += el
        s.add(calc)
lst = [0] + list(s)
lst.sort()
search_num = 1

while True:
    if search_num >= len(lst):
        print(search_num)
        break
    elif search_num != lst[search_num]:
        print(search_num)
        break
    elif search_num == lst[search_num]:
        search_num += 1
