from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
visited_arr = [[False] * m for _ in range(n)]
max_draw = 0
cnt = 0
for col in range(n):
    for row in range(m):
        if arr[col][row] == 1 and not visited_arr[col][row]:
            cnt += 1
            queue.append([col, row])
            visited_arr[col][row] = True
            draw = 1
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited_arr[nx][ny] and arr[nx][ny] == 1:
                        draw += 1
                        visited_arr[nx][ny] = True
                        queue.append([nx, ny])
            max_draw = max(draw, max_draw)
print(cnt)
print(max_draw)