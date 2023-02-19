import sys

n = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
memo = [0] * n
for idx in range(n):
    if idx == 0:
        memo[0] = arr[0]
    elif idx == 1:
        memo[1] = arr[0] + arr[1]
    elif idx == 2:
        memo[2] = max(arr[1] + arr[2], arr[0] + arr[2])
    else:
        memo[idx] = max(arr[idx] + memo[idx - 2], arr[idx] + arr[idx - 1] + memo[idx - 3])
print(memo[-1])
