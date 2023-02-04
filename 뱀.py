import sys
import collections

N = int(sys.stdin.readline().rstrip())
arr = [[0 for _ in range(N)] for _ in range(N)]
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    arr[x - 1][y - 1] = 1
L = int(sys.stdin.readline().rstrip())

dist_arr = []
for _ in range(L):
    x, c = sys.stdin.readline().rstrip().split()
    dist_arr.append([int(x), c])
dist_timer_arr = [0 for _ in range(dist_arr[-1][0] + 1)]
for el in dist_arr:
    dist_timer_arr[el[0]] = el[1]

timer = 0
queue = collections.deque()
queue.append((0, 0))

dist = 1
while True:
    timer += 1
    snake_head_x = list(queue)[0][0]
    snake_head_y = list(queue)[0][1]
    if dist == 0:
        if snake_head_x - 1 < 0:
            break
        elif arr[snake_head_x - 1][snake_head_y] == 2:
            break

        if arr[snake_head_x - 1][snake_head_y] == 1:
            queue.appendleft((snake_head_x - 1, snake_head_y))
            arr[snake_head_x - 1][snake_head_y] = 2
        else:
            queue.appendleft((snake_head_x - 1, snake_head_y))
            arr[snake_head_x - 1][snake_head_y] = 2
            snake_tail_x, snake_tail_y = queue.pop()
            arr[snake_tail_x][snake_tail_y] = 0
    elif dist == 1:
        if snake_head_y + 1 >= N:
            break
        elif arr[snake_head_x][snake_head_y + 1] == 2:
            break

        if arr[snake_head_x][snake_head_y + 1] == 1:
            queue.appendleft((snake_head_x, snake_head_y + 1))
            arr[snake_head_x][snake_head_y + 1] = 2
            arr[snake_head_x][snake_head_y] = 2
        else:
            queue.appendleft((snake_head_x, snake_head_y + 1))
            arr[snake_head_x][snake_head_y + 1] = 2
            snake_tail_x, snake_tail_y = queue.pop()
            arr[snake_tail_x][snake_tail_y] = 0
    elif dist == 2:
        if snake_head_x + 1 >= N:
            break
        elif arr[snake_head_x + 1][snake_head_y] == 2:
            break

        if arr[snake_head_x + 1][snake_head_y] == 1:
            queue.appendleft((snake_head_x + 1, snake_head_y))
            arr[snake_head_x + 1][snake_head_y] = 2
        else:
            queue.appendleft((snake_head_x + 1, snake_head_y))
            arr[snake_head_x + 1][snake_head_y] = 2
            snake_tail_x, snake_tail_y = queue.pop()
            arr[snake_tail_x][snake_tail_y] = 0
    elif dist == 3:
        if snake_head_y - 1 < 0:
            break
        elif arr[snake_head_x][snake_head_y - 1] == 2:
            break

        if arr[snake_head_x][snake_head_y - 1] == 1:
            queue.appendleft((snake_head_x, snake_head_y - 1))
            arr[snake_head_x][snake_head_y - 1] = 2
        else:
            queue.appendleft((snake_head_x, snake_head_y - 1))
            arr[snake_head_x][snake_head_y - 1] = 2
            snake_tail_x, snake_tail_y = queue.pop()
            arr[snake_tail_x][snake_tail_y] = 0
    if timer <= dist_arr[-1][0]:
        if dist_timer_arr[timer] != 0:
            if dist == 0:
                if dist_timer_arr[timer] == 'L':
                    dist = 3
                elif dist_timer_arr[timer] == 'D':
                    dist = 1
            elif dist == 1:
                if dist_timer_arr[timer] == 'L':
                    dist = 0
                elif dist_timer_arr[timer] == 'D':
                    dist = 2
            elif dist == 2:
                if dist_timer_arr[timer] == 'L':
                    dist = 1
                elif dist_timer_arr[timer] == 'D':
                    dist = 3
            elif dist == 3:
                if dist_timer_arr[timer] == 'L':
                    dist = 2
                elif dist_timer_arr[timer] == 'D':
                    dist = 0

print(timer)
