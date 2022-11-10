for t in range(1, 11):
    square = int(input().rstrip())
    arr = []
    for _ in range(square):
        arr.append(list(map(int, input().split())))
    count = 0
    for row in range(square):
        for col in range(square):
            if arr[col][row] == 2:
                arr[col][row] = 0
            elif arr[col][row] == 1:
                break

        for col in range(square - 1, -1, -1):
            if arr[col][row] == 1:
                arr[col][row] = 0
            elif arr[col][row] == 2:
                break
    for row in range(square):
        for col in range(square - 1):
            if arr[col][row] == 1:
                mini_col = 1
                while True:
                    if arr[col + mini_col][row] == 1:
                        arr[col][row] = 0
                    if arr[col + mini_col][row] == 2:
                        break
                    mini_col += 1
    for row in range(square):
        for col in range(square):
            if arr[col][row] == 1:
                count += 1
    print("#" + str(t), count)
