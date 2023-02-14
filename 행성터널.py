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


x_list = []
y_list = []
z_list = []

n = int(sys.stdin.readline().rstrip())
for i in range(1, n + 1):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

edges = []
for i in range(1, n):
    edges.append((abs(x_list[i][0] - x_list[i - 1][0]), x_list[i][1], x_list[i - 1][1]))
    edges.append((abs(y_list[i][0] - y_list[i - 1][0]), y_list[i][1], y_list[i - 1][1]))
    edges.append((abs(z_list[i][0] - z_list[i - 1][0]), z_list[i][1], z_list[i - 1][1]))

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges.sort()
count = 0
cost_sum = 0
for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        cost_sum += cost
        count += 1

    if count == n:
        break

print(cost_sum)
