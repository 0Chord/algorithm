import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
queue = deque()
for idx in range(len(arr)):
    queue.append([arr[idx], idx + 1])
orders = list(queue)
result = []
while len(queue) >= 1:
    number = queue.popleft()
    result.append(number[1])

    if len(queue) > 0 and number[0] > 0:
        for _ in range(number[0] - 1):
            pop_el = queue.popleft()
            queue.append(pop_el)
    elif len(queue) > 0 and number[0] < 0:
        for _ in range(abs(number[0])):
            pop_el = queue.pop()
            queue.appendleft(pop_el)

print(*result)
