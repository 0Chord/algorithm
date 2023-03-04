import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
INF = int(1e10)
memo = [INF] * (n + 1)
memo[0] = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        memo[i] = min(memo[i], memo[i - j] + arr[j])
print(memo[n])
