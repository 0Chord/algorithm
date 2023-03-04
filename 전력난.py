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


while True:
    m, n = map(int, sys.stdin.readline().rstrip().split())
    if m == 0 and n == 0:
        break

    edges = []
    parent = [i for i in range(m)]
    all_cost = 0
    for _ in range(n):
        a, b, cost = map(int, sys.stdin.readline().rstrip().split())
        all_cost += cost
        edges.append((cost, a, b))
        edges.append((cost, b, a))
    edges.sort()
    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(all_cost - result)
