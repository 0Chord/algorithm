import sys
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
dist_arr = []
for col in range(N):
    for row in range(M):
        if arr[col][row] != 0 and arr[col][row] != 6:
            dist_arr.append([arr[col][row], col, row])

zero_count = 65


def recur(idx, lst):
    global zero_count
    if idx == len(dist_arr):
        count = 0
        for el in lst:
            for e in el:
                if e == 0:
                    count += 1
        zero_count = min(zero_count, count)
        return
    if dist_arr[idx][0] == 1:
        copy_one_arr = copy.deepcopy(lst)
        copy_two_arr = copy.deepcopy(lst)
        copy_three_arr = copy.deepcopy(lst)
        copy_four_arr = copy.deepcopy(lst)
        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        recur(idx + 1, copy_one_arr)
        for col_idx in range(dist_arr[idx][1], N):
            if copy_two_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_two_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_two_arr[col_idx][dist_arr[idx][2]] = '#'
        recur(idx + 1, copy_two_arr)
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_three_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_three_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_three_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_three_arr)
        for row_idx in range(dist_arr[idx][2], M):
            if copy_four_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_four_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_four_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_four_arr)
    elif dist_arr[idx][0] == 2:
        copy_one_arr = copy.deepcopy(lst)
        copy_two_arr = copy.deepcopy(lst)
        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        for col_idx in range(dist_arr[idx][1], N):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        recur(idx + 1, copy_one_arr)

        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_two_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_two_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_two_arr[dist_arr[idx][1]][row_idx] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_two_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_two_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_two_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_two_arr)
    elif dist_arr[idx][0] == 3:
        copy_one_arr = copy.deepcopy(lst)
        copy_two_arr = copy.deepcopy(lst)
        copy_three_arr = copy.deepcopy(lst)
        copy_four_arr = copy.deepcopy(lst)
        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_one_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_one_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_one_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_one_arr)

        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_two_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_two_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_two_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_two_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_two_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_two_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_two_arr)

        for col_idx in range(dist_arr[idx][1], N):
            if copy_three_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_three_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_three_arr[col_idx][dist_arr[idx][2]] = '#'
        recur(idx + 1, copy_two_arr)
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_three_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_three_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_three_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_three_arr)

        for col_idx in range(dist_arr[idx][1], N):
            if copy_four_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_four_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_four_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_four_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_four_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_four_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_four_arr)
    elif dist_arr[idx][0] == 4:
        copy_one_arr = copy.deepcopy(lst)
        copy_two_arr = copy.deepcopy(lst)
        copy_three_arr = copy.deepcopy(lst)
        copy_four_arr = copy.deepcopy(lst)

        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        for col_idx in range(dist_arr[idx][1], N):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_one_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_one_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_one_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_one_arr)

        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_two_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_two_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_two_arr[col_idx][dist_arr[idx][2]] = '#'
        for col_idx in range(dist_arr[idx][1], N):
            if copy_two_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_two_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_two_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_two_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_two_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_two_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_two_arr)

        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_three_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_three_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_three_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_three_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_three_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_three_arr[dist_arr[idx][1]][row_idx] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_three_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_three_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_three_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_three_arr)

        for col_idx in range(dist_arr[idx][1], N):
            if copy_four_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_four_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_four_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_four_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_four_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_four_arr[dist_arr[idx][1]][row_idx] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_four_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_four_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_four_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_four_arr)
    elif dist_arr[idx][0] == 5:
        copy_one_arr = copy.deepcopy(lst)

        for col_idx in range(dist_arr[idx][1], -1, -1):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        recur(idx + 1, copy_one_arr)
        for col_idx in range(dist_arr[idx][1], N):
            if copy_one_arr[col_idx][dist_arr[idx][2]] == 6:
                break
            elif copy_one_arr[col_idx][dist_arr[idx][2]] == 0:
                copy_one_arr[col_idx][dist_arr[idx][2]] = '#'
        for row_idx in range(dist_arr[idx][2], -1, -1):
            if copy_one_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_one_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_one_arr[dist_arr[idx][1]][row_idx] = '#'
        for row_idx in range(dist_arr[idx][2], M):
            if copy_one_arr[dist_arr[idx][1]][row_idx] == 6:
                break
            elif copy_one_arr[dist_arr[idx][1]][row_idx] == 0:
                copy_one_arr[dist_arr[idx][1]][row_idx] = '#'
        recur(idx + 1, copy_one_arr)


recur(0, arr)
print(zero_count)
