import sys

first = list(sys.stdin.readline().rstrip())
second = list(sys.stdin.readline().rstrip())

n = len(first)
m = len(second)

dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if first[j - 1] == second[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

max_len = dp[-1][-1]
print(max_len)

if dp[-1][-1] != 0:
    answer = ""
    x = m
    y = n
    while x != 0 and y != 0:
        if first[y - 1] == second[x - 1]:
            answer += first[y - 1]
            x -= 1
            y -= 1
        else:
            if dp[x][y] == dp[x - 1][y]:
                x -= 1
            elif dp[x][y] == dp[x][y - 1]:
                y -= 1
    print(answer[::-1])
