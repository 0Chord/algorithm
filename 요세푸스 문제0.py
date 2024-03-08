import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i for i in range(1, n + 1)])

cnt = 0
result = []
while len(queue):
    cnt += 1
    pop_el = queue.popleft()
    if cnt == k:
        result.append(pop_el)
        cnt = 0
    else:
        queue.append(pop_el)

print('<' + ', '.join(map(str, result)) + '>')
