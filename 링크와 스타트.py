import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
member_list = [i for i in range(n)]
INF = int(1e10)
res = INF

for i in range(1, int(n / 2 + 1)):
    member_divide = combinations(member_list, i)
    for comb in member_divide:
        start_list = list(comb)
        link_list = list(set(member_list) - set(start_list))
        start_all_sum = 0
        link_all_sum = 0
        for j in range(n - 1):
            for k in range(n - 1):
                try:
                    start_sum = arr[start_list[j]][start_list[k]]
                except IndexError:
                    start_sum = 0

                try:
                    link_sum = arr[link_list[j]][link_list[k]]
                except IndexError:
                    link_sum = 0
                start_all_sum += start_sum
                link_all_sum += link_sum
        res = min(res, abs(start_all_sum - link_all_sum))

print(res)
