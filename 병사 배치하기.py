N = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

memo = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            memo[i] = max(memo[i], memo[j] + 1)
print(N - max(memo))
