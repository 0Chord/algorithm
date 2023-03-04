import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, x = heapq.heappop(q)
        if cost > distance[x]:
            continue
        for i in graph[x]:
            dist = cost + i[1]
            if dist < distance[i[0]]:
                distance[i[0]] = dist
                heapq.heappush(q, (dist, i[0]))


n, m, r = map(int, sys.stdin.readline().rstrip().split())

item_score = [0]+list(map(int, sys.stdin.readline().rstrip().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(r):
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))
INF = int(1e10)
max_score = 0
for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    score = 0
    for j in range(n + 1):
        if distance[j] <= m:
            score += item_score[j]
    max_score = max(score,max_score)
print(max_score)
