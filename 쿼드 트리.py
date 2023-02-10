import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

res_str = ""


def divide(n, x, y):
    global res_str
    init = arr[x][y]
    for col in range(n):
        for row in range(n):
            if arr[x + col][y + row] != init:
                res_str += "("
                for i in range(2):
                    for j in range(2):
                        divide(n // 2, x + i * n // 2, y + j * n // 2)
                res_str += ")"
                return
    res_str += str(init)
    return


divide(N, 0, 0)
print(res_str)
