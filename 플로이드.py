import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
INF = int(1e10)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for idx in range(1, n + 1):
    graph[idx][idx] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for col in range(1, n + 1):
    for row in range(1, n + 1):
        if graph[col][row] == INF:
            graph[col][row] = 0
        print(graph[col][row], end=" ")
    print()
