N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(M)]

visited = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]

for lst in arr:
    graph[lst[0]].append(lst[1])
    graph[lst[1]].append(lst[0])


def dfs(idx):
    visited[idx] = True
    for el in graph[idx]:
        if not visited[el]:
            dfs(el)


count = 0

for vertex in range(1, N + 1):
    if not visited[vertex] and len(graph[vertex]) != 0:
        count += 1
        dfs(vertex)

    if len(graph[vertex]) == 0:
        count += 1
print(count)
