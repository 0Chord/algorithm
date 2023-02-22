import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
memo = [0] * n
arr.sort()
memo[0] = arr[0]
for idx in range(1, n):
    if idx == 1:
        memo[idx] = max(arr[idx] + memo[idx - 1], memo[idx - 1] * arr[idx])
    else:
        memo[idx] = max(arr[idx] * arr[idx - 1] + memo[idx - 2], arr[idx] + memo[idx - 1])

print(memo[-1])
