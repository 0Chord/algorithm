import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
timer = 0
visited_arr = [False] * 100001

queue = deque()
queue.append([N, 0])
while True:
    x, t = queue.popleft()
    visited_arr[x] = True
    if x == K:
        print(t)
        break
    if x >= len(visited_arr):
        continue
    if 0 <= x * 2 < len(visited_arr) and not visited_arr[x * 2]:
        queue.appendleft([x * 2, t])
    if 0 <= x + 1 < len(visited_arr) and not visited_arr[x + 1]:
        queue.append([x + 1, t + 1])
    if 0 <= x - 1 < len(visited_arr) and not visited_arr[x - 1]:
        queue.append([x - 1, t + 1])
