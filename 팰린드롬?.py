import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
memo = [[0 for _ in range(N)] for _ in range(N)]

for idx in range(N):
    for start_idx in range(N - idx):
        end_idx = idx + start_idx

        if start_idx == end_idx:
            memo[start_idx][end_idx] = 1
        elif arr[start_idx] == arr[end_idx]:
            if start_idx + 1 == end_idx:
                memo[start_idx][end_idx] = 1
            elif memo[start_idx + 1][end_idx - 1] == 1:
                memo[start_idx][end_idx] = 1

for _ in range(M):
    S, E = map(int, sys.stdin.readline().rstrip().split())
    print(memo[S - 1][E - 1])
