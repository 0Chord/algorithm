N = int(input().rstrip())

arr = [[]]
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

memo = [0] * 30

for idx in range(1, N + 1):
    for col in range(idx):
        memo[idx] = max(memo[idx], memo[col])
    memo[idx + arr[idx][0]] = max(memo[idx] + arr[idx][1], memo[idx + arr[idx][0]])

for idx in range(1, N + 2):
    memo[N + 1] = max(memo[idx], memo[N + 1])

print(memo[N + 1])
