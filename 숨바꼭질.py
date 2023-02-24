import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

queue = deque()
arr = [int(1e10)] * 100001
arr[n] = 0
queue.append(n)
while queue:
    x = queue.popleft()

    if arr[k] != int(1e10):
        print(arr[k])
        break

    if x * 2 < len(arr) and arr[x * 2] > arr[x] + 1:
        arr[x * 2] = arr[x] + 1
        queue.append(x * 2)
    if x - 1 >= 0 and arr[x - 1] > arr[x] + 1:
        arr[x - 1] = arr[x] + 1
        queue.append(x - 1)
    if x + 1 < len(arr) and arr[x + 1] > arr[x] + 1:
        arr[x + 1] = arr[x] + 1
        queue.append(x + 1)
