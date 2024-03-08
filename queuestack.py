import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
second_arr = list(map(int, sys.stdin.readline().rstrip().split()))
third_arr = list(map(int, sys.stdin.readline().rstrip().split()))
fourth = int(sys.stdin.readline().rstrip())
fifth_arr = list(map(int, sys.stdin.readline().rstrip().split()))
queue = deque()
for idx in range(len(second_arr)):
    if second_arr[idx] == 0:
        queue.appendleft(third_arr[idx])

for idx in range(fourth):
    queue.append(fifth_arr[idx])
    print(queue.popleft(), end=' ')
