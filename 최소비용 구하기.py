import sys
import heapq

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
INF = int(1e10)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, c = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, c))

start, end = map(int, sys.stdin.readline().rstrip().split())
distance = [INF] * (N + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            if i[1] + dist < distance[i[0]]:
                cost = i[1] + dist
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])
