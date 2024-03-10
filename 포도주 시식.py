import sys

n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
memo = [0 for _ in range(n)]

for idx in range(n):
    if idx == 0:
        memo[idx] = arr[idx]
    elif idx == 1:
        memo[idx] = arr[idx - 1] + arr[idx]
    elif idx == 2:
        memo[idx] = max(arr[idx] + arr[idx - 1], arr[idx] + arr[idx - 2], memo[idx - 1])
    else:
        memo[idx] = max(memo[idx - 2] + arr[idx], arr[idx] + arr[idx - 1] + memo[idx - 3], memo[idx - 1])

print(max(memo))
