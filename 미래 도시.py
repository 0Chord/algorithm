import sys

INF = int(1e10)
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
x, k = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for el in arr:
    x, y = el
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
