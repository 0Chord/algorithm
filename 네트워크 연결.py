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


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

result = 0
edges = []
n_one_result = int(1e10)
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    if a == b and n == 1:
        n_one_result = min(n_one_result, cost)
    else:
        edges.append((cost, a, b))

edges.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
if n == 1:
    print(n_one_result)
else:
    for edge in edges:
        cost, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            result += cost
            union_parent(parent, x, y)
    print(result)
