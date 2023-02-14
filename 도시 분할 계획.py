import sys

n, m = map(int, sys.stdin.readline().rstrip().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((c, a, b))

edges.sort()

max_cost = 0
min_sum = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        max_cost = max(max_cost, cost)
        min_sum += cost

print(min_sum - max_cost)
