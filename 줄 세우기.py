from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    indegree[y] += 1

visited_arr = [False] * (n + 1)


def dfs(idx, arr):
    visited_arr[idx] = True
    arr.append(idx)

    for i in graph[idx]:
        if not visited_arr[i]:
            visited_arr[i] = True
            dfs(i, arr)


result = []


def topology_sort(arr):
    q = deque()
    for el in arr:
        if indegree[el] == 0:
            q.append(el)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


for j in range(1, n + 1):
    if not visited_arr[j]:
        dfs_arr = []
        dfs(j, dfs_arr)
        topology_sort(dfs_arr)

print(*result)