T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    arr = [0] + list(map(int, input().rstrip().split()))
    memo = [0 for _ in range(N + 1)]
    for idx in range(1, N + 1):
        memo[idx] = memo[idx - 1] + arr[idx]

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(1, N + 2 - i):
            dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + (
                    memo[j + i - 1] - memo[j - 1])
    print(dp[1][N])
