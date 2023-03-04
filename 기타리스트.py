import sys

n, s, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [False] * (m + 1)
dp[s] = True

for i in range(1, n + 1):
    temp = [False] * (m + 1)
    for j in range(m + 1):
        if dp[j]:
            if j + arr[i-1] <= m:
                temp[j + arr[i-1]] = True
            if j - arr[i-1] >= 0:
                temp[j - arr[i-1]] = True
    dp = temp

res = -1
for idx in range(m, -1, -1):
    if dp[idx]:
        res = idx
        break
print(res)
