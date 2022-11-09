T = int(input())


def count_word(arr, N, K):
    count = 0
    idx = 0
    while True:
        if arr[idx] == 0:
            idx += 1
        else:
            second_idx = 0
            while True:
                if idx + second_idx == N:
                    break
                elif arr[idx + second_idx] == 1:
                    second_idx += 1
                else:
                    break
            if second_idx == K:
                count += 1
            idx += second_idx
        if idx == N:
            break
    return count


for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    count = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for idx in range(N):
        row_arr = list(arr[idx])
        col_arr = []
        for col in range(N):
            col_arr.append(arr[col][idx])
        count += count_word(row_arr, N, K)
        count += count_word(col_arr, N, K)

    print("#" + str(t), count)
