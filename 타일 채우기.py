N = int(input().rstrip())

memo = [0] * 31
memo[0] = 1
memo[2] = 3
for idx in range(3, 31):
    if idx % 2 == 0:
        memo[idx] = memo[idx - 2] * 3
        for j in range(0, idx - 2, 2):
            memo[idx] += memo[j] * 2

print(memo[N])
