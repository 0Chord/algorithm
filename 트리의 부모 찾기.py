import sys

sys.setrecursionlimit(1000000)

N = int(input().rstrip())

arr = [[] for _ in range(N + 1)]
result = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n, m = map(int, input().rstrip().split())
    arr[n].append(m)
    arr[m].append(n)

visited_arr = [False for _ in range(N + 1)]


def dfs(x, precious):
    if visited_arr[x]:
        return
    visited_arr[x] = True
    if precious != 0:
        result[x].append(precious)
    for el in arr[x]:
        dfs(el, x)


dfs(1, 0)

for idx in range(2,len(result)):
    print(*result[idx])