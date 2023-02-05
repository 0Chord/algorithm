import sys
import collections

N, L, R = map(int, sys.stdin.readline().rstrip().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
days = 0
while True:
    flag = False
    days_flag = False
    visited_arr = [[False for _ in range(N)] for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if not visited_arr[col][row]:
                union = []
                sum = 0
                queue = collections.deque()
                queue.append((col, row))
                visited_arr[col][row] = True
                while queue:
                    x, y = queue.popleft()
                    union.append([x, y])
                    sum += arr[x][y]

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited_arr[nx][ny] and L <= abs(
                                    arr[x][y] - arr[nx][ny]) <= R:
                                visited_arr[nx][ny] = True
                                queue.append((nx, ny))
                if sum > arr[col][row]:
                    days_flag = True
                    flag = True
                sum = sum // len(union)
                for el in union:
                    arr[el[0]][el[1]] = sum
    if days_flag:
        days += 1
    if not flag:
        break
print(days)
