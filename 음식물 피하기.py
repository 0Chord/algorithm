import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())
trash_arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    trash_arr[x - 1][y - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited_arr = [[False] * m for _ in range(n)]
max_trash = 0
queue = deque()
for col in range(n):
    for row in range(m):
        if trash_arr[col][row] == 1 and not visited_arr[col][row]:
            visited_arr[col][row] = True
            queue.append([col, row])
            trash = 1
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited_arr[nx][ny] and trash_arr[nx][ny] == 1:
                        queue.append([nx, ny])
                        visited_arr[nx][ny] = True
                        trash += 1
            max_trash = max(max_trash, trash)
print(max_trash)
