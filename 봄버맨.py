import sys
from copy import deepcopy

r, c, n = map(int, sys.stdin.readline().rstrip().split())
bomb_arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

times = 1
lst = []
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
dist_arr = []
bomb_time = 0
while True:
    if times < 4:
        if times % 3 == 1:
            dist_arr = []
            for col in range(r):
                for row in range(c):
                    if bomb_arr[col][row] == 'O':
                        dist_arr.append([col, row])
            if times == n:
                for e in bomb_arr:
                    print("".join(e))
                break
        elif times % 3 == 2:
            lst = [["O"] * c for _ in range(r)]
            bomb_arr = deepcopy(lst)
            if times == n:
                for e in bomb_arr:
                    print("".join(e))
                break
        elif times % 3 == 0:
            for el in dist_arr:
                for i in range(5):
                    nx = el[0] + dx[i]
                    ny = el[1] + dy[i]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    lst[nx][ny] = "."

            bomb_arr = deepcopy(lst)
            if times == n:
                for e in bomb_arr:
                    print("".join(e))
                break

            lst = [["O"] * c for _ in range(r)]

            dist_arr = []
            for col in range(r):
                for row in range(c):
                    if bomb_arr[col][row] == "O":
                        dist_arr.append([col, row])
            bomb_arr = deepcopy(lst)
            bomb_time = times
    else:
        if times - bomb_time == 1:
            if times == n:
                for e in bomb_arr:
                    print("".join(e))
                break
        elif times - bomb_time == 2:
            for el in dist_arr:
                for i in range(5):
                    nx = el[0] + dx[i]
                    ny = el[1] + dy[i]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    lst[nx][ny] = '.'
            bomb_arr = deepcopy(lst)
            if times == n:
                for e in bomb_arr:
                    print("".join(e))
                break
            lst = [["O"] * c for _ in range(r)]
            dist_arr = []
            for col in range(r):
                for row in range(c):
                    if bomb_arr[col][row] == "O":
                        dist_arr.append([col, row])
            bomb_arr = deepcopy(lst)
            bomb_time = times
    times += 1

