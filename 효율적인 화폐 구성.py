N, M = map(int, input().rstrip().split())

arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))

memo = [10001] * (M + 1)

for el in arr:
    if el <= M:
        memo[el] = 1
arr.sort()

for idx in range(1, M + 1):
    for el in arr:
        if memo[idx - el] != 10000 and idx > el:
            memo[idx] = min(memo[idx - el] + 1, memo[idx])
if memo[-1] != 10001:
    print(memo[-1])
else:
    print(-1)
