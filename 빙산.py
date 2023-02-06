import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
time = 0

check_arr = []
queue = deque()
while True:
    count = 0
    visited_arr = [[False] * M for _ in range(N)]
    count_arr = [[0 for _ in range(M)] for _ in range(N)]
    for col in range(N):
        for row in range(M):
            if not visited_arr[col][row] and arr[col][row] != 0:
                queue.append([col, row])
                count += 1
                visited_arr[col][row] = True
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and not visited_arr[nx][ny] and arr[nx][ny] > 0:
                            queue.append([nx, ny])
                            visited_arr[nx][ny] = True
                        elif 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                            count_arr[x][y] += 1

    for col in range(N):
        for row in range(M):
            arr[col][row] -= count_arr[col][row]
            if arr[col][row] < 0:
                arr[col][row] = 0

    if count == 0:
        print(0)
        break
    elif count > 1:
        print(time)
        break

    time += 1
