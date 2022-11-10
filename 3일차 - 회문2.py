for t in range(1, 11):
    test_case = input().strip()
    arr = []
    for _ in range(100):
        arr.append(input().strip())
    max_num = 0
    for col in range(100):
        for row in range(100):
            col_str = ""
            for mini_row in range(row, 100):
                cutting_str = arr[col][row:mini_row + 1]
                if cutting_str == cutting_str[::-1]:
                    max_num = max(max_num, len(cutting_str))
                col_str += arr[mini_row][col]
                if col_str == col_str[::-1]:
                    max_num = max(max_num, len(col_str))

    print("#" + str(t), max_num)
