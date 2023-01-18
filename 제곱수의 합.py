N = int(input().rstrip())

memo = [0] * 100001

for idx in range(100001):
    memo[idx] = idx

for i in range(1, 100001):
    for j in range(1, i):
        if j ** 2 > i:
            break
        if memo[i] > memo[i - j ** 2] + 1:
            memo[i] = memo[i - j ** 2] + 1

print(memo[N])
