T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    max_num = 0
    for col in range(N - M+1):
        for row in range(N - M+1):
            fly_count = 0
            for small_col in range(col, col + M):
                for small_row in range(row, row + M):
                    fly_count += arr[small_col][small_row]
            max_num = max(max_num, fly_count)
    print("#" + str(t), max_num)
