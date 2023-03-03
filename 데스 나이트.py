import sys
from collections import deque

queue = deque()

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(sys.stdin.readline().rstrip())
r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e10)
visited_arr = [[False] * n for _ in range(n)]
board = [[INF] * n for _ in range(n)]
board[r1][c1] = 0
visited_arr[r1][c1] = True
queue.append([r1, c1])

while queue:
    x, y = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y] + 1:
            board[nx][ny] = min(board[nx][ny], board[x][y] + 1)
            queue.append([nx, ny])

if board[r2][c2] == INF:
    print(-1)
else:
    print(board[r2][c2])
