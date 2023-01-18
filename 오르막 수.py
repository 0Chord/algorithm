N = int(input().rstrip())
memo = [[0 for _ in range(10)] for _ in range(1001)]
for idx in range(10):
    memo[0][idx] = 10 - idx

for idx in range(1, 1001):
    for i in range(10):
        memo[idx][0] += memo[idx - 1][i]
    for col in range(1, 10):
        memo[idx][col] = memo[idx][col - 1] - memo[idx - 1][col - 1]
print(memo[N - 1][0] % 10007)
