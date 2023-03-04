import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
INF = int(1e10)
distance = [INF] * (n + 1)

distance[1] = 0
distance[0] = -1
queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if distance[i] > distance[x] + 1:
            distance[i] = distance[x] + 1
            queue.append(i)

i = int(1e10)
max_distance = max(distance)
cnt = 0
for idx in range(len(distance)):
    if distance[idx] == max_distance:
        cnt += 1
        if i > idx:
            i = idx
print(i, max_distance, cnt)