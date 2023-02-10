import sys

N = int(sys.stdin.readline().rstrip())
count = 0


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)


for _ in range(N):
    count = 2 * count + 1

print(count)
hanoi(N, 1, 2, 3)
