def select_arr(idx, value):
    global count
    if idx == N:
        if value == R:
            count += 1
        return
    if value == R:
        count += 1
        return
    else:
        select_arr(idx + 1, value + arr[idx])
        select_arr(idx + 1, value)


T = int(input().rstrip())

for t in range(1, T + 1):
    N, R = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    select_arr(0, 0)
    print("#" + str(t), count)
