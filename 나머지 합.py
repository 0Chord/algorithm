import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = [0] * (M + 1)
a = [0] * (N + 1)

for idx in range(len(arr)):
    a[idx + 1] += a[idx] + arr[idx]
    cnt[a[idx + 1] % M] += 1
ans = cnt[0]

for el in cnt:
    ans += (el * (el - 1)) // 2
print(ans)
