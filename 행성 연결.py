import sys


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline().rstrip())

edges = []

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for col in range(n):
    for row in range(n):
        if col != row:
            edges.append((arr[col][row], col, row))

edges.sort()

parent = [i for i in range(n)]
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
