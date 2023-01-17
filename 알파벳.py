import sys
import copy

sys.setrecursionlimit(100000)

R, C = map(int, input().rstrip().split())

graph = []
for _ in range(R):
    graph.append(list(input().rstrip()))

max_length = 0

dict_x_arr = [-1, 1, 0, 0]
dict_y_arr = [0, 0, -1, 1]


def dfs(x, y, count):
    global max_length
    print(visited_arr)
    if x <= -1 or x >= R or y <= -1 or y >= C:
        max_length = max(max_length, count)
        return
    if visited_arr[ord(graph[x][y]) - 65]:
        max_length = max(max_length, count)
        return
    for idx in range(4):
        visited_arr[ord(graph[x][y])-65] = True
        dfs(x + dict_x_arr[idx], y + dict_y_arr[idx], count + 1)
        visited_arr[ord(graph[x][y])-65] = False


visited_arr = [False for _ in range(26)]

dfs(0, 0, 0)

print(max_length)
