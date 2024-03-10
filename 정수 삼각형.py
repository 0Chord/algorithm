import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

if n == 1:
    print(arr[0][0])
else:
    memo = [[0 for _ in range(idx)] for idx in range(1, n + 1)]
    memo[0][0] = arr[0][0]
    for idx in range(1, n):
        for inner_idx in range(len(arr[idx])):
            if inner_idx == 0:
                memo[idx][inner_idx] = memo[idx - 1][inner_idx] + arr[idx][inner_idx]
            elif inner_idx == len(arr[idx]) - 1:
                memo[idx][inner_idx] = memo[idx - 1][inner_idx - 1] + arr[idx][inner_idx]
            else:
                if memo[idx - 1][inner_idx - 1] > memo[idx - 1][inner_idx]:
                    memo[idx][inner_idx] = arr[idx][inner_idx] + memo[idx - 1][inner_idx - 1]
                else:
                    memo[idx][inner_idx] = arr[idx][inner_idx] + memo[idx - 1][inner_idx]
    print(max(memo[-1]))
