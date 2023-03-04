import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline().rstrip())

arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
INF = int(1e10)
wall_arr = [[INF] * n for _ in range(n)]
wall_arr[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append([0, 0])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0 and wall_arr[x][y] + 1 < wall_arr[nx][ny]:
                wall_arr[nx][ny] = wall_arr[x][y] + 1
                queue.append([nx, ny])
            if arr[nx][ny] == 1 and wall_arr[nx][ny] > wall_arr[x][y]:
                wall_arr[nx][ny] = wall_arr[x][y]
                queue.append([nx, ny])
print(wall_arr[-1][-1])
