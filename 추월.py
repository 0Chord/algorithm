from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(n):
    queue.append(sys.stdin.readline().rstrip())

finished_arr = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for el in finished_arr:
    if queue[0] == el:
        queue.popleft()
    else:
        cnt += 1
        queue.remove(el)
print(cnt)