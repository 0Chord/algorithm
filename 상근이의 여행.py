import sys


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


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parent = [i for i in range(n + 1)]
    edges = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        edges.append([x, y])
    edges.sort()
    cost = 0
    for edge in edges:
        x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            cost += 1
    print(cost)
