import heapq
import sys

INF = int(1e10)

v, e = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, x, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((x, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for idx in range(1, v + 1):
    if distance[idx] == INF:
        print("INF")
    else:
        print(distance[idx])
