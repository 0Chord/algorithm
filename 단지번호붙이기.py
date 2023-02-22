import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
queue = deque()
sum_count = 0
res = []
for col in range(n):
    for row in range(n):
        if arr[col][row] == 1 and not visited[col][row]:
            queue.append([col, row])
            sum_count += 1
            visited[col][row] = True
            cnt = 1
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
                        cnt += 1
                        visited[nx][ny] = True
                        queue.append([nx, ny])

            res.append(cnt)
print(sum_count)
res.sort()
for el in res:
    print(el)
