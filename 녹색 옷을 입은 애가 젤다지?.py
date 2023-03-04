import sys
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e10)
t = 0
while True:
    t += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    dist[0][0] = arr[0][0]

    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + arr[nx][ny]
                if dist[nx][ny] > next_cost:
                    dist[nx][ny] = next_cost
                    heapq.heappush(q, (next_cost, nx, ny))
    print("Problem " + str(t) + ":", dist[-1][-1])
