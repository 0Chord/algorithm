T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = ""
    print("#"+str(t))
    for el in arr:
        print(*el)
