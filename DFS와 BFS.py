import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
dfs_visited_arr = [False] * (n + 1)

for idx in range(n + 1):
    graph[idx].sort()
dfs_memo = []


def dfs(start):
    if dfs_visited_arr[start]:
        return
    dfs_memo.append(start)
    dfs_visited_arr[start] = True
    for el in graph[start]:
        if not dfs_visited_arr[el]:
            dfs(el)


dfs(v)
bfs_memo = []
bfs_visited_arr = [False] * (n + 1)
queue = deque()
queue.append(v)
bfs_visited_arr[v] = True
while queue:
    x = queue.popleft()
    bfs_memo.append(x)

    for el in graph[x]:
        if not bfs_visited_arr[el]:
            bfs_visited_arr[el] = True
            queue.append(el)

print(*dfs_memo)
print(*bfs_memo)