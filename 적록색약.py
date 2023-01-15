import sys
sys.setrecursionlimit(100000)

N = int(input().rstrip())
graph = []
visited_graph = [[False for _ in range(N)] for _ in range(N)]

for _ in range(N):
    graph.append(list(input().rstrip()))


def dfs(col, row, color):
    if col <= -1 or col >= N or row <= -1 or row >= N:
        return
    if visited_graph[col][row]:
        return

    if graph[col][row] != color:
        return
    else:
        visited_graph[col][row] = True
        dfs(col + 1, row, color)
        dfs(col - 1, row, color)
        dfs(col, row + 1, color)
        dfs(col, row - 1, color)


count = 0
problem_count = 0
for col_idx in range(N):
    for row_idx in range(N):
        if not visited_graph[col_idx][row_idx]:
            count += 1
            dfs(col_idx, row_idx, graph[col_idx][row_idx])

for col in range(N):
    for row in range(N):
        if graph[col][row] == 'G':
            graph[col][row] = 'R'
visited_graph = [[False for _ in range(N)] for _ in range(N)]

for col_idx in range(N):
    for row_idx in range(N):
        if not visited_graph[col_idx][row_idx]:
            problem_count += 1
            dfs(col_idx, row_idx, graph[col_idx][row_idx])
print(count, problem_count)
