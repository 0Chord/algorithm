import sys
from collections import deque

R, C = map(int, sys.stdin.readline().rstrip().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
days = 0
location_arr = [0, 0]
for col in range(R):
    for row in range(C):
        if arr[col][row] == "D":
            location_arr[0] = col
            location_arr[1] = row
while True:
    rain_arr = []
    visited_arr = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    for col in range(R):
        for row in range(C):
            if arr[col][row] == "*" and not visited_arr[col][row]:
                queue.append([col, row])
                visited_arr[col][row] = True
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < R and 0 <= ny < C:
                            if arr[nx][ny] == "*" and not visited_arr[nx][ny]:
                                visited_arr[nx][ny] = True
                                queue.append([nx, ny])
                            elif arr[nx][ny] == "." and not visited_arr[nx][ny]:
                                rain_arr.append([nx, ny])
                                visited_arr[nx][ny] = True
                            elif arr[nx][ny] == "S" and not visited_arr[nx][ny]:
                                rain_arr.append([nx, ny])
                                visited_arr[nx][ny] = True

    hog_visited_arr = [[False for _ in range(C)] for _ in range(R)]
    hog_arr = []
    flag = False
    for col in range(R):
        for row in range(C):
            if arr[col][row] == "S" and not hog_visited_arr[col][row]:
                queue.append([col, row])
                hog_visited_arr[col][row] = True
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < R and 0 <= ny < C:
                            if not visited_arr[nx][ny] and (arr[nx][ny] == "." or arr[nx][ny] == "D") and [nx,
                                                                                                           ny] not in rain_arr:
                                flag = True
                                visited_arr[nx][ny] = True
                                hog_arr.append([nx, ny])
                            elif not visited_arr[nx][ny] and arr[nx][ny] == "S":
                                visited_arr[nx][ny] = True
                                queue.append([nx, ny])

    for el in hog_arr:
        arr[el[0]][el[1]] = "S"
    for el in rain_arr:
        arr[el[0]][el[1]] = "*"
    days += 1
    if arr[location_arr[0]][location_arr[1]] == "S":
        print(days)
        break
    if not flag:
        print("KAKTUS")
        break
