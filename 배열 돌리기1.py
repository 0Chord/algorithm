from collections import deque
import sys

queue = deque()

n, m, r = map(int, sys.stdin.readline().rstrip().split())
arr = []
result_list = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
for idx in range(min(n, m) // 2):
    for row in range(idx, m - idx):
        queue.append(arr[idx][row])

    for col in range(idx + 1, n - idx):
        queue.append(arr[col][m - 1 - idx])

    for row in range(m - 2 - idx, idx - 1, -1):
        queue.append(arr[n - 1 - idx][row])

    for col in range(n - 2 - idx, idx, -1):
        queue.append(arr[col][idx])

    for _ in range(r):
        pop_el = queue.popleft()
        queue.append(pop_el)

    for row in range(idx, m - idx):
        el = queue.popleft()
        result_list[idx][row] = el

    for col in range(idx + 1, n - idx):
        el = queue.popleft()
        result_list[col][m - 1 - idx] = el

    for row in range(m - 2 - idx, idx - 1, -1):
        el = queue.popleft()
        result_list[n - 1 - idx][row] = el

    for col in range(n - 2 - idx, idx, -1):
        el = queue.popleft()
        result_list[col][idx] = el

for el in result_list:
    print(*el)
