T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    flag = False
    for col in range(N):
        for row in range(N):
            if arr[col][row] == "o":
                count = 0
                # 가로
                for mini_row in range(row, N):
                    if arr[col][mini_row] == "o":
                        count += 1
                    else:
                        break
                if count >= 5:
                    flag = True
                count = 0
                # 세로
                for mini_col in range(col, N):
                    if arr[mini_col][row] == "o":
                        count += 1
                    else:
                        break
                if count >= 5:
                    flag = True
                # 대각선
                count = 0
                min_len = min(N - col, N - row)
                for cross_idx in range(min_len):
                    if arr[col + cross_idx][row + cross_idx] == "o":
                        count += 1
                    else:
                        break
                if count >= 5:
                    flag = True

                # 반대각
                count = 0
                max_len = min(N - col, row + 1)
                for reversed_cross_idx in range(max_len):
                    if arr[col + reversed_cross_idx][row - reversed_cross_idx] == "o":
                        count += 1
                    else:
                        break
                if count >= 5:
                    flag = True
    if flag:
        print("#" + str(t), "YES")
    else:
        print("#" + str(t), "NO")
