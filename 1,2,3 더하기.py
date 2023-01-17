T = int(input().rstrip())
memo = [0] * 11
memo[1] = 1
memo[2] = 2
memo[3] = 4
for idx in range(4, 11):
    memo[idx] = memo[idx - 3] + memo[idx - 2] + memo[idx - 1]
for _ in range(T):
    n = int(input().rstrip())
    print(memo[n])
