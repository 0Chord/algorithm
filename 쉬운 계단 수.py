import sys

n = int(sys.stdin.readline().rstrip())

memo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for idx in range(1, n + 1):
    if idx == 1:
        for i in range(1, 10):
            memo[i] = 1
    else:
        calc_memo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(10):
            if i == 0:
                calc_memo[0] = memo[1]
            elif i == 9:
                calc_memo[9] = memo[8]
            else:
                calc_memo[i] = memo[i - 1] + memo[i + 1]
        memo = calc_memo
res = 0
for el in memo:
    res += el
print(res % 1000000000)
