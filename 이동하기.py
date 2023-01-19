N, M = map(int, input().rstrip().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

memo = [[0 for _ in range(M)] for _ in range(N)]

for col in range(N):
    for row in range(M):
        if col == 0 and row == 0:
            memo[col][row] = arr[col][row]
        elif col == 0:
            memo[col][row] = max(memo[col][row], memo[col][row - 1] + arr[col][row])
        elif row == 0:
            memo[col][row] = max(memo[col][row], memo[col - 1][row] + arr[col][row])
        else:
            memo[col][row] = max(memo[col][row], memo[col - 1][row] + arr[col][row],
                                 memo[col - 1][row - 1] + arr[col][row], memo[col][row - 1] + arr[col][row])

print(memo[-1][-1])
