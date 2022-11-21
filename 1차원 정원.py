T = int(input().rstrip())

for t in range(1, T + 1):
    N, D = map(int, input().split())
    arr = [0 for _ in range(N)]
    count = 1
    for idx in range(D, N - D + 1):
        flag = True
        for i in range(idx - D, idx + D + 1):
            if i == N:
                break
            if arr[i] != 0:
                flag = False
        if flag:
            for i in range(idx - D, idx + D + 1):
                if i == N:
                    break
                arr[i] = count
            count += 1
    if 0 in arr:
        print("#" + str(t), count)
    else:
        print("#" + str(t), count - 1)
