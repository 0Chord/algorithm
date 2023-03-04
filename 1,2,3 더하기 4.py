import sys

t = int(sys.stdin.readline().rstrip())

memo = [1] * 10001

for idx in range(2, 10001):
    memo[idx] += memo[idx - 2]

for idx in range(3, 10001):
    memo[idx] += memo[idx - 3]

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(memo[n])
