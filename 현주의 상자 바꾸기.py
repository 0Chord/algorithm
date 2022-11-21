T = int(input().rstrip())

for t in range(1, T + 1):
    N, Q = map(int, input().split())
    arr = []
    for _ in range(Q):
        arr.append(list(map(int, input().split())))
    result_arr = [0] * N
    for idx in range(len(arr)):
        for i in range(arr[idx][0] - 1, arr[idx][1]):
            result_arr[i] = idx + 1
    print("#" + str(t), *result_arr)
