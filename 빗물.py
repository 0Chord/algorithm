import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

rain_bowl = [[0] * w for _ in range(h)]

for idx in range(len(arr)):
    for i in range(arr[idx]):
        rain_bowl[h - 1 - i][idx] = 1

rain_cnt = 0

for idx in range(h - 1, -1, -1):
    wall_lst = []
    for i in range(w):
        if rain_bowl[idx][i] == 1:
            wall_lst.append(i)
    if len(wall_lst) > 1:
        for i in range(len(wall_lst) - 1):
            rain_cnt += wall_lst[i + 1] - wall_lst[i] - 1
print(rain_cnt)
