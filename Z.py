import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())

cnt = 0


def divide(n, x, y):
    global cnt
    if x > r or x + n <= r or y > c or y + n <= c:
        cnt += n ** 2
        return

    if n > 2:
        n = n // 2
        divide(n, x, y)
        divide(n, x, y + n)
        divide(n, x + n, y)
        divide(n, x + n, y + n)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)


divide(2 ** N, 0, 0)
