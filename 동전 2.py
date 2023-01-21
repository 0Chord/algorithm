n, k = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    arr.append(int(input().rstrip()))

memo = [10001] * 10001
memo[0] = 0
for el in arr:
    for idx in range(el, 10001):
        memo[idx] = min(memo[idx], memo[idx - el] + 1)
if memo[k] == 10001:
    print(-1)
else:
    print(memo[k])
