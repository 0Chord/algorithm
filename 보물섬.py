import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_num = 0
queue = deque()
for col in range(N):
    for row in range(M):
        if arr[col][row] == "L":
            visited_arr = [[False] * M for _ in range(N)]
            max_num = 0
            visited_arr[col][row] = True
            queue.append((col, row, 0))
            while queue:
                x, y, cnt = queue.popleft()
                visited_arr[x][y] = True
                flag = False
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited_arr[nx][ny] and arr[nx][ny] == "L":
                        visited_arr[nx][ny] = True
                        queue.append((nx, ny, cnt + 1))
                        flag = True
                if not flag:
                    max_num = max(max_num, cnt)
            min_num = max(min_num, max_num)

print(min_num)

