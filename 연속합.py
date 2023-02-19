import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

memo = [-int(1e10)] * n
memo[0] = arr[0]

for idx in range(1, n):
    memo[idx] = max(memo[idx - 1] + arr[idx], arr[idx])

print(max(memo))
