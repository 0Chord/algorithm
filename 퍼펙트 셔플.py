import math

T = int(input().rstrip())

for t in range(1, T + 1):
    N = int(input().rstrip())
    arr = list(input().split())
    first_arr = []
    second_arr = []
    result = []
    if N % 2 == 0:
        first_arr = arr[0:math.ceil(N // 2)]
        second_arr = arr[math.ceil(N // 2):]
        for idx in range(N // 2):
            result.append(first_arr[idx])
            result.append(second_arr[idx])
        print("#" + str(t), *result)
    else:
        first_arr = arr[0:math.ceil(N // 2) + 1]
        second_arr = arr[math.ceil(N // 2) + 1:]
        for idx in range(N // 2):
            result.append(first_arr[idx])
            result.append(second_arr[idx])
        result.append(first_arr[-1])
        print("#" + str(t), *result)

