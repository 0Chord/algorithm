import sys

memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

memo[0][0][0] = 1

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b == 0 or c == 0:
                memo[a][b][c] = 1
            elif a < b < c:
                memo[a][b][c] = memo[a][b][c - 1] + memo[a][b - 1][c - 1] - memo[a][b - 1][c]
            else:
                memo[a][b][c] = memo[a - 1][b][c] + memo[a - 1][b - 1][c] + memo[a - 1][b][c - 1] - memo[a - 1][b - 1][
                    c - 1]

while True:
    n1, n2, n3 = map(int, sys.stdin.readline().rstrip().split())

    if n1 == n2 == n3 == -1:
        break
    elif n1 <= 0 or n2 <= 0 or n3 <= 0:
        print('w({0}, {1}, {2}) = {3}'.format(n1, n2, n3, memo[0][0][0]))
    elif n1 > 20 or n2 > 20 or n3 > 20:
        print('w({0}, {1}, {2}) = {3}'.format(n1, n2, n3, memo[20][20][20]))
    else:
        print('w({0}, {1}, {2}) = {3}'.format(n1, n2, n3, memo[n1][n2][n3]))
