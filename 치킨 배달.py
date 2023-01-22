N, M = map(int, input().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
home_arr = []
shop_arr = []

for col in range(N):
    for row in range(N):
        if arr[col][row] == 1:
            home_arr.append([col, row])
        elif arr[col][row] == 2:
            shop_arr.append([col, row])

min_length = 999999999999


def recur(idx, lst):
    global min_length
    if idx == len(shop_arr):
        return
    lst.append(shop_arr[idx])
    if len(lst) == M:
        length = 0
        for el in home_arr:
            mini_length = 100000000000
            for e in lst:
                mini_length = min(mini_length, abs(el[0] - e[0]) + abs(el[1] - e[1]))
            length += mini_length
        min_length = min(min_length, length)

    recur(idx + 1, lst)
    lst.pop()
    recur(idx + 1, lst)


recur(0, [])

print(min_length)

