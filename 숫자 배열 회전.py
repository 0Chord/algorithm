T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(list(input().split()))
    result_arr = [[] for _ in range(N)]
    for idx in range(N):
        insert_str = ""
        second_str = ""
        third_str = ""
        for row in range(N):
            insert_str += arr[row][idx]
        for row in range(N-1,-1,-1):
            second_str += arr[N-1-idx][row]
            third_str += arr[row][N-1-idx]
        result_arr[idx].append(insert_str[::-1])
        result_arr[idx].append(second_str)
        result_arr[idx].append(third_str[::-1])
    print("#"+str(t))
    for el in result_arr:
        print(*el)
