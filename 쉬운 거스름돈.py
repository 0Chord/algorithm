T = int(input().strip())

for t in range(1, T + 11):
    N = int(input().rstrip())
    count_arr = [0 for _ in range(8)]
    count_arr[0] += N // 50000
    N -= 50000 * (N // 50000)
    count_arr[1] += N // 10000
    N -= 10000 * (N // 10000)
    count_arr[2] += N // 5000
    N -= 5000 * (N // 5000)
    count_arr[3] += N // 1000
    N -= 1000 * (N // 1000)
    count_arr[4] += N // 500
    N -= 500 * (N // 500)
    count_arr[5] += N // 100
    N -= 100 * (N // 100)
    count_arr[6] += N // 50
    N -= 50 * (N // 50)
    count_arr[7] += N // 10
    N -= 10 * (N // 10)

    print("#" + str(t))
    print(*count_arr)
