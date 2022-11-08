for t in range(1, 11):
    test_case = input()
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    max_num = 0

    for col in range(100):
        col_sum = 0
        col_arr = list(arr[col])
        for idx in range(100):
            col_sum += col_arr[idx]
        max_num = max(max_num, col_sum)

    for row in range(100):
        row_sum = 0
        for col in range(100):
            row_sum += arr[col][row]
        max_num = max(max_num, row_sum)
    cross_sum = 0
    reversed_cross_sum = 0
    for idx in range(100):
        cross_sum += arr[idx][idx]
        reversed_cross_sum += arr[idx][99 - idx]
    max_num = max(max_num, cross_sum, reversed_cross_sum)

    print("#" + test_case, max_num)
