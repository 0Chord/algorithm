import math

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))
    value_count = 0
    for center_low in range(N // 2):
        for idx in range(N // 2 - center_low, N // 2 + center_low + 1):
            value_count += arr[center_low][idx]
            value_count += arr[N - 1 - center_low][idx]
    for idx in range(N):
        value_count += arr[N // 2][idx]
    print("#" + str(t), value_count)
