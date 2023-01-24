N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
memo = [[] for _ in range(N)]
memo[0].append(A[0])
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if len(memo[j]) > len(memo[i]):
                memo[i] = []
                memo[i] += memo[j]
    memo[i].append(A[i])
max_len = 1
max_idx = 0
for idx in range(1, N):
    if max_len < len(memo[idx]):
        max_len = len(memo[idx])
        max_idx = idx
print(max_len)
print(*memo[max_idx])
