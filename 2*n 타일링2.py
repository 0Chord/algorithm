N = int(input().rstrip())

memo = [0] * 1001
memo[1] = 1
memo[2] = 3
for idx in range(3, 1001):
    memo[idx] = memo[idx - 1] + memo[idx - 2] * 2

print(memo[N] % 10007)
