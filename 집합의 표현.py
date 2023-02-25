import sys

sys.setrecursionlimit(int(1e8))


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


n, m = map(int, sys.stdin.readline().rstrip().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0:
        union_parent(parent, b, c)
    else:
        x = find_parent(parent, b)
        y = find_parent(parent, c)
        if x == y:
            print("YES")
        else:
            print("NO")
