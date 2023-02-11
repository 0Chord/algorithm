import sys
import heapq

INF = int(1e10)
n, m, c = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, z))


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


dijkstra(c)
city_cnt = 0
max_time = 0
for idx in range(1, n + 1):
    if distance[idx] != INF and distance[idx] != 0:
        city_cnt += 1
        max_time = max(max_time, distance[idx])
print(city_cnt, max_time)
