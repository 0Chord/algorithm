N = int(input().rstrip())

memo = [0] * 91
memo[1] = 1
memo[2] = 1
for idx in range(3, 91):
    memo[idx] = memo[idx - 2] + memo[idx - 1]

print(memo[N])
