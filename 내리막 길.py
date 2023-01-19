M, N = map(int, input().rstrip().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().rstrip().split())))

memo = [[-1 for _ in range(N)] for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if memo[x][y] != -1:
        return memo[x][y]
    memo[x][y] = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                memo[x][y] += dfs(nx, ny)
    return memo[x][y]


print(dfs(0, 0))
