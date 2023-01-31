import sys
import itertools

while True:
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    if lst[0] == 0:
        break
    k = lst.pop(0)

    combi_arr = list(itertools.combinations(lst, 6))
    for el in combi_arr:
        print(*el)
    print("")