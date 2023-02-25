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

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

arr = []

for idx in range(1, n + 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            arr.append([idx, j + 1])

expect_tour_list = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort(key=lambda x: (x[0], x[1]))
for el in arr:
    x, y = el
    union_parent(parent, x, y)

flag = True

expect_parent = find_parent(parent, expect_tour_list[0])
for el in expect_tour_list:
    if find_parent(parent, el) != expect_parent:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
