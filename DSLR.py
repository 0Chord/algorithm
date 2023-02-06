import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    A, B = list(sys.stdin.readline().rstrip().split())
    visited_arr = [False] * 10000
    queue = deque()
    queue.append((A, ""))
    while True:
        x, path = queue.popleft()
        visited_arr[int(x)] = True
        if int(x) == int(B):
            print(path)
            break
        if int(x) < int(1000):
            x = "0" * (4 - len(x)) + x
        D = str((int(x) * 2) % 10000)
        S = 0
        if int(x) == 0:
            S = str(9999)
        else:
            S = str(int(x) - 1)
        L = x[1:] + x[:1]
        R = x[-1:] + x[:-1]

        if not visited_arr[int(D)]:
            queue.append((D, path + "D"))
            visited_arr[int(D)] = True
        if not visited_arr[int(S)]:
            queue.append((S, path + "S"))
            visited_arr[int(S)] = True
        if not visited_arr[int(L)]:
            queue.append((L, path + "L"))
            visited_arr[int(L)] = True
        if not visited_arr[int(R)]:
            queue.append((R, path + "R"))
            visited_arr[int(R)] = True
