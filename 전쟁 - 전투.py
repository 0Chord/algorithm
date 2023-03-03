import sys
from collections import deque

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

b_power = 0
w_power = 0
visited_arr = [[False] * m for _ in range(n)]
for col in range(n):
    for row in range(m):
        if arr[col][row] == 'W' and not visited_arr[col][row]:
            mini_w = 1
            visited_arr[col][row] = True
            queue.append([col, row])
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited_arr[nx][ny] and arr[nx][ny] == 'W':
                        mini_w += 1
                        visited_arr[nx][ny] = True
                        queue.append([nx, ny])
            w_power += pow(mini_w, 2)
        if arr[col][row] == 'B' and not visited_arr[col][row]:
            mini_b = 1
            visited_arr[col][row] = True
            queue.append([col, row])
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited_arr[nx][ny] and arr[nx][ny] == 'B':
                        mini_b += 1
                        visited_arr[nx][ny] = True
                        queue.append([nx, ny])
            b_power += pow(mini_b, 2)
print(w_power, b_power)
