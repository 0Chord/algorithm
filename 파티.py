import sys
import heapq

n, m, x = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e10)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


max_distance = 0
for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dist_cost = 0
    dijkstra(i)
    dist_cost += distance[x]
    distance = [INF] * (n + 1)
    dijkstra(x)
    dist_cost += distance[i]
    max_distance = max(max_distance, dist_cost)

print(max_distance)
