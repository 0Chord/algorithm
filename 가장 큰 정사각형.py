import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
memo = [[0 for _ in range(m)] for _ in range(n)]
for col in range(n):
    for row in range(m):
        if row == 0 or col == 0:
            memo[col][row] = arr[col][row]
        else:
            if arr[col][row] == 1 and arr[col][row - 1] == 1 and arr[col - 1][row] == 1 and arr[col - 1][row - 1] == 1:
                memo[col][row] = min(memo[col - 1][row - 1], memo[col][row - 1], memo[col - 1][row]) + 1
            else:
                memo[col][row] = arr[col][row]
max_num = 0
max_col = 0
max_row = 0
for col in range(n):
    for row in range(m):
        if max_num < memo[col][row]:
            max_num = memo[col][row]
            max_col = col
            max_row = row
print(max_num ** 2)
