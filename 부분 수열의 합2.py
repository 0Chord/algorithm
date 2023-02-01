import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


def get_num(lst, find):
    return bisect_right(lst, find) - bisect_left(lst, find)


def get_sum(lst, sum_arr):
    for i in range(1, len(lst) + 1):
        for a in combinations(lst, i):
            sum_arr.append(sum(a))
    sum_arr.sort()


left, right = arr[:N // 2], arr[N // 2:]
left_sum, right_sum = [], []

get_sum(left, left_sum)
get_sum(right, right_sum)
ans = 0

for l in left_sum:
    find = S - l
    ans += get_num(right_sum, find)

ans += get_num(left_sum, S)
ans += get_num(right_sum, S)

print(ans)
