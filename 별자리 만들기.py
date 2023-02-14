import sys
import math


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline().rstrip())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

arr = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    arr.append((x, y))
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        cost = math.sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
        edges.append((cost, i, j))

cost_sum = 0
edges.sort()
for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        cost_sum += cost
round_cost_sum = round(cost_sum, 2)
print(round_cost_sum)
