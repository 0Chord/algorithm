import sys
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

queue = deque()
days = 0
visited_arr = [[False] * m for _ in range(n)]
res_arr = []
for col in range(n):
    for row in range(m):
        if arr[col][row] == 1:
            res_arr.append([col, row])
while True:
    tomato_lst = []
    for el in res_arr:
        col, row = el[0], el[1]
        if arr[col][row] == 1 and not visited_arr[col][row]:
            queue.append([col, row])
            visited_arr[col][row] = True
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] == 0:
                            tomato_lst.append([nx, ny])
                        elif arr[nx][ny] == 1 and not visited_arr[nx][ny]:
                            visited_arr[nx][ny] = True
                            queue.append([nx, ny])

    if len(tomato_lst) > 0:
        days += 1
        for el in tomato_lst:
            arr[el[0]][el[1]] = 1
        res_arr = copy.deepcopy(tomato_lst)
    else:
        flag = True
        for el in arr:
            if 0 in el:
                flag = False
        if flag:
            print(days)
            break
        else:
            print(-1)
            break
