import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
w_first = "WBWBWBWB"
b_first = "BWBWBWBW"

w_first_chess = ""
b_first_chess = ""

for _ in range(4):
    w_first_chess += w_first
    w_first_chess += b_first
    b_first_chess += b_first
    b_first_chess += w_first
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
cnt = 1000000000000
for col_idx in range(n - 7):
    for row_idx in range(m - 7):
        slice_chess = ''
        for col in range(col_idx, col_idx + 8):
            slice_chess += ''.join(arr[col][row_idx:row_idx + 8])
        w_diff_cnt = 0
        b_diff_cnt = 0
        for idx in range(len(slice_chess)):
            if w_first_chess[idx] != slice_chess[idx]:
                w_diff_cnt += 1
            if b_first_chess[idx] != slice_chess[idx]:
                b_diff_cnt += 1
        cnt = min(cnt, w_diff_cnt, b_diff_cnt)

print(cnt)
