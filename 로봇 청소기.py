import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
count = 0
stack = 0
while True:
    if arr[r][c] == 0:
        count += 1
        arr[r][c] = -1
    if d == 0:
        if arr[r][c - 1] == 0:
            d = 3
            c = c - 1
            stack = 0
            continue
        else:
            if stack == 4:
                if arr[r + 1][c] == -1:
                    r = r + 1
                    stack = 0
                    continue
                elif arr[r + 1][c] == 1:
                    break
            stack += 1
            d = 3
            continue
    elif d == 1:
        if arr[r - 1][c] == 0:
            d = 0
            r = r - 1
            stack = 0
            continue
        else:
            if stack == 4:
                if arr[r][c - 1] == -1:
                    c = c - 1
                    stack = 0
                    continue
                elif arr[r][c - 1] == 1:
                    break
            stack += 1
            d = 0
            continue
    elif d == 2:
        if arr[r][c + 1] == 0:
            d = 1
            c = c + 1
            stack = 0
            continue
        else:
            if stack == 4:
                if arr[r - 1][c] == -1:
                    r = r - 1
                    stack = 0
                    continue
                elif arr[r - 1][c] == 1:
                    break
            stack += 1
            d = 1
            continue
    elif d == 3:
        if arr[r + 1][c] == 0:
            d = 2
            r = r + 1
            stack = 0
            continue
        else:
            if stack == 4:
                if arr[r][c + 1] == -1:
                    c = c + 1
                    stack = 0
                    continue
                elif arr[r][c + 1] == 1:
                    break
            stack += 1
            d = 2
            continue
print(count)
