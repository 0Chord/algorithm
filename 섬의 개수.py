import sys

sys.setrecursionlimit(100000)

direction_arr = [[-1, 1], [0, 1], [1, 1], [1, 0], [-1, 0], [-1, -1], [0, -1], [1, -1]]


def dfs(col, row, visited_graph, arr):
    if col <= -1 or col >= h or row <= -1 or row >= w:
        return
    if arr[col][row] == 0:
        return
    if visited_graph[col][row]:
        return
    visited_graph[col][row] = True
    for el in direction_arr:
        dfs(col + el[0], row + el[1], visited_graph, arr)


while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    count = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))
    visited_arr = [[False for _ in range(w)] for _ in range(h)]

    for column in range(h):
        for row_idx in range(w):
            if not visited_arr[column][row_idx] and graph[column][row_idx] == 1:
                count += 1
                dfs(column, row_idx, visited_arr, graph)
    print(count)
