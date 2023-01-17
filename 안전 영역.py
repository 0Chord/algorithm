import sys

sys.setrecursionlimit(100000)

N = int(input().rstrip())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

max_count = 1


def dfs(x, y, height):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return
    if graph[x][y] <= height:
        return
    if visited_arr[x][y]:
        return

    visited_arr[x][y] = True
    dfs(x + 1, y, height)
    dfs(x - 1, y, height)
    dfs(x, y - 1, height)
    dfs(x, y + 1, height)


for depth in range(1, 101):
    visited_arr = [[False for _ in range(N)] for _ in range(N)]
    count = 0
    for col in range(N):
        for row in range(N):
            if graph[col][row] > depth and not visited_arr[col][row]:
                count += 1
                dfs(col, row, depth)
    max_count = max(max_count, count)

print(max_count)
