import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    result = -1
    for age in range(x, m * n + 1, m):
        if age % n == y:
            result = age
            break
        elif y == n and age % n == 0:
            result = age
            break
    print(result)
