N, M, x, y, K = map(int, input().rstrip().split())
arr = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
dist_arr = list(map(int, input().rstrip().split()))
dice_arr = [0, 0, 0, 0, 0, 0]


def dist(el):
    a, b, c, d, e, f = dice_arr[0], dice_arr[1], dice_arr[2], dice_arr[3], dice_arr[4], dice_arr[5]
    if el == 1:
        dice_arr[0], dice_arr[1], dice_arr[2], dice_arr[3], dice_arr[4], dice_arr[5] = d, b, a, f, e, c
    elif el == 2:
        dice_arr[0], dice_arr[1], dice_arr[2], dice_arr[3], dice_arr[4], dice_arr[5] = c, b, f, a, e, d
    elif el == 3:
        dice_arr[0], dice_arr[1], dice_arr[2], dice_arr[3], dice_arr[4], dice_arr[5] = e, a, c, d, f, b
    elif el == 4:
        dice_arr[0], dice_arr[1], dice_arr[2], dice_arr[3], dice_arr[4], dice_arr[5] = b, f, c, d, a, e


nx, ny = x, y
for idx in dist_arr:
    nx += dx[idx - 1]
    ny += dy[idx - 1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[idx - 1]
        ny -= dy[idx - 1]
        continue
    dist(idx)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice_arr[-1]
    else:
        dice_arr[-1] = arr[nx][ny]
        arr[nx][ny] = 0
    print(dice_arr[0])
