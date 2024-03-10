import sys

n = int(sys.stdin.readline().rstrip())

cnt1 = 0
cnt2 = 0


def recur(input):
    global cnt1
    if input == 1 or input == 2:
        cnt1 += 1
        return 1
    else:
        return recur(input - 1) + recur(input - 2)


memo = [0 for _ in range(n + 1)]
memo[1] = 1
memo[2] = 1


def dp(input):
    global cnt2
    for idx in range(3, input + 1):
        memo[idx] = memo[idx - 1] + memo[idx - 2]
        cnt2 += 1
    return memo[input]


recur(n)
dp(n)

print(cnt1, cnt2)
