T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = [0 for _ in range(5)]
    while True:
        if N == 1:
            break
        if N % 2 == 0:
            arr[0] += 1
            N = N // 2
        elif N % 3 == 0:
            arr[1] += 1
            N = N // 3
        elif N % 5 == 0:
            arr[2] += 1
            N = N // 5
        elif N % 7 == 0:
            arr[3] += 1
            N = N // 7
        elif N % 11 == 0:
            arr[4] += 1
            N = N // 11
    print("#" + str(t), *arr)
