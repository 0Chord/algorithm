import sys
from collections import deque

sys.setrecursionlimit(int(1e9))
f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())

visited_arr = [1e9 for _ in range(f + 1)]


def dfs(floor, count):
    queue = deque([floor])
    visited_arr[floor] = count
    while queue:
        v = queue.popleft()
        if v == g:
            return
        for i in (v - d, v + u):

            if 0 < i <= f and visited_arr[i] == 1e9:
                visited_arr[i] = visited_arr[v] + 1
                queue.append(i)


dfs(s, 0)
if visited_arr[g] == 1e9:
    print("use the stairs")
else:
    print(visited_arr[g])
