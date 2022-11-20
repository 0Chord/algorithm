encoding_arr = [[0 for _ in range(300)] for _ in range(300)]
encoding_arr[1][1] = 1
for row in range(2, 300):
    encoding_arr[1][row] = encoding_arr[1][row - 1] + row

for col in range(2, 300):
    for row in range(1, 299):
        encoding_arr[col][row] = encoding_arr[col - 1][row + 1] - 1
T = int(input().rstrip())

for t in range(1, T + 1):
    p, q = map(int, input().split())
    encoding_p_col = 0
    encoding_p_row = 0
    encoding_q_col = 0
    encoding_q_row = 0
    p_flag = False
    q_flag = False
    for col in range(len(encoding_arr)):
        for row in range(len(encoding_arr)):
            if encoding_arr[col][row] == p:
                encoding_p_col = col
                encoding_p_row = row
                p_flag = True
                break
        if p_flag:
            break
    for col in range(len(encoding_arr)):
        for row in range(len(encoding_arr)):
            if encoding_arr[col][row] == q:
                encoding_q_col = col
                encoding_q_row = row
                q_flag = True
                break
        if q_flag:
            break
    print("#" + str(t), encoding_arr[encoding_p_col + encoding_q_col][encoding_p_row + encoding_q_row])
