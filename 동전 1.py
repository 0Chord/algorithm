n, k = map(int, input().rstrip().split())

arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

memo = [0] * (k + 1)
memo[0] = 1

for el in arr:
    for idx in range(el, k + 1):
        memo[idx] += memo[idx - el]

print(memo[k])
