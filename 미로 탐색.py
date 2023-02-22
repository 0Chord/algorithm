import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

start = [0, 0]
INF = int(1e8)
queue = deque()
visited_arr = [[INF] * m for _ in range(n)]
visited_arr[start[0]][start[1]] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue.append([start[0], start[1]])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited_arr[nx][ny] > visited_arr[x][y] + 1 and arr[nx][ny] == 1:
            visited_arr[nx][ny] = visited_arr[x][y] + 1
            queue.append([nx, ny])
print(visited_arr[-1][-1])
