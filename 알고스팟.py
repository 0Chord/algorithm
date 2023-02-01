import sys
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

q = collections.deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(dist[-1][-1])
