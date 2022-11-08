T = int(input())

for t in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    flag = True
    for col in range(len(arr)):
        col_arr = list(arr[col])
        col_arr.sort()
        for idx in range(len(col_arr) - 1):
            if col_arr[idx] == col_arr[idx + 1]:
                flag = False

    for row in range(len(arr)):
        row_arr = []
        for col in range(len(arr)):
            row_arr.append(arr[col][row])
        row_arr.sort()
        for idx in range(len(row_arr) - 1):
            if row_arr[idx] == col_arr[idx + 1]:
                flag = False

    for col in range(0, len(arr), 3):
        for row in range(0, len(arr), 3):
            three_by_three_arr = []
            for mini_col in range(3):
                for mini_row in range(3):
                    three_by_three_arr.append(arr[col + mini_col][row + mini_row])
            three_by_three_arr.sort()
            for idx in range(len(three_by_three_arr) - 1):
                if three_by_three_arr[idx] == three_by_three_arr[idx + 1]:
                    flag = False

    if not flag:
        print("#" + str(t), 0)
    else:
        print("#" + str(t), 1)
