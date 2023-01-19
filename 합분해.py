n, k = map(int, input().rstrip().split())

memo = [[0 for _ in range(201)] for _ in range(201)]
for idx in range(201):
    memo[idx][0] = 1
for idx in range(201):
    memo[1][idx] = 1

for idx in range(2, 201):
    for j in range(1, 201):
        memo[idx][j] = memo[idx][j - 1] + memo[idx - 1][j]

print(memo[k][n] % 1000000000)
