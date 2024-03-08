import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
inst_arr = []
for _ in range(n):
    inst_arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque()

for el in inst_arr:
    if el[0] == 1:
        queue.appendleft(el[1])
    elif el[0] == 2:
        queue.append(el[1])
    elif el[0] == 3:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif el[0] == 4:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif el[0] == 5:
        print(len(queue))
    elif el[0] == 6:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif el[0] == 7:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif el[0] == 8:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
