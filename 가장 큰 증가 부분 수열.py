import copy

A = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

memo = copy.deepcopy(arr)

for i in range(1, A):
    for j in range(i):
        if arr[j] < arr[i]:
            memo[i] = max(memo[j] + arr[i], memo[i])
print(max(memo))
