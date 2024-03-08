import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

arr = deque(list(map(int, sys.stdin.readline().rstrip().split())))

order = 1
queue = deque()
while arr:
    if order == arr[0]:
        order += 1
        arr.popleft()
    else:
        queue.appendleft(arr.popleft())

    while queue:
        if queue[0] == order:
            order += 1
            queue.popleft()
        else:
            break

if len(queue) == 0:
    print("Nice")
else:
    print("Sad")
