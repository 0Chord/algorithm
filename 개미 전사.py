N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

memo = [0 for _ in range(N)]
memo[0] = arr[0]
memo[1] = arr[1]
for idx in range(2, N):
    if memo[idx - 2] + arr[idx] > memo[idx - 1]:
        memo[idx] = memo[idx - 2] + arr[idx]
    else:
        memo[idx] = memo[idx-1]

print(max(memo))