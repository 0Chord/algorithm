import sys

n = int(sys.stdin.readline().rstrip())

input = []

for _ in range(n):
    input.append(list(map(int, sys.stdin.readline().rstrip().split())))

memo = [[0 for _ in range(3)] for _ in range(n)]

for idx in range(3):
    memo[0][idx] = input[0][idx]

for idx in range(1, n):
    if memo[idx - 1][1] < memo[idx - 1][2]:
        memo[idx][0] = input[idx][0] + memo[idx - 1][1]
    else:
        memo[idx][0] = input[idx][0] + memo[idx - 1][2]
    if memo[idx - 1][0] < memo[idx - 1][2]:
        memo[idx][1] = input[idx][1] + memo[idx - 1][0]
    else:
        memo[idx][1] = input[idx][1] + memo[idx - 1][2]
    if memo[idx - 1][0] < memo[idx - 1][1]:
        memo[idx][2] = input[idx][2] + memo[idx - 1][0]
    else:
        memo[idx][2] = input[idx][2] + memo[idx - 1][1]
print(min(memo[-1]))
