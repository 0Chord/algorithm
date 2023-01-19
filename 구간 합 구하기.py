N, M = map(int, input().rstrip().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
position_arr = []
for _ in range(M):
    position_arr.append(list(map(int, input().rstrip().split())))

memo = [[0 for _ in range(N)] for _ in range(N)]

memo[0][0] = arr[0][0]
for idx in range(1, N):
    memo[0][idx] = memo[0][idx - 1] + arr[0][idx]
    memo[idx][0] = memo[idx - 1][0] + arr[idx][0]

for col in range(1, N):
    for row in range(1, N):
        memo[col][row] = memo[col - 1][row] + memo[col][row - 1] - memo[col - 1][row - 1] + arr[col][row]

for el in position_arr:
    x1, y1, x2, y2 = el
    if x1 == 1 and y1 == 1:
        print(memo[x2 - 1][y2 - 1])
    elif x1 == x2 and y1 == y2:
        print(arr[x1 - 1][y1 - 1])
    elif x1 == 1:
        print(memo[x2 - 1][y2 - 1] - memo[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1])
    else:
        print(memo[x2 - 1][y2 - 1] - memo[x1 - 2][y2 - 1] - memo[x2 - 1][y1 - 2] + memo[x1 - 2][y1 - 2])

