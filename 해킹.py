import sys
import heapq

t = int(sys.stdin.readline().rstrip())


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
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().rstrip().split())

    start = c
    INF = int(1e10)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        graph[b].append((a, s))
    dijkstra(start)
    cnt = 0
    cost = 0
    for el in distance:
        if el != INF:
            cost = max(cost, el)
            cnt += 1
    print(cnt, cost)
