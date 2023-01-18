T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().rstrip().split())))
    memo = [[0 for _ in range(N)] for _ in range(2)]
    memo[0][0] = arr[0][0]
    memo[1][0] = arr[1][0]
    for idx in range(1, N):
        if arr[0][idx] + memo[1][idx - 1] < arr[1][idx] + memo[0][idx - 1]:
            memo[1][idx] = arr[1][idx] + memo[0][idx - 1]
            if arr[0][idx] + memo[1][idx - 1] > memo[0][idx - 1]:
                memo[0][idx] = arr[0][idx] + memo[1][idx - 1]
            else:
                memo[0][idx] = memo[0][idx - 1]
        else:
            memo[0][idx] = arr[0][idx] + memo[1][idx - 1]
            if arr[1][idx] + memo[0][idx - 1] > memo[1][idx - 1]:
                memo[1][idx] = arr[1][idx] + memo[0][idx - 1]
            else:
                memo[1][idx] = memo[1][idx - 1]
    max_num = max(memo[0][-1], memo[1][-1])
    print(max_num)
