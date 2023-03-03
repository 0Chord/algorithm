import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[y].append(x)
res = [0] * (n + 1)
queue = deque()
for idx in range(1, n + 1):
    queue.append(idx)
    visited_arr = [False] * (n + 1)
    cnt = 0
    visited_arr[idx] = True
    while queue:
        cnt += 1
        x = queue.popleft()
        for i in graph[x]:
            if not visited_arr[i]:
                visited_arr[i] = True
                queue.append(i)
    res[idx] = cnt
max_num = max(res)
for idx in range(n + 1):
    if max_num == res[idx]:
        print(idx, end=' ')
print()
