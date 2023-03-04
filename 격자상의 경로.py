import sys
from copy import deepcopy

n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * m for _ in range(n)]

dist = ((k - 1) // m, (k - 1) - ((k - 1) // m) * m)
dx = [0, 1]
dy = [1, 0]

if k == 0:
    dist_arr = [[0] * m for _ in range(n)]
    for idx in range(m):
        dist_arr[0][idx] = 1
    for idx in range(n):
        dist_arr[idx][0] = 1
    for col in range(1, n):
        for row in range(1, m):
            dist_arr[col][row] = dist_arr[col - 1][row] + dist_arr[col][row - 1]
    print(dist_arr[n - 1][m - 1])
else:
    first_arr = [[0] * ((k - 1) - ((k - 1) // m) * m+1) for _ in range((k - 1) // m+1)]
    for idx in range((k - 1) - ((k - 1) // m) * m+1):
        first_arr[0][idx] = 1
    for idx in range((k - 1) // m+1):
        first_arr[idx][0] = 1
    for col in range(1, (k - 1) // m+1):
        for row in range(1, (k - 1) - ((k - 1) // m) * m+1):
            first_arr[col][row] = first_arr[col - 1][row] + first_arr[col][row - 1]

    second_arr = [[0] * (m - ((k - 1) - ((k - 1) // m) * m)) for _ in range(n - ((k - 1) // m))]
    for idx in range(m - ((k - 1) - ((k - 1) // m) * m)):
        second_arr[0][idx] = 1
    for idx in range(n - ((k - 1) // m)):
        second_arr[idx][0] = 1
    for col in range(1, n - ((k - 1) // m)):
        for row in range(1, m - ((k - 1) - ((k - 1) // m) * m)):
            second_arr[col][row] = second_arr[col - 1][row] + second_arr[col][row - 1]
    print(first_arr[-1][-1] * second_arr[-1][-1])
