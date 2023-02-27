import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().rstrip().split())
truck_arr = list(map(int, sys.stdin.readline().rstrip().split()))

bridges = deque([0] * w)
weights = 0
times = 0
idx = 0

while True:
    times += 1
    weights -= bridges.popleft()

    if idx < n and weights + truck_arr[idx] <= L:
        weights += truck_arr[idx]
        bridges.append(truck_arr[idx])
        idx += 1
    else:
        bridges.append(0)

    if idx == n and weights == 0:
        break
print(times)
