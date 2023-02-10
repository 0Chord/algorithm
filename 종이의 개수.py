import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
minus_one = 0
zero = 0
one = 0


def divide(num, i, j):
    global minus_one, zero, one
    dist = arr[i][j]
    for col in range(i, i + num):
        for row in range(j, j + num):
            if arr[col][row] != dist:
                for k in range(3):
                    for n in range(3):
                        divide(num // 3, i + k * num // 3, j + n * num // 3)
                return
    if dist == 0:
        zero += 1
    elif dist == -1:
        minus_one += 1
    elif dist == 1:
        one += 1
    return


divide(N, 0, 0)

print(minus_one)
print(zero)
print(one)
