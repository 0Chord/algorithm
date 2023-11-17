import sys
from itertools import combinations
from math import inf

n, m, k = map(int, sys.stdin.readline().rstrip().split())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
position_list = [[x, y] for x in range(n) for y in range(m)]


def back_tracking(idx, score, col, row):
    flag = True
    if idx < k:
        for index in range(idx):
            for i in range(4):
                if col[idx] + dx[i] == col[index] and row[idx] + dy[i] == row[index]:
                    flag = False
                    break
            if not flag:
                break
    if flag:
        if idx != k:
            middle_score = score + arr[col[idx]][row[idx]]
            return back_tracking(idx + 1, middle_score, col, row)
        else:
            return score
    else:
        return -inf


result = -inf

for el in list(combinations(position_list, k)):
    col_list = []
    row_list = []
    for e in list(el):
        col_list.append(e[0])
        row_list.append(e[1])
    mini_score = arr[el[0][0]][el[0][1]]
    result_score = back_tracking(1, mini_score, col_list, row_list)
    result = max(result, result_score)
print(result)
