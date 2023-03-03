import sys
from collections import deque

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
wolf = 0
goat = 0
visited_arr = [[False] * m for _ in range(n)]
for col in range(n):
    for row in range(m):
        if not visited_arr[col][row] and (arr[col][row] == 'v' or arr[col][row] == 'o'):
            mini_goat = 0
            mini_wolf = 0
            if arr[col][row] == 'o':
                mini_goat += 1
            elif arr[col][row] == 'v':
                mini_wolf += 1
            queue.append([col, row])
            visited_arr[col][row] = True
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited_arr[nx][ny] and arr[nx][ny] != '#':
                        queue.append([nx, ny])
                        visited_arr[nx][ny] = True
                        if arr[nx][ny] == 'o':
                            mini_goat += 1
                        elif arr[nx][ny] == 'v':
                            mini_wolf += 1
            if mini_wolf < mini_goat:
                goat += mini_goat
            else:
                wolf += mini_wolf

print(goat, wolf)
