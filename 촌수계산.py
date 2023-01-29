import sys

n = int(sys.stdin.readline().rstrip())
x, y = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    arr[first].append(second)
    arr[second].append(first)
visited_arr = [-1 for _ in range(n + 1)]


def dfs(idx, count):
    if visited_arr[idx] != -1:
        return

    visited_arr[idx] = count
    for el in arr[idx]:
        dfs(el, count + 1)


dfs(x, 0)
print(visited_arr[y])
