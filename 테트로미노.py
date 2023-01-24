N, M = map(int, input().rstrip().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

max_sum = 0

for col in range(N):
    for row in range(M - 3):
        mini_sum = 0
        for mini_row in range(4):
            mini_sum += arr[col][row + mini_row]
        max_sum = max(max_sum, mini_sum)

    if col > 0:
        for row in range(M - 1):
            mini_sum = 0
            for mini_row in range(2):
                mini_sum += arr[col - 1][row + mini_row]
                mini_sum += arr[col][row + mini_row]
            max_sum = max(max_sum, mini_sum)

        for row in range(M - 2):
            mini_sum = 0
            mini_sum += arr[col][row]
            mini_sum += arr[col][row + 1]
            mini_sum += arr[col - 1][row + 1]
            mini_sum += arr[col][row + 2]
            max_sum = max(max_sum, mini_sum)

        for row in range(1, M - 1):
            mini_sum = 0
            mini_sum += arr[col - 1][row - 1]
            mini_sum += arr[col - 1][row]
            mini_sum += arr[col][row]
            mini_sum += arr[col][row + 1]
            second_sum = 0
            second_sum += arr[col][row - 1]
            second_sum += arr[col - 1][row]
            second_sum += arr[col][row]
            second_sum += arr[col - 1][row + 1]
            max_sum = max(max_sum, mini_sum, second_sum)

        for row in range(M - 2):
            mini_arr = [0, 0, 0, 0]
            for mini_row in range(3):
                mini_arr[0] += arr[col][row + mini_row]
                mini_arr[1] += arr[col][row + mini_row]
                mini_arr[2] += arr[col - 1][row + mini_row]
                mini_arr[3] += arr[col - 1][row + mini_row]
                if mini_row == 0:
                    mini_arr[0] += arr[col - 1][row + mini_row]
                    mini_arr[2] += arr[col][row + mini_row]
                if mini_row == 2:
                    mini_arr[1] += arr[col - 1][row + mini_row]
                    mini_arr[3] += arr[col][row + mini_row]
            mini_arr_max_num = max(mini_arr)
            max_sum = max(max_sum, mini_arr_max_num)
    if col < N - 1:
        for row in range(M - 2):
            mini_sum = 0
            mini_sum += arr[col][row]
            mini_sum += arr[col][row + 1]
            mini_sum += arr[col + 1][row + 1]
            mini_sum += arr[col][row + 2]
            max_sum = max(max_sum, mini_sum)

for row in range(M):
    for col in range(N - 3):
        mini_sum = 0
        for mini_col in range(4):
            mini_sum += arr[col + mini_col][row]
        max_sum = max(max_sum, mini_sum)
    if row < M - 1:
        for col in range(N - 2):
            mini_arr = [0, 0, 0, 0, 0, 0, 0, 0]
            for mini_col in range(3):
                mini_arr[0] += arr[col + mini_col][row]
                mini_arr[1] += arr[col + mini_col][row + 1]
                mini_arr[2] += arr[col + mini_col][row + 1]
                mini_arr[3] += arr[col + mini_col][row]
                mini_arr[4] += arr[col + mini_col][row + 1]
                mini_arr[5] += arr[col + mini_col][row]
                if mini_col == 0:
                    mini_arr[2] += arr[col + mini_col][row]
                    mini_arr[3] += arr[col + mini_col][row + 1]
                    mini_arr[6] += arr[col + mini_col][row]
                    mini_arr[7] += arr[col + mini_col][row + 1]
                if mini_col == 2:
                    mini_arr[0] += arr[col + mini_col][row + 1]
                    mini_arr[1] += arr[col + mini_col][row]
                    mini_arr[6] += arr[col + mini_col][row + 1]
                    mini_arr[7] += arr[col + mini_col][row]
                if mini_col == 1:
                    mini_arr[4] += arr[col + mini_col][row]
                    mini_arr[5] += arr[col + mini_col][row + 1]
                    mini_arr[6] += arr[col + mini_col][row]
                    mini_arr[6] += arr[col + mini_col][row + 1]
                    mini_arr[7] += arr[col + mini_col][row]
                    mini_arr[7] += arr[col + mini_col][row + 1]
            max_arr_num = max(mini_arr)
            max_sum = max(max_sum, max_arr_num)

print(max_sum)
