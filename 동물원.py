N = int(input().rstrip())
if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    memo = [0] * (N + 1)
    dp = [0] * (N + 1)
    dp[2] = 2
    dp[3] = 4
    memo[1] = 3
    memo[2] = 7
    memo[3] = 17
    if N > 3:
        for idx in range(4, N + 1):
            memo[idx] = (memo[idx - 1] * 3) % 9901
            dp[idx] = (dp[idx - 1] % 9901) + (2 * memo[idx - 3]) % 9901
            memo[idx] -= dp[idx]
    print(memo[N] % 9901)
