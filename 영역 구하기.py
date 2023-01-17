import sys

sys.setrecursionlimit(1000000)

M, N, K = map(int, input().rstrip().split())

arr = []
for _ in range(K):
    arr.append(list(map(int, input().rstrip().split())))

graph = [[0 for _ in range(N)] for _ in range(M)]

for el in arr:
    for col in range(M - el[3], M - el[1]):
        for row in range(el[0], el[2]):
            graph[col][row] = 1

x_arr = [-1, 1, 0, 0]
y_arr = [0, 0, -1, 1]


def dfs(x, y):
    global max_width
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return
    if graph[x][y] == 1:
        return
    graph[x][y] = 1
    for idx in range(4):
        dfs(x + x_arr[idx], y + y_arr[idx])


cnt = 0
width_arr = []
for col in range(M):
    for row in range(N):
        if graph[col][row] == 0:
            one_count = 0
            for el in graph:
                for e in el:
                    if e == 1:
                        one_count += 1
            cnt += 1
            dfs(col, row)
            another_one_count = 0
            for el in graph:
                for e in el:
                    if e == 1:
                        if e == 1:
                            another_one_count += 1
            width_arr.append(another_one_count - one_count)

print(cnt)
width_arr.sort()
print(*width_arr)
