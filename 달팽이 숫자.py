import math

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    count = 1

    for j in range(math.ceil(N / 2)):
        for n in range(j, N - 1 - j):
            arr[j][n] = count
            count += 1
        if count > N ** 2:
            break

        for n in range(j, N - 1 - j):
            arr[n][N - 1 - j] = count
            count += 1
        if count > N ** 2:
            break

        for n in range(N - 1 - j, j, -1):
            arr[N - 1 - j][n] = count
            count += 1
        if count > N ** 2:
            break

        for n in range(N - 1 - j, j, -1):
            arr[n][j] = count
            count += 1
    if N % 2 == 1:
        arr[math.floor(N / 2)][math.floor(N / 2)] = N ** 2
    print("#"+str(i))
    for row in arr:
        print(*row)
