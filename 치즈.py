import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
days = 0
copy_arr = []
while True:
    lst = []
    flag = False
    visited_arr = [[False] * M for _ in range(N)]

    queue.append((0, 0))
    visited_arr[0][0] = True
    while queue:
        x, y = queue.popleft()
        visited_arr[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited_arr[nx][ny]:
                if arr[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited_arr[nx][ny] = True
                elif arr[nx][ny] == 1:
                    lst.append((nx, ny))
                    visited_arr[nx][ny] = True
                    flag = True

    if not flag:
        print(days)
        print(len(copy_arr))
        break
    else:
        copy_arr = copy.deepcopy(lst)
        for el in lst:
            arr[el[0]][el[1]] = 0
        days += 1

