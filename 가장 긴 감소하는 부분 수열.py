A = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

memo = [1] * A
for i in range(1, A):
    for j in range(i):
        if arr[i] < arr[j]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))