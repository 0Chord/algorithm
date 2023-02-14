import sys

n = int(sys.stdin.readline().rstrip())
INF = int(1e10)
memo = [INF] * (n + 1)
memo[1] = 0

for i in range(1, n):
    if i * 3 <= n:
        memo[i * 3] = min(memo[i] + 1, memo[i * 3])
    if i * 2 <= n:
        memo[i * 2] = min(memo[i] + 1, memo[i * 2])
    if i + 1 <= n:
        memo[i + 1] = min(memo[i] + 1, memo[i + 1])

print(memo[n])
