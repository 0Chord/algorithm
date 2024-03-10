import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

memo = [1 for _ in range(n)]

if n == 1:
    print(max(memo))
else:
    for idx in range(1, n):
        for mini_idx in range(idx):
            if A[idx] > A[mini_idx]:
                memo[idx] = max(memo[idx], memo[mini_idx] + 1)

    print(max(memo))
