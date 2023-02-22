import sys

t = int(sys.stdin.readline().rstrip())

memo = [0] * 101
memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2
memo[5] = 2
for idx in range(6, 101):
    memo[idx] = memo[idx-1]+memo[idx-5]
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(memo[n])
