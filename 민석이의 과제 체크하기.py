T = int(input().rstrip())

for t in range(1, T + 1):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))
    calc_arr = [i for i in range(1, N + 1)]
    for el in arr:
        calc_arr[el - 1] = 0
    result_arr = []
    for el in calc_arr:
        if el != 0:
            result_arr.append(el)
    result_arr.sort()
    print("#" + str(t), *result_arr)
