import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
inst_arr = []
for idx in range(n):
    inst_arr.append(list(sys.stdin.readline().rstrip().split()))

queue = deque()

for el in inst_arr:
    if el[0] == 'push':
        queue.append(int(el[1]))
    elif el[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif el[0] == 'size':
        print(len(queue))
    elif el[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif el[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif el[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
