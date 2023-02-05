import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)
count_arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    visited_arr = [False] * (N + 1)
    queue = deque([i])
    count = 0
    visited_arr[0] = True
    el_arr = []
    while True:
        if False not in visited_arr:
            break
        while queue:
            x = queue.popleft()
            visited_arr[x] = True
            count_arr[i][x] = count
            el_arr.append(x)
        for el in el_arr:
            for e in arr[el]:
                if not visited_arr[e]:
                    queue.append(e)
        count += 1
sum_arr = [0] * (N + 1)
sum_arr[0] = 1e8
for idx in range(1, len(count_arr)):
    for el in count_arr[idx]:
        sum_arr[idx] += el
for idx in range(len(sum_arr)):
    if sum_arr[idx] == min(sum_arr):
        print(idx)
        break
